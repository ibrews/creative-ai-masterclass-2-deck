# Creative AI Workflow Masterclass, Part 2: Let It Run

**Alex Coulombe Presents · Thursday, November 12, 2026 · 11 a.m.–1 p.m. Eastern.**

Build a paper city in Unreal Engine 5.9 Preview, light it for dusk, add a lantern festival, animate a sculpture and create a three-shot cinematic. The teaching deck and offline student workbook share 28 ordered steps. Each step includes actions, a copyable AI prompt where useful, an expected result and a recovery path.

[Open the Spatial Deck](https://ibrews.github.io/creative-ai-masterclass-2-deck/) · [Read the student workbook](https://ibrews.github.io/creative-ai-masterclass-2-deck/classroom/start-here.html) · [Last week’s deck](https://ibrews.github.io/creative-ai-masterclass-1-deck/)

## Quickstart

1. Download and extract the class workshop package. Open **Start Here.html**.
2. Use a Starter copy to build, or a Finished copy to explore the supplied maps. Open **Unreal/PaperCity.uproject** with the specified Unreal version.
3. Run numbered files in **Actions** inside Unreal Editor, in order. The assistant helps prepare and explain files; a third-party AI bridge is optional.

The project uses built-in Unreal meshes and original procedural scene recipes. It requires Python Editor Script Plugin, Editor Scripting Utilities, Sequencer Scripting and Movie Render Queue. No C++ compilation, headset, paid asset pack or paid API key is required. An assistant subscription may be needed for local coding access.

## Things to Try

1. Build **01_PaperCity** and verify the three tower wall heights, 200 / 300 / 400 cm.
2. Compare the daylight and dusk maps from the same camera.
3. Inspect the festival’s labeled trees, benches, boats and lanterns, then propose your own bounded variation.
4. Scrub the 12-second, three-shot **LS_LanternFestival** sequence and inspect each shot’s start, middle and end.
5. Save your design reason in project memory and ask a fresh chat to recover it without the old conversation.

## Teaching and maintenance

The complete route is the default; a two-hour class can focus on setup, native scene generation, one variation, the sequence and restart. The workbook contains additional rendering, recovery and extension exercises for independent study.

- `tools/author_part2.py` owns lesson text, support files and `SECTIONS` generation.
- `classroom/lessons.json` is the generated workbook source; `tools/build_student_workbook.py` builds the self-contained HTML.
- `workshop/Unreal/Content/Python/small_worlds.py` is the native scene builder. It refuses existing output maps.
- `course/sections.json` records the generated slide pool. `index.html` remains a single-file Spatial Deck.
- `evidence/` holds actual validation records. Source code and plans are not proof that a native scene rendered.

The target is **UE 5.9.0 Preview, changelist 60351404 on Windows**. Other platforms and versions require a local check. Unreal Python is editor-only; the generated scene and animation are native assets. The included Part 1 Blender/GLB source is a starting scene. The native festival is a reinterpretation, not a lossless import or neural text-to-3D generation.

## Credits

**Alex Coulombe Presents**. Framework: [Spatial Deck](https://github.com/ibrews/spatial-deck). Part 1 source: [Small Worlds Workshop](https://github.com/ibrews/creative-ai-masterclass-1-deck). Fonts retain their included licenses. Engine basic shapes are referenced from the learner’s Unreal installation; no Epic engine files are redistributed.
