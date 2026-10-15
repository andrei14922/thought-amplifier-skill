"""Validate both public editions using only the Python standard library."""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import io
import json
import posixpath
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
CODEX = '.agents/skills/thought-amplifier/'
CLAUDE = '.claude/skills/thought-amplifier/'
PACKAGE = {
    'SKILL.md', 'LICENSE.md', 'INSTALL-AND-ONBOARD.md',
    'references/thinking-methods.md', 'references/learning-and-practice.md',
    'references/continuity-and-reuse.md', 'references/romanian-guide.md',
    'references/ONBOARDING.md',
}

def sha(data):
    return hashlib.sha256(data).hexdigest()

def normalized(data):
    return data.decode('utf-8-sig').replace('\r\n', '\n').encode('utf-8')

def slug(heading):
    heading = re.sub(r'[^\w\- ]', '', heading.lower())
    return heading.replace(' ', '-')

def load():
    result = {}
    for name in ['README.md', 'LICENSE.md', 'CHANGELOG.md', 'VERSIONS.json']:
        result[name] = (ROOT / name).read_bytes()
    for directory in [CODEX, CLAUDE, 'docs', 'downloads/claude']:
        for p in (ROOT / directory).rglob('*'):
            if p.is_file():
                result[p.relative_to(ROOT).as_posix()] = p.read_bytes()
    # Include link destinations without reading unrelated local files.
    for p in (ROOT / 'assets').glob('*'):
        if p.is_file(): result[p.relative_to(ROOT).as_posix()] = b''
    return result

