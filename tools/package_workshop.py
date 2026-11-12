#!/usr/bin/env python3
"""Package a complete offline class project without Unreal caches."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import zipfile
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
EXCLUDE = {'.git', '__pycache__', '.DS_Store', 'Intermediate', 'DerivedDataCache', 'Saved', 'Binaries'}


def copy_tree(source, target):
    for p in source.rglob('*'):
        rel = p.relative_to(source)
        if p.is_file() and not any(part in EXCLUDE for part in rel.parts):
            out = target / rel
            out.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, out)


def package(mode, output):
    name = f'small-worlds-unreal-part-2-project-{mode}-2026-11-12'
    stage = output / name
    if stage.exists():
        raise SystemExit('Refusing existing package directory: ' + str(stage))
    stage.mkdir(parents=True)
    project = stage / 'Small Worlds Unreal Workshop'
    copy_tree(ROOT / 'workshop', project)
    content = project / 'Unreal' / 'Content' / 'SmallWorlds'
    if mode == 'starter' and content.exists():
        shutil.rmtree(content)  # only our new packaging copy, never the source project
    if mode == 'finished' and not list(content.rglob('*.umap')):
        raise SystemExit('No native maps: refusing a Finished package')
    deck = project / 'Deck'
    for d in ['styles', 'media', 'images', 'slides']:
        copy_tree(ROOT / d, deck / d)
    deck.mkdir(exist_ok=True)
    shutil.copy2(ROOT / 'index.html', deck / 'index.html')
    (deck / 'classroom').mkdir(exist_ok=True)
    shutil.copy2(ROOT / 'classroom/start-here.html', deck / 'classroom/start-here.html')
    for n in ['favicon.svg', 'favicon.ico', 'favicon-16.png', 'favicon-32.png', 'apple-touch-icon.png', 'social.png', 'LICENSE']:
        shutil.copy2(ROOT / n, deck / n)
    for kind in ['Workbook', 'Slides']:
        pdf = ROOT / 'evidence' / f'Small-Worlds-Part-2-{kind}.pdf'
        if pdf.exists():
            shutil.copy2(pdf, project / pdf.name)
    files = [p for p in sorted(project.rglob('*')) if p.is_file()]
    manifest = dict(subject='Small Worlds: AI for Unreal Engine, Part 2', artifact_kind='complete offline classroom project',
                    scope=mode, created_at=datetime.now(timezone.utc).isoformat(),
                    engine='UE 5.9.0 Preview CL60351404, Windows',
                    source_repository='https://github.com/ibrews/creative-ai-masterclass-2-deck',
                    packaging_reason='Complete project, offline deck and self-paced workbook with more than 30 meaningful files.',
                    files=[dict(path=p.relative_to(project).as_posix(), bytes=p.stat().st_size, sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in files])
    (project / 'package-manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
    archive = output / (name + '.zip')
    with zipfile.ZipFile(archive, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for p in sorted(project.rglob('*')):
            if p.is_file():
                z.write(p, p.relative_to(stage))
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        for f in manifest['files']:
            data = z.read('Small Worlds Unreal Workshop/' + f['path'])
            assert hashlib.sha256(data).hexdigest() == f['sha256']
    print(json.dumps(dict(path=str(archive), files=len(files)+1, bytes=archive.stat().st_size,
                          sha256=hashlib.sha256(archive.read_bytes()).hexdigest()), indent=2))


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--mode', choices=['starter', 'finished'], required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    a.output.mkdir(parents=True, exist_ok=True)
    package(a.mode, a.output)
