"""Independent native reopen check, run in a second Unreal Editor process."""
from pathlib import Path
import json
import os
import sys
import unreal as ue

sys.path.insert(0, str(Path(ue.Paths.project_dir()) / 'Content' / 'Python'))
import small_worlds as sw

rows = []
for stage, name in [('starter', '01_PaperCity'), ('dusk', '02_Dusk'), ('festival', '03_LanternFestival'), ('cinematic', '04_Cinematic')]:
    assert sw.LEVELS.load_level('/Game/SmallWorlds/Maps/' + name)
    rows.append(sw.verify(stage))
seq = ue.load_asset('/Game/SmallWorlds/Cinematics/LS_LanternFestival')
assert seq is not None
assert seq.get_display_rate().numerator == 24
assert seq.get_playback_end() == 288
cuts = seq.find_tracks_by_exact_type(ue.MovieSceneCameraCutTrack)
assert len(cuts) == 1 and len(cuts[0].get_sections()) == 3
transforms = []
for binding in seq.get_bindings():
    for track in binding.find_tracks_by_exact_type(ue.MovieScene3DTransformTrack):
        sections = track.get_sections()
        keys = sum(len(channel.get_keys()) for section in sections for channel in section.get_all_channels())
        assert keys >= 18
        transforms.append({'binding': binding.get_name(), 'keys': keys})
assert len(transforms) == 4
result = {'maps': rows, 'sequence': {'fps': 24, 'frames': 288, 'cuts': 3, 'transform_tracks': transforms},
          'scope': 'Independent saved reopen and native structure; artistic acceptance remains separate.'}
out = Path(os.environ['SMALL_WORLDS_EVIDENCE']) / 'independent-reopen.json'
out.write_text(json.dumps(result, indent=2))
ue.log('SMALL_WORLDS_REOPEN_PASS ' + str(out))