def validate(files):
    errors = []
    def check(condition, label):
        if not condition: errors.append(label)
    try:
        versions = json.loads(files['VERSIONS.json'])
        c, d = versions['claude'], versions['codex']
        check(c['status'] == 'public-preview', 'Claude preview status missing')
        check(c['source'] + '/' == CLAUDE and d['source'] + '/' == CODEX, 'Platform source paths changed')
        check(c['download'].endswith('thought-amplifier-claude-v' + c['version'] + '.zip'), 'Download version mismatch')
        check('/v' + c['version'] + '/' in c['download'], 'Version directory mismatch')
        manifest = json.loads(files[c['manifest']])
        check(manifest['release'] == c['version'], 'Manifest version mismatch')
        check(manifest['status'] == c['status'], 'Manifest status mismatch')
        check(manifest['fresh_claude_behavior'] == 'not-yet-validated', 'Preview evidence label missing')
        archive = files[c['download']]
        check(sha(archive) == c['sha256'], 'Archive checksum mismatch')
        checksum_path = posixpath.dirname(c['download']) + '/SHA256SUMS.txt'
        check(files[checksum_path].decode().split()[0] == c['sha256'], 'Checksum file mismatch')
        check(set(k[len(CLAUDE):] for k in files if k.startswith(CLAUDE)) == PACKAGE, 'Claude file allowlist mismatch')
        check(set(manifest['release_files']) == PACKAGE, 'Manifest file allowlist mismatch')
        for name in PACKAGE:
            check(sha(normalized(files[CLAUDE + name])) == manifest['release_files'][name], 'Claude source hash mismatch: ' + name)
        check(set(k[len(CODEX):] for k in files if k.startswith(CODEX)) == set(d['files']), 'Codex file allowlist mismatch')
        for name, expected in d['files'].items():
            data = files[CODEX + name]
            check(sha(normalized(data) if name.endswith(('.md', '.yaml')) else data) == expected, 'Codex changed: ' + name)
        public = normalized(files[CODEX + 'SKILL.md']).decode()
        port = normalized(files[CLAUDE + 'SKILL.md']).decode()
        public_body = public.split('---', 2)[2].strip()
        port_body = port.split('---', 2)[2].strip()
        check(port_body.startswith(public_body + '\n\n## Claude Use and Onboarding\n'), 'Public core drift')
        check(sha(public_body.encode()) == manifest['public_body_sha256_normalized'], 'Public body pin mismatch')
        check(sha(normalized(files[CODEX + 'SKILL.md'])) == manifest['source_skill_sha256'], 'Public source pin mismatch')
        for name, expected in manifest['public_references'].items():
            a, b = normalized(files[CODEX + 'references/' + name]), normalized(files[CLAUDE + 'references/' + name])
            check(a == b and sha(a) == expected, 'Shared reference drift: ' + name)
        check(normalized(files[CLAUDE + 'LICENSE.md']) == normalized(files['LICENSE.md']), 'License mismatch')
        front = re.match(r'---\nname: thought-amplifier\ndescription: ([^\n]+)\n---', port)
        check(bool(front) and 0 < len(front[1]) <= 200, 'Claude metadata invalid')
        check('zero question marks' not in port.lower(), 'Rigid question gate returned')
        with zipfile.ZipFile(io.BytesIO(archive)) as z:
            check(z.testzip() is None, 'ZIP CRC failed')
            check(len(z.namelist()) == len(set(z.namelist())), 'Duplicate ZIP entries')
            check(set(z.namelist()) == {'thought-amplifier/' + p for p in PACKAGE}, 'ZIP roots or file allowlist invalid')
            for item in z.infolist():
                check('..' not in PurePosixPath(item.filename).parts and not item.filename.startswith('/'), 'Unsafe ZIP path')
                check((item.external_attr >> 16) & 0o170000 != 0o120000, 'ZIP symlink')
            for name in PACKAGE:
                check(normalized(z.read('thought-amplifier/' + name)) == normalized(files[CLAUDE + name]), 'ZIP source mismatch: ' + name)
        for prefix in [CODEX, CLAUDE]:
            text = normalized(files[prefix + 'SKILL.md']).decode()
            for ref in re.findall(r'`(references/[^`]+\.md)`', text):
                check(prefix + ref in files, 'Missing skill reference: ' + ref)
        for name in ['README.md', 'docs/RELEASES.md']:
            doc = files[name].decode()
            check(c['version'] in doc and d['version'] in doc, 'Current-version documentation missing: ' + name)
            check('preview' in doc.lower(), 'Preview label missing: ' + name)
        check(c['version'] in files['docs/CLAUDE.md'].decode(), 'Claude guide version missing')
        check(d['version'] in files['docs/CODEX.md'].decode(), 'Codex guide version missing')
        for name, raw in files.items():
            if not name.endswith(('.md', '.json', '.txt', '.yaml')): continue
            text = normalized(raw).decode()
            check(not re.search(r'[A-Z]:[/\\]Users[/\\]|STORMLORD|sk-ant-[A-Za-z0-9_-]+|github_pat_[A-Za-z0-9_]+|-----BEGIN .*PRIVATE KEY-----', text, re.I), 'Private-data pattern: ' + name)
            if not name.endswith('.md'): continue
            for target in re.findall(r'\]\(([^)]+)\)', text):
                if target.startswith(('https://', 'http://', 'mailto:')): continue
                target = target.split('?', 1)[0]
                path, _, anchor = target.partition('#')
                resolved = posixpath.normpath(posixpath.join(posixpath.dirname(name), path)) if path else name
                exists = resolved in files or any(k.startswith(resolved.rstrip('/') + '/') for k in files)
                check(exists, 'Broken local link: ' + name + ' -> ' + target)
                if anchor and resolved in files and resolved.endswith('.md'):
                    headings = re.findall(r'^#{1,6}\s+(.+)$', files[resolved].decode('utf-8-sig'), re.M)
                    check(anchor in {slug(h) for h in headings}, 'Broken anchor: ' + name + ' -> ' + target)
    except (KeyError, ValueError, UnicodeError, zipfile.BadZipFile, IndexError) as exc:
        errors.append('Invalid package structure: ' + str(exc))
    return errors

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    files = load()
    errors = validate(files)
    if errors:
        print('\n'.join('FAIL: ' + e for e in errors)); raise SystemExit(1)
    print('PASS: versions, source parity, archive, license, distribution boundary and local documentation links.')
    if args.self_test:
        tests = []
        def changed(name, path, data):
            f = dict(files); f[path] = data; tests.append((name, f))
        changed('core drift', CLAUDE+'SKILL.md', files[CLAUDE+'SKILL.md'].replace(b'## Language', b'## Missing', 1))
        changed('shared reference drift', CLAUDE+'references/romanian-guide.md', b'broken')
        changed('private data', CLAUDE+'references/ONBOARDING.md', b'C:/Users/EXAMPLE/private.txt')
        changed('unexpected executable', CLAUDE+'run.py', b'print(1)')
        changed('broken link', 'README.md', files['README.md']+b'\n[bad](not-here.md)\n')
        changed('broken anchor', 'README.md', files['README.md']+b'\n[bad](docs/CODEX.md#missing)\n')
        v = json.loads(files['VERSIONS.json']); v['claude']['version']='9.9.9'
        changed('stale version', 'VERSIONS.json', json.dumps(v).encode())
        v = json.loads(files['VERSIONS.json']); v['claude']['status']='fully-validated'
        changed('false validation label', 'VERSIONS.json', json.dumps(v).encode())
        v = json.loads(files['VERSIONS.json'])
        changed('corrupt archive', v['claude']['download'], b'not a zip')
        changed('missing attribution', CLAUDE+'LICENSE.md', b'')
        for name, mutant in tests:
            if not validate(mutant): raise SystemExit('FAIL: undetected seeded fault: ' + name)
        print('PASS: all ' + str(len(tests)) + ' seeded faults rejected without changing files.')

if __name__ == '__main__':
    main()
