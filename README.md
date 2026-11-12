# Creative AI Workflow Masterclass, Part 2: Let It Run

**Alex Coulombe Presents · Thursday, November 12, 2026 · 11 a.m.–1 p.m. Eastern.**

Direct Unreal Engine 5.9 Preview with AI, learn Forage, assemble and remix a harbor city from twelve original part recipes, and create a cinematic. The Spatial Deck and self-paced workbook share **43 ordered steps** with actions, copyable prompts, checks and recovery. The class ends by turning the scene and workflow into a small Epic AI MegaJam game plan.

[Open the Spatial Deck](https://ibrews.github.io/creative-ai-masterclass-2-deck/) · [Student workbook](https://ibrews.github.io/creative-ai-masterclass-2-deck/classroom/start-here.html) · [Class downloads](https://drive.google.com/drive/folders/1KRlqQv1tcr6ADRweYq-Z56itprH5UknJ) · [Book the class](https://www.alexcoulombepresents.com/classes/2026-11-11-creative-ai-masterclass-part-2)

## Quickstart

1. Download and extract the updated class ZIP. Open **Start Here.html**. Keep the original download separate from your working copy.
2. **Finished** opens Harbor City for an immediate AI-directed variation. **Starter** lets you import the Forage practice sample and generate the scenes yourself. Open **Unreal/PaperCity.uproject** with Windows UE 5.9.0 Preview CL60351404.
3. Connect your own signed-in agent through Unreal Assistant/native Unreal MCP, or run the numbered **Actions** inside Unreal Editor. The supplied Harbor Workshop AI Tools expose the kit through 5.9’s native Toolset Registry.
4. Open **Second Brain/unreal/Start Here.html** in the class package for sixteen portable Unreal techniques, or give its readable files to your local assistant.

The class downloads include the free **Forage 0.1.2b1 Windows beta**, the original practice assets, the existing second-brain foundations and the new Unreal field guide. Those private distribution files are supplied in the class folder; this public source repository contains the original native scenes, recipes and workshop toolset. No client files or internal knowledge index are part of the second-brain edition.

The core route requires no C++ compilation, headset, paid asset pack or paid API key. Your assistant may need a subscription, CLI and ACP adapter. Optional Canvas generation has its own provider/model and cost requirements. ECABridge is a separate optional class download; native MCP covers the required route. Keep ECABridge disabled for core rendering: its supplied preview binary asserted during shutdown after one two-job MRQ test. The default native-only route passed both jobs and closed cleanly.

## Things to Try

1. Open **05_HarborCity** and ask native `HarborWorkshopTools` to duplicate it, then add three `market_stall` recipes in the variation.
2. In Starter, use **Window → Forage → Guided Tutorial** to stage and import the original mesh, material and texture. Build the 64-placement harbor city through one native tool call.
3. Explore **06_KitGallery** and `Studio/harbor-kit.json`: twelve reusable, editable native actor families.
4. Play **LS_HarborCity**, then compare Paper City’s daylight/dusk maps and its separate **LS_LanternFestival** sequence.
5. Find the Rotator or light-color recipe in the supplied second brain. Finish by writing a tiny playable-game brief for the MegaJam, with one next milestone.

## What is supplied

Six native maps, two 12-second three-shot sequences, thirteen materials, the actual imported Forage practice mesh/material/texture, twelve part recipes, a 64-placement city layout and the Part 1 Blender/GLB starting scene. The complete offline downloads include the deck, workbook, PDFs, Forage and second brain. [Last week’s deck](https://ibrews.github.io/creative-ai-masterclass-1-deck/) remains available.

The native geometry uses built-in Unreal shapes and original procedural recipes. It is a reinterpretation of the supplied source, rather than a lossless import or a claim of neural text-to-3D generation. No Epic engine files are redistributed.

## Validation

An empty project generated the four Paper City stages and the harbor/gallery through real 5.9 native MCP calls. The first city-remix prompt passed. A separate process reopened all six saved maps and checked the Forage mesh, six horizontal bridges, gallery and cinematic structure. Native-only Movie Render Queue rendered two sets of 288 frames at 24 fps, then the editor closed cleanly. Both MP4s fully decoded; all camera views and each shot’s start, middle and end were inspected.

An independent rendered review passed all **101 slides** at desktop and phone sizes, the **45-page workbook**, offline guide and navigation. The result movie intentionally starts paused and plays correctly on demand. The second brain passed its allowlist, privacy/context and rendered review, plus its existing 40 connector and 7 gallery tests. Windows 5.9 was rehearsed; other platforms, learner account setup and optional cloud generation need their own checks. Human artistic acceptance remains separate.

## Teaching and maintenance

`course/INSTRUCTOR.md` supplies a two-hour live route. The complete deck stays the default; the original foundations, optional Canvas labs and recovery exercises remain available for independent study.

- `tools/author_part2.py`, `part2_additions.py` and `part2_support.py` own course generation.
- `tools/build_student_workbook.py` builds the self-contained HTML; copy it to `workshop/Start Here.html`.
- `small_worlds.py` and `harbor_kit.py` own native authoring; existing output maps are protected.
- `workshop/Unreal/Plugins/HarborWorkshop` supplies the original native MCP toolset.
- `tools/export_classroom.mjs` exports PDFs. `tools/package_workshop.py` requires the exact reviewed second-brain manifest and the supplied Forage plugin, excludes caches, preserves distinct Starter/Finished archive names, and verifies every archived hash.
- `evidence/` contains bounded proof records. `promo/` contains editable promo-video composition sources; `images/promo` and `media/promo` contain the signup assets.

## Credits

**Alex Coulombe Presents**. Framework: [Spatial Deck](https://github.com/ibrews/spatial-deck). Part 1 source: [Small Worlds Workshop](https://github.com/ibrews/creative-ai-masterclass-1-deck). Fonts retain their included licenses. Engine basic shapes are referenced from the learner’s installed Unreal Engine.
