#!/usr/bin/env python3
"""Build the Part 2 teaching edition from one ordered set of student steps."""
from pathlib import Path
import json
import re
import shutil
from html import escape

ROOT = Path(__file__).resolve().parents[1]
lessons = []


def lesson(group, slug, title, subtitle, actions, prompt, check, fix, plate=None, links=None):
    lessons.append(dict(group=group, id=slug, title=title, subtitle=subtitle, actions=actions,
                        prompt=prompt, check=check, fix=fix, plate=plate or [title, 'Do → inspect → save → continue'],
                        image='', links=links or [], notes=''))


lesson('01 · Get ready', 'start', 'Choose your starting point', 'A self-paced route from a small brief to a saved Unreal cinematic.', [
    'Download and extract the Part 2 workshop ZIP from the class folder. Open Start Here.html in the extracted folder. Work on a copy, not inside a ZIP preview.',
    'Starting from scratch: use the Starter project. Exploring the completed work: use the Finished project and open Unreal/PaperCity.uproject. Keep the original download as your recovery copy.',
    'You can follow every numbered step without Alex. The slide deck is the teaching view; this workbook contains the full instructions. Last week’s kit is optional because the source Paper City scene is included.'
], '', 'The folder contains Actions, Unreal, SourceAssets, Studio and Recipes. Studio/design.json identifies brief SW-18.', 'If you only see a web preview, extract the complete folder. If you missed Part 1, use the included files and begin here.',
       ['Small Worlds · Part 2', 'Actions/    Run these inside Unreal', 'Unreal/     PaperCity.uproject', 'SourceAssets/  Part 1 scene', 'Studio/     Design + your notes', 'Recipes/    Reference + recovery'])

lesson('01 · Get ready', 'accounts', 'Bring one assistant and Unreal', 'Use the account you already have.', [
    'Open Codex or Claude Desktop in its local coding workspace. Sign in to an account that can read and edit a local folder. An account subscription may be needed; no paid API key is required by this workshop.',
    'Install Unreal Engine 5.9 Preview using Epic Games Launcher if available to your account and operating system. This edition was prepared for 5.9.0 Preview, changelist 60351404. Allow time for the large download.',
    'Keep a working older Unreal installation. A 5.9-saved project is not an older-version starter. If your platform lacks this Preview, follow the workbook and inspect the reference media; do not convert your only production project.'
], 'Read only: identify my operating system, installed Unreal versions, available space and whether this app can access the workshop folder. Report what is verified and what needs a local check. Do not install software or change my other projects.',
       'You know the exact engine you will open and the local workshop location.', 'If 5.9 is unavailable, stop the native steps here and read the reference route. Do not claim the Unreal scripts ran in a browser or in system Python.',
       ['Target: Unreal Engine 5.9 Preview', 'One local coding assistant', 'No headset', 'No paid asset pack', 'No paid API key'],
       [('Get Unreal Engine', 'https://www.unrealengine.com/download'), ('Get Codex', 'https://openai.com/codex/'), ('Get Claude Desktop', 'https://claude.com/download')])

lesson('01 · Get ready', 'open-folder', 'Give the assistant the whole folder', 'Its working directory matters.', [
    'In Codex choose Open folder or Add project, select the extracted workshop folder and choose Local. In Claude Desktop choose Code, a local environment and the same folder.',
    'Open a chat in this project. Ask it to read AGENTS.md, Studio/design.json and Recipes/01-start-here.md before editing.',
    'Check that it can name real files. A browser chat with pasted screenshots does not have the same local file access.'
], 'Read AGENTS.md, Studio/design.json and Recipes/01-start-here.md. Tell me the brief ID, the three tower wall heights in centimeters, the target engine and the first action file. Cite paths. Do not edit or launch anything.',
       'It reports SW-18, heights 200 / 300 / 400 cm and Actions/01_build_starter.py.', 'Reopen the enclosing folder if it cannot see Actions and Unreal together. Do not select only Unreal/Content.', ['Brief SW-18', '200 / 300 / 400 cm', 'Studio/design.json', 'Actions/01_build_starter.py'])

lesson('01 · Get ready', 'contract', 'Write a small job before running it', 'Give the agent a finish line it can check.', [
    'Open Studio/job-template.md. Replace the bracketed fields with your own goal and limits. Use the sample goal below if this is your first attempt.',
    'Permit edits only in this workshop copy. Choose a time limit, a retry limit and whether new downloads or paid services are allowed.',
    'Ask for a plan before the first write. Read it and authorize the bounded job. The assistant must report actual evidence rather than filling in a successful receipt in advance.'
], 'Draft Studio/my-job.md for this goal: build Paper City in Unreal, make a dusk variant, add a lantern festival and create a 12-second sequence. Only use this workshop and built-in Unreal assets. Budget: 30 minutes of active agent work, at most two retries per failed step, no paid services or downloads. Preserve prior maps. Finish with saved maps, verification output and a list of visual checks for me. Show the plan before running it.',
       'The job names allowed files, budget, stop conditions and the output you will inspect.', 'Shrink a broad request such as “make it amazing” to one visible change with a comparison image. Keep stretch ideas in a separate list.', ['Goal', 'Inputs + allowed files', 'Budget + retry limit', 'Checkpoint + recovery', 'Evidence + your verdict'])

lesson('01 · Get ready', 'open-unreal', 'Open the supplied Unreal project', 'A Blueprint-only project avoids a compiler setup.', [
    'In the Starter copy, double-click Unreal/PaperCity.uproject and choose your installed 5.9 Preview editor. If Windows asks which app to use, open the engine first and browse to the project.',
    'The project requests Python Editor Script Plugin, Editor Scripting Utilities, Sequencer Scripting and Movie Render Queue. If prompted, enable them and restart this project. Do not build an engine from source.',
    'On a fresh starter the final map does not exist yet. An empty editor or missing startup-map notice is expected. Open the Output Log from Window → Developer Tools → Output Log (or search the Window menu).'
], 'Help me open only Unreal/PaperCity.uproject with my installed 5.9 Preview. Verify the engine version and these enabled plugins: Python Editor Script Plugin, Editor Scripting Utilities, Sequencer Scripting and Movie Render Queue. Do not convert any other project or install C++ tools.',
       'You have the PaperCity editor open and an Output Log with no missing required plugin error.', 'If the project asks to compile C++ or reports a third-party plugin, you opened the wrong folder. This project has no C++ module and requires no AI bridge plugin.', ['PaperCity.uproject', 'Blueprint-only', 'Built-in editor plugins', 'No third-party plugin required'])

lesson('01 · Get ready', 'python-check', 'Run a harmless Python check', 'Unreal Python runs inside the editor.', [
    'In the Output Log input, keep the normal console command mode and enter: py import unreal; print(unreal.SystemLibrary.get_engine_version()). Press Enter.',
    'Look for the printed engine version in the log. A system terminal cannot import Unreal’s editor module.',
    'For action files, use Tools → Execute Python Script and browse to the numbered file in Actions. If that menu is absent, use the console form: py "FULL/PATH/TO/Actions/00_check_environment.py". Replace FULL/PATH/TO with your extracted workshop location; use forward slashes.'
], 'Explain how to run Actions/00_check_environment.py inside my already-open Unreal editor. Give me the exact py command with my local file path, using forward slashes. Do not run it in system Python. Wait for me to paste its log result.',
       'The log prints SMALL_WORLDS_ENVIRONMENT with the engine version and workshop path.', 'If you see “No module named unreal”, the command ran in the wrong Python. If the script file is missing, remove the ZIP from the path and select the extracted Actions file.', ['Output Log console', 'py "…/Actions/00_check_environment.py"', 'Expected: SMALL_WORLDS_ENVIRONMENT'])

lesson('02 · Build the world', 'starter', 'Build the daylight baseline', 'Generate native actors from a readable recipe.', [
    'In Unreal choose Tools → Execute Python Script and select Actions/01_build_starter.py. This creates /Game/SmallWorlds/Maps/01_PaperCity.',
    'Wait for SMALL_WORLDS_PASS in Output Log. In Content Browser open Content → SmallWorlds → Maps. Double-click 01_PaperCity if necessary.',
    'In the Outliner search SW_Tower. Count three towers. Select SW_Cam_Wide and use Pilot from its context menu to inspect the overall composition. Press Ctrl+S / Cmd+S to save.'
], 'Read the starter builder and Studio/design.json. Explain what Actions/01_build_starter.py will create and how it avoids replacing an existing map. Then give me its exact Unreal console command. After I run it, help me inspect the actual log and actor list.',
       'Three towers, two bridges, a canal, lamps and a cyan sculpture are visible. The log records the map and actor count.', 'If it says the map already exists, open it instead of rerunning. Preserve it by copying the whole workshop before a fresh build. If a script fails, read the first traceback before retrying.', ['01_PaperCity', 'Three towers', 'Two bridges', 'Canal + lanterns', 'Saved baseline'])

lesson('02 · Build the world', 'units', 'Check scale before polishing', 'Unreal scene units are centimeters.', [
    'Select SW_Tower_1, SW_Tower_2 and SW_Tower_3 in the Outliner. Their cube scales are Z=2, Z=3 and Z=4 because the source cube is 100 cm high.',
    'Compare the two 180 cm-wide bridges with the towers. Do not infer real-world height from the viewport zoom.',
    'Run Actions/05_verify_current.py. Keep its actual JSON result in Studio/receipts. The verifier checks structure and dimensions; you still inspect the picture.'
], 'Check the three SW_Tower actors against Studio/design.json. Explain the difference between source-mesh size, actor scale and world-space height. Report the measured values from Unreal if connected; otherwise ask me for the Details values. Do not claim you inspected the editor from source code alone.',
       'Tower wall heights are 200 / 300 / 400 cm. A receipt states the engine and actor count.', 'A 100× scale error means meters and centimeters were confused. Fix only a duplicate project, then rerun verification and inspect the framing.', ['100 cm cube × Z scale', '2 = 200 cm', '3 = 300 cm', '4 = 400 cm'])

lesson('02 · Build the world', 'materials', 'Inspect the material library', 'Separate the shape from its surface.', [
    'Open Content → SmallWorlds → Materials. Open M_Jade and inspect Base Color, Roughness and Metallic in the graph.',
    'Select a bridge rail, inspect its material slot and confirm it uses M_Jade. Compare the rough paper towers with the glossier canal.',
    'Ask your assistant for one bounded material variation. Duplicate the material in Content Browser before editing. Apply the duplicate to one selected rail and compare it with the untouched bridge.'
], 'Propose one jade-rail material variation with an exact Base Color, Roughness and Metallic value. Keep the paper walls and canal unchanged. Tell me how to duplicate M_Jade and apply the duplicate to only one bridge rail. I will inspect before accepting it.',
       'One rail uses your duplicate material; the original M_Jade and the other bridge stay available for comparison.', 'If every rail changed, you edited the shared material. Restore its prior values, duplicate it and apply the duplicate to a single actor.', ['Mesh → material slot', 'Base Color', 'Roughness', 'Metallic', 'Duplicate before editing'])

lesson('02 · Build the world', 'dusk', 'Make a dusk lighting variant', 'Change the light while preserving the daylight map.', [
    'Run Actions/02_build_dusk.py. It creates 02_Dusk as a separate map with warmer key light, emissive lanterns and point lights.',
    'Open 01_PaperCity and 02_Dusk in turn. Use the same SW_Cam_Wide view for both. Wait for shader compilation and exposure to settle.',
    'Capture both views with the same viewport size using your operating system screenshot tool. Save them in Studio/evidence and record which version you prefer.'
], 'Read the two stage definitions. Before I run 02_build_dusk.py, predict which lighting settings will change. After I supply matching screenshots and the log, compare shadow direction, lantern visibility, highlights and tower readability. Separate observations from suggestions.',
       'Both maps exist. The dusk view has visible warm lanterns and readable towers. Your verdict is recorded with the compared filenames.', 'If the view is black, confirm you are looking through a camera, not below the plinth. Check exposure and lights in the saved map before raising every intensity.', ['01_PaperCity → baseline', '02_Dusk → warm lamps', 'Same camera + same crop', 'Your visual verdict'])

lesson('02 · Build the world', 'prop-recipe', 'Turn one prop into a reusable recipe', 'A lantern has a small, understandable construction.', [
    'In small_worlds.py find the loop that creates SW_LanternPost, SW_LanternCap, SW_Lantern and SW_LanternLight. Read the dimensions and labels together.',
    'Ask the assistant to describe a new prop with the same clarity: component shapes, dimensions, materials and placement. Choose a bench, plant, kiosk or boat.',
    'Have it write the recipe into Studio/prop-proposal.md before it edits code. Require a unique actor prefix so the result can be found and removed as one scoped experiment.'
], 'Design an original small ticket kiosk for this paper city using built-in cubes, cylinders and cones. Give dimensions in centimeters, material choices, labeled parts and a placement that leaves both bridges clear. Save the proposal in Studio/prop-proposal.md. Do not build until I choose the design.',
       'You can explain every component and find where the prop will stand. No paid asset purchase is needed.', 'If the proposal needs an unavailable model or API, ask for a built-in-shape version first. Record generated asset provenance if you later use another tool.', ['Prop = labeled parts', 'Dimensions in cm', 'Materials', 'Placement', 'Acceptance view'])

lesson('02 · Build the world', 'festival', 'Build the lantern festival', 'Use repetition to make a richer scene.', [
    'Run Actions/03_build_festival.py. Open 03_LanternFestival.',
    'Inspect the added paper trees, benches, hanging lanterns, stepping stones and boats. Find each type in the Outliner by its SW_ prefix.',
    'Look through all three SW_Cam cameras. Check that bridges stay readable and that trees do not cover the towers. Save a wide view and a detail view.'
], 'Read the festival stage. List the added prop families and their actor prefixes. After I run it, guide me through a wide, bridge and sculpture inspection. Ask me to reject any placement that blocks a bridge or hides the focal point.',
       'The festival map contains repeated, individually labeled props and still reads as the same city.', 'If it is cluttered, hide a single prop family in the Outliner first. Compare that change before deleting or rebuilding anything.', ['Trees', 'Benches', 'Hanging lanterns', 'Boats + stepping stones', 'One coherent scene'])

lesson('03 · Direct the AI', 'art-direction', 'Give feedback the agent can act on', 'Name the visual problem and protect what works.', [
    'Pick one screenshot and write what you see. Example: “The hanging lanterns overlap the middle tower’s windows.”',
    'Name the protected elements: tower wall heights, camera, bridge width and accepted rail material. Limit the edit to one prop group.',
    'Ask for one revision in a duplicate map. Capture the same camera again. Accept or reject the visible result rather than the assistant’s confidence.'
], 'The hanging lanterns overlap the middle tower windows in my attached view. Propose a single change to their height or spacing. Preserve tower wall heights, both bridges, the camera and all materials. Work only in a duplicate named 03_LanternFestival_MyRevision. Explain the comparison I should inspect before editing.',
       'The revision changes one named problem and preserves your protected choices.', 'If the agent rewrites the whole scene, stop it, restore the duplicate from your baseline and restate the exact actor prefix it may change.', ['Observation', 'One allowed change', 'Protected choices', 'Same comparison view', 'Accept or reject'])

lesson('03 · Direct the AI', 'batch', 'Request a batch with a fixed budget', 'Make several ideas, then choose.', [
    'Ask for three written variations first: quiet gallery, night market and sculptural park. Keep the towers and bridges as shared constraints.',
    'Choose one to build in a separate map. Limit the job to a fixed prop count and a small number of material colors.',
    'Require the output list and a screenshot before the agent starts another variation. A batch is a set of reviewable alternatives, not permission for endless generation.'
], 'Propose three variants of Paper City: quiet gallery, night market and sculpture park. For each, give exactly three prop families, a three-color palette and one hero-camera idea. Use built-in geometry. Do not build yet. I will choose one, then authorize at most 12 new props in a separate map with a 10-minute budget.',
       'Three distinct proposals can be compared before using compute or changing files.', 'If all three descriptions are vague adjectives, ask for object counts, placement coordinates and a specific focal point.', ['Quiet gallery', 'Night market', 'Sculpture park', 'Choose → build → inspect'])

lesson('03 · Direct the AI', 'handoff', 'Compare with the original Blender scene', 'Understand what survived the engine handoff.', [
    'Open SourceAssets/Paper City.blend in Blender if installed, or inspect the included source postcard. This is the Part 1 starting scene, not a claim about every live-class edit.',
    'The native Unreal recipe is a deliberate reinterpretation: three towers, folded roofs, a canal and jade rails, expanded into a festival. It is not a lossless import.',
    'Optional: drag SourceAssets/Paper City.glb into an empty Content Browser folder in a duplicate project. Review the import options, scale, materials and hierarchy. Compare imported geometry with the native recipe; do not replace the finished map.'
], 'Compare the included Part 1 source assets with the Unreal construction recipe. Identify what is preserved, what is rebuilt and what needs checking after a GLB import: units, axes, material slots, transparency and object hierarchy. Do not call the native reconstruction a lossless import.',
       'You can distinguish an imported mesh from a native reconstruction and list the handoff checks.', 'If GLB import is unavailable in your editor configuration, keep it optional. The main workshop uses built-in Unreal meshes and does not depend on that importer.', ['Source scene → handoff', 'Units + axes', 'Materials + hierarchy', 'Rebuild ≠ lossless import'])

lesson('03 · Direct the AI', 'bridge', 'Choose how AI reaches the editor', 'The same job can use a script or a direct tool connection.', [
    'The required path uses the local coding assistant to prepare files and you to run the numbered script in Unreal. It works without a third-party bridge.',
    'An instructor with an installed, tested ue5-mcp connection can inspect actors, edit the scene and capture it directly. Ask for a read-only actor query first, then one bounded write in a duplicate map.',
    'UE 5.9 also includes experimental native tool infrastructure. Installed plugins determine which tools are present. Do not assume the built-in server exposes every operation from another bridge.'
], 'First tell me which Unreal tools this chat actually has. If none, use the script-and-manual-run route. If connected, perform a read-only query for the current map and SW_Tower actors, report actual values and stop. Do not infer connectivity from a plugin file on disk.',
       'The agent identifies its actual connection and can show a real query result or clearly use the manual route.', 'A server health response proves transport, not editing. Test one harmless read before giving write authority. Do not publish an unauthenticated editor port to the internet.', ['Local assistant → script → Unreal', 'Connected assistant → native tools → Unreal', 'Both need visible verification'])

lesson('04 · Make it move', 'sequence', 'Create the 12-second cinematic', 'Three shots and one animated sculpture.', [
    'Run Actions/04_build_cinematic.py. It creates 04_Cinematic and Content/SmallWorlds/Cinematics/LS_LanternFestival.',
    'Open the new map, then double-click LS_LanternFestival in Content Browser. In Sequencer enable the camera-cut view button on the Camera Cuts track.',
    'Scrub frames 0, 96 and 192. You should see wide, bridge and sculpture cameras. Scrub between keys to inspect the floating sculpture and camera movement.'
], 'Explain Actions/04_build_cinematic.py before I run it. Identify the three camera cuts, the 24 fps frame ranges and the animated sculpture. After I run it, help me inspect the cut track and transform keys. Do not claim rendered motion from key counts alone.',
       'The sequence lasts 288 frames at 24 fps, with three four-second shots. The sculpture moves and rotates when scrubbed.', 'If the viewport stays on your free camera, enable Sequencer’s camera-cut lock. If the sequence already exists, open it rather than overwriting it.', ['0–95 · Wide', '96–191 · Bridge', '192–287 · Sculpture', '24 fps × 12 s = 288 frames'])

lesson('04 · Make it move', 'camera', 'Review the start, middle and end', 'A camera move must hold its composition.', [
    'For the first shot inspect frames 0, 48 and 95. For the second inspect 96, 144 and 191. For the third inspect 192, 240 and 287.',
    'At each frame check the focal subject, foreground intersections, lantern visibility and whether the frame clips a roof or sculpture.',
    'If a move fails, duplicate the sequence and shorten its travel before adding more keys. Save nine frame captures or a contact sheet for your review.'
], 'Make me a nine-frame inspection checklist for LS_LanternFestival: start, middle and end of each shot. For each, I will mark framing, clipping, focal subject and lighting. If a shot fails, propose the smallest camera-key adjustment and preserve the original sequence.',
       'All three samples in each shot have been inspected. A keyframe existing is separate from good composition.', 'If a subject leaves the frame, reduce translation or retarget the end rotation in the duplicate sequence. Recheck all three samples.', ['Shot 1: 0 / 48 / 95', 'Shot 2: 96 / 144 / 191', 'Shot 3: 192 / 240 / 287'])

lesson('04 · Make it move', 'render', 'Render a short image sequence', 'Use frames first so a failed encode does not waste a render.', [
    'Open Window → Cinematics → Movie Render Queue. Add LS_LanternFestival. Confirm the job’s map is 04_Cinematic.',
    'Open the job settings. Add or keep Deferred Rendering and PNG Sequence. In Output choose a new folder inside Studio/renders, set 1280 × 720 and 24 fps, and keep the sequence frame range. Use Anti-Aliasing engine warm-up if effects need time to initialize.',
    'Render locally. Wait for completion, then open the first, middle and last frames. Keep the Output Log if the render reports an error. The optional command-line encode recipe is in Recipes/04-render.md.'
], 'Help me configure one local Movie Render Queue job for LS_LanternFestival in map 04_Cinematic: 1280×720, 24 fps, PNG frames, a new Studio/renders folder and the sequence’s 288-frame range. Explain the settings I must inspect. Do not start an overnight render or overwrite prior frames.',
       'A new folder contains the rendered frame sequence. You inspected images from all three cuts.', 'If every frame uses one camera, check the saved Camera Cuts track and job sequence. If the render is much brighter than the viewport, compare exposure and cinematic scalability before adjusting lights.', ['Map: 04_Cinematic', 'Sequence: LS_LanternFestival', '1280 × 720 · 24 fps', 'PNG frames → inspect → encode'])

lesson('04 · Make it move', 'encode', 'Turn frames into a review video', 'Inspect the movie after encoding.', [
    'If FFmpeg is already installed, ask the assistant to inspect the actual image filenames and form an encode command from that pattern. Do not assume a filename that is not present.',
    'Use H.264, yuv420p and 24 fps for the review MP4. Keep the original frames and use a new output filename.',
    'Play the full movie. Check the cut boundaries and sculpture motion, then seek to the last frame. Record any visual defect separately from decode success.'
], 'Read the filenames in my Studio/renders folder. If FFmpeg is installed, encode the 24 fps PNG sequence to a new H.264 yuv420p MP4 without deleting frames or replacing another video. Show the exact input pattern. Validate decode, duration and dimensions, then ask me to inspect the complete movie.',
       'You have a playable review MP4 and an actual decode result. Your visual verdict names any remaining issue.', 'If filenames contain gaps, repair the render or explicitly choose a correct continuous range. Do not hide missing frames by silently looping a still.', ['Rendered frames', 'Actual filename pattern', 'H.264 · yuv420p · 24 fps', 'Decode + human viewing'])

lesson('05 · Let it run', 'checkpoint', 'Save a checkpoint another chat can use', 'Memory needs concrete state.', [
    'Open Studio/project-memory.md. Record the accepted map, sequence, engine version, design choices and evidence paths.',
    'Write one sentence explaining why you kept a choice. Include a nickname or design reason that a new agent cannot guess from general knowledge.',
    'Name exactly one next action and its stop condition. Keep rejected alternatives so the next chat does not rebuild them.'
], 'Update Studio/project-memory.md from the work we actually completed. Record engine version, saved map and sequence, accepted choices, rejected alternatives, actual verification results and evidence filenames. My private design reason is: [write your own reason]. Next action: [one action]. Do not record acceptance I have not given.',
       'The note names a real saved state and an unambiguous next action.', 'If it only says “made progress,” replace that with map paths, values, filenames and a concrete next step.', ['Goal + accepted state', 'Why this choice', 'Rejected alternatives', 'Evidence paths', 'Next action + stop'])

lesson('05 · Let it run', 'restart', 'Test a fresh chat', 'Make continuity observable.', [
    'Save the Unreal project and your notes. Start a new local chat in the same workshop folder.',
    'Do not paste the old conversation. Ask the new agent to read the memory and report the private design reason, accepted map and next action.',
    'Open the cited files yourself. If the answer is wrong, repair the note or path and repeat. Keep the failed answer as useful evidence.'
], 'Read AGENTS.md and Studio/project-memory.md. Without editing anything, tell me the accepted map, sequence, private design reason, last actual check and exact next action. Cite each source. If a fact is absent, say it is absent instead of guessing.',
       'The new agent recovers your actual reason and state from files.', 'If it recites generic advice, ask it to open the exact note. If it invents a value, compare its answer with the cited text.', ['Fresh chat', 'Read saved note', 'Recall private reason', 'Check citations', 'Resume one step'])

lesson('05 · Let it run', 'failure', 'Practice one recoverable failure', 'Use a copy so the exercise cannot destroy your baseline.', [
    'Make a full duplicate of the Starter workshop. In that duplicate only, ask the agent to change the JSON key lantern_intensity to lantern_intensity_typo.',
    'Run the dusk action in the duplicate. Inspect the traceback. It should name the missing lantern_intensity key. Preserve the log before fixing it.',
    'Restore the correct key from the original design file. Use a fresh duplicate before running again because the failed action may already have created a partial map. Record the failure, repair and rerun result.'
], 'In my designated failure-exercise copy only, rename lantern_intensity to lantern_intensity_typo in Studio/design.json. Explain the expected KeyError and partial-map risk. Do not run other jobs. After I provide the traceback, restore the key from the reference file and prepare a clean retry copy; do not overwrite the partial map.',
       'You identified a specific cause, preserved evidence and repaired it without deleting your good scene.', 'If your copy already contains 02_Dusk, the existing-map guard will stop earlier. Start with the Starter package for this exercise.', ['Controlled typo', 'Read first traceback', 'Preserve partial state', 'Restore input', 'Retry in clean copy'])

lesson('05 · Let it run', 'long-job', 'Give a longer job a real boundary', 'The finish line stays visible while you are away.', [
    'Choose one extension you can verify: a new prop set, one lighting variation or one revised camera sequence.',
    'Specify the allowed map, output folder, maximum active time, retry count and checkpoint frequency. Name actions that require you, such as approving a paid generation or judging the final image.',
    'Ask for a short progress file at each completed milestone. A long-running process is not completion; the final receipt must name the saved output and known issues.'
], 'In a duplicate festival map, add at most 12 original paper-market props using built-in shapes. Preserve both bridges and the three tower wall heights. Budget: 20 minutes, two retries per failing operation, no paid services. Save progress after a complete prop family. Stop with a saved map, actor inventory and three camera captures. Report any unverified step honestly and ask me to inspect the result.',
       'The agent can explain when to continue, checkpoint, stop or ask you for a required action.', 'If the task expands into a new plugin, engine build or purchase, stop that extension and deliver the bounded result you authorized.', ['One extension', 'Exact files + map', 'Time + retries', 'Milestone evidence', 'Known limits'])

lesson('05 · Let it run', 'acceptance', 'Separate checks from your verdict', 'A successful command is only part of a useful result.', [
    'Run the current-map verifier and inspect its actual output. Confirm all four maps and the sequence open after saving.',
    'Play the sequence and your rendered movie. Compare the nine camera samples and both lighting versions.',
    'Write your own acceptance statement in Studio/receipt-template.md: accepted, accepted with named issues, or rejected. List the exact artifact and reason. The assistant may record your words after you decide.'
], 'Prepare a completion receipt from actual files and log results. Separate structural checks, visual checks and my acceptance. List the engine, four map paths, sequence, render folder, video if present, known issues and next action. Leave the human verdict pending until I provide it.',
       'The receipt identifies a real artifact and distinguishes machine checks from your decision.', 'If a check is missing, mark it unverified and perform it. Do not convert an intended command into evidence that it ran.', ['Structure', 'Saved reopen', 'Visual comparison', 'Full video viewing', 'Your verdict'])

lesson('06 · Keep creating', 'stretch-worlds', 'Build three more worlds from the same kit', 'Change the brief while keeping the method.', [
    'Choose one: a floating library, a desert observatory or a rainy street market. Start in a new workshop copy or a separate project.',
    'Ask for a small palette, reusable prop recipes, a focal point and three camera compositions. Require a baseline before effects.',
    'Run one complete loop: brief, build, inspect, revise, save, restart. Do not launch all three just because they are listed here.'
], 'Draft a bounded brief for a [floating library / desert observatory / rainy street market] using built-in Unreal geometry. Include three prop recipes, dimensions, palette, lighting intention, a focal point and three camera views. Give me a five-step build plan and measurable checks. Do not generate yet.',
       'Your new world has specific objects and a clear first milestone.', 'If the first milestone cannot be inspected quickly, reduce the object count and postpone particles or external assets.', ['Floating library', 'Desert observatory', 'Rainy street market', 'Same complete loop'])

lesson('06 · Keep creating', 'stretch-effects', 'Add effects as a separate experiment', 'Start with a visible, reversible change.', [
    'Duplicate the festival map. Choose one optional effect: drifting particles, a fountain or moving fog.',
    'Ask your agent to identify the installed tools and a supported route before creating an effect. Keep Niagara and new experimental features outside the required path.',
    'Inspect the effect during playback and in a short render with adequate warm-up. A component existing in the Outliner does not prove visible motion.'
], 'In a duplicate map, propose one subtle drifting-particle effect that preserves the paper-city style. First inspect available Niagara tooling and version support. Explain playback, warm-up, render and rollback checks. Do not change the accepted scene or install plugins.',
       'One effect is visibly present in playback and a short rendered test, or clearly remains an unverified proposal.', 'If it disappears in a render, inspect simulation warm-up and camera framing before increasing particle counts.', ['Optional experiment', 'Duplicate map', 'Playback + render', 'Warm-up', 'Rollback'])

lesson('06 · Keep creating', 'next', 'Leave yourself a route back', 'Finish with files you can reopen.', [
    'Keep your accepted project, source recipe, design JSON, notes, screenshots and receipt together. Exclude caches from a sharing copy.',
    'Close the editor, reopen the accepted map and sequence, and repeat one visual check. Keep the original class download separate from your modified copy.',
    'Return to this workbook at the first missing checkpoint whenever you resume. Bring your best result and one precise failure to office hours.'
], 'Inventory my workshop and prepare a sharing copy with project Content, Config, action scripts, design file, source assets, notes and evidence. Exclude DerivedDataCache, Intermediate and regenerable Saved caches. Preserve the working project. List files before packaging and verify the extracted copy opens.',
       'You have an accepted state, a readable receipt and a verified route to reopen it.', 'If the copy cannot open, fix missing project content or plugin requirements before calling it a usable handoff.', ['Accepted project', 'Source + design', 'Evidence + receipt', 'Clean sharing copy', 'Reopen check'])


def write_support():
    w = ROOT / 'workshop'
    files = {
      'AGENTS.md': '# Small Worlds Workshop, Part 2\n\nRead Recipes/01-start-here.md and Studio/design.json first. Target Unreal Engine 5.9 Preview. Work only in this workshop. Preserve existing maps and accepted artifacts. Unreal Python executes inside Unreal Editor, not system Python. Use Actions in order. Ask for a bounded job before editing. Report actual logs and artifacts; do not invent connectivity or visual acceptance. Keep student project memory in Studio/project-memory.md. External downloads, paid services and publishing require the learner’s task authorization.\n',
      'Studio/project-memory.md': '# My Paper City project\n\n## Goal\n\n## Accepted map and sequence\n\n## Design reason only I know\n\n## Actual checks and evidence\n\n## Rejected alternatives\n\n## Next action and stop condition\n',
      'Studio/job-template.md': '# My bounded job\n\nGoal: [visible result]\nInputs and engine: [exact files/version]\nAllowed changes: [folders/map]\nProtected choices: [what to preserve]\nTime/retry/spend limit: [limits]\nCheckpoint: [saved artifact]\nStop or ask when: [conditions]\nAcceptance evidence: [checks and views]\n',
      'Studio/receipt-template.md': '# Completion receipt\n\nProject and engine:\nSaved maps and sequence:\nInputs and design revision:\nCommands actually run:\nStructural check results:\nVisual evidence inspected:\nKnown issues and unverified checks:\nHuman verdict (pending until supplied):\nNext action:\n',
      'Recipes/01-start-here.md': '# Small Worlds, Part 2\n\nBrief SW-18: reinterpret Paper City as a lantern festival. Preserve three tower wall heights, 200 / 300 / 400 cm, and both bridges. Create native maps with the numbered Actions scripts. Run them inside Unreal Editor 5.9 Preview. First action: Actions/01_build_starter.py.\n\nThe required route needs built-in editor plugins only. The included Paper City GLB and Blender scene are the Part 1 starting scene, not the complete live-class result. Original classroom source: https://github.com/ibrews/creative-ai-masterclass-1-deck .\n\nOpen Start Here.html for every numbered instruction, copyable prompt, expected result and recovery action.\n',
      'Recipes/02-recovery.md': '# Recovery\n\nRead the first Python traceback in Output Log. Preserve your log and project before changing anything. The builder refuses an existing map to protect your work. A failed build may have created a partial map. Use a clean Starter copy for a retry, or open and inspect an already completed map. Never delete an accepted map merely to rerun a demo.\n\nUnreal Python is editor-only. The generated maps, materials and LevelSequence are native assets that remain after Python finishes.\n',
      'Recipes/03-ai-connections.md': '# AI connection routes\n\nRequired: a local coding assistant prepares files and you run the script in Unreal. Optional: a configured ue5-mcp connection can inspect, edit and capture native scenes directly. Test read-only queries before writes. Do not infer a live connection from installed files.\n\nThe instructor’s 5.9 Windows connection was tested separately. Learner setup, macOS plugin binaries and every experimental native Epic toolset are not certified by that test.\n',
      'Recipes/04-render.md': '# Rendering\n\nUse Movie Render Queue with map 04_Cinematic and sequence LS_LanternFestival, PNG frames, 1280×720, 24 fps, sequence range 0–287. Set a new output folder. Inspect actual frames from each camera cut.\n\nFor FFmpeg, inspect the actual filenames first. Example only, replace the pattern and start number with your real files:\n\n```sh\nffmpeg -framerate 24 -start_number 0 -i "YOUR_ACTUAL_PATTERN.%04d.png" -c:v libx264 -pix_fmt yuv420p -crf 18 "new-review.mp4"\n```\n\nKeep the source frames. Decode the MP4 and inspect it visually. A command exit code does not certify the image.\n',
      'Recipes/05-sources.md': '# Sources and scope\n\nClass: Alex Coulombe Presents, November 12, 2026, 11 a.m.–1 p.m. Eastern. Calendar event checked November 11.\n\nFramework: https://github.com/ibrews/spatial-deck . Part 1: https://github.com/ibrews/creative-ai-masterclass-1-deck .\n\nEpic Python guide: https://dev.epicgames.com/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-python . Sequencer camera documentation: https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-camera-cut-track-in-unreal-engine .\n\nThe paper-city recipe and new classroom materials are original AI-assisted procedural work, not a claim of text-to-3D neural generation. Built-in Engine basic shapes require an installed licensed Unreal Engine. No Epic engine files are redistributed in the student package.\n'
    }
    for rel, content in files.items():
        (w / rel).write_text(content, encoding='utf-8')
    for num, stage in enumerate(['starter', 'dusk', 'festival', 'cinematic'], 1):
        (w/'Actions'/f'{num:02}_build_{stage}.py').write_text(
          'from pathlib import Path\nimport sys\nimport unreal\n'
          'p = str(Path(unreal.Paths.project_dir()) / "Content" / "Python")\n'
          'if p not in sys.path: sys.path.insert(0, p)\n'
          'import small_worlds\nimport importlib\nimportlib.reload(small_worlds)\n'
          f'small_worlds.build("{stage}")\n')
    (w/'Actions'/'00_check_environment.py').write_text('import unreal\nfrom pathlib import Path\nprint("SMALL_WORLDS_ENVIRONMENT", unreal.SystemLibrary.get_engine_version(), Path(unreal.Paths.project_dir()).resolve().parent)\n')
    (w/'Actions'/'05_verify_current.py').write_text('import unreal, sys\nfrom pathlib import Path\np=str(Path(unreal.Paths.project_dir())/"Content"/"Python")\nif p not in sys.path: sys.path.insert(0,p)\nimport small_worlds\nprint("SMALL_WORLDS_VERIFY",small_worlds.verify())\n')
    for name in ['Paper City.glb', 'Paper City.blend', 'Postcard.png']:
        shutil.copy2(ROOT/'classroom/Creative/Starting-Scene'/name, w/'SourceAssets'/name)


def build():
    write_support()
    (ROOT/'classroom/lessons.json').write_text(json.dumps(lessons, indent=2, ensure_ascii=False)+'\n')
    groups = {}
    for l in lessons:
        groups.setdefault(l['group'], []).append(l)
    sections = []
    for i, (group, steps) in enumerate(groups.items()):
        cases = []
        for l in steps:
            idx = lessons.index(l)+1
            notes = '\n\n'.join(l['actions'])+'\n\n'+l['prompt']+'\n\nCheck: '+l['check']+'\n\nRecovery: '+l['fix']
            c = dict(title=f'{idx:02} · '+l['title'], subtitle=l['subtitle'],
                     bullets=[escape(x) for x in l['actions']], notes=notes, guideStep=l['id'],
                     example=dict(label='Your route',lines=l['plate']))
            # Short action summaries on screen; full instructions stay in notes and workbook.
            c['bullets'] = [escape(x.split('. ')[0]+'.') for x in l['actions']]
            cases.append(c)
            if l['prompt']:
                cases.append(dict(title='Ask, then inspect', subtitle=l['title'], bullets=[
                    'Copy the complete prompt from the workbook.', 'Inspect the actual result before continuing.', escape(l['check'])],
                    example=dict(label='Prompt opening',lines=[l['prompt'][:220]+'…' if len(l['prompt'])>220 else l['prompt']]),
                    guideStep=l['id'], notes=notes))
        sections.append(dict(year=f'CH {i+1}',accent=['teal','amber','purple','rose'][i%4],
                             lesson=dict(title=group.split(' · ')[1],short=group.split(' · ')[1],
                                         tagline=steps[0]['subtitle'],tags='Small Worlds · Unreal Engine 5.9 Preview'),
                             notes='Follow the numbered student workbook. Keep a saved checkpoint before the next chapter.',cases=cases))
    (ROOT/'course/sections.json').write_text(json.dumps(sections, indent=2, ensure_ascii=False)+'\n')
    html = (ROOT/'index.html').read_text()
    begin = html.index('const SECTIONS =')
    end = html.index('const BONUS =',begin)
    html = html[:begin]+'const SECTIONS ='+json.dumps(sections,ensure_ascii=False,indent=1)+';\n\n'+html[end:]
    html = re.sub(r'const BONUS = .*?;\n', 'const BONUS = '+json.dumps(dict(year='NEXT',title='Keep the world. Change the brief.',tagline='Save your accepted scene, inspect the evidence and give the next session one clear step.',notes='Use the sharing and restart checks in the workbook. The full route stays available after class.'))+';\n',html,count=1)
    bm = re.search(r'const BOOKENDS\s*=\s*', html)
    b0 = bm.start()
    _, used = json.JSONDecoder().raw_decode(html[bm.end():])
    b1 = bm.end() + used
    if html[b1:b1+1] == ';': b1 += 1
    bookends={k:dict(notes=v) for k,v in {
      'cover':'Thursday November 12, 2026, 11 a.m. to 1 p.m. Eastern. Show the completed scene first, then open the workbook. Students can follow it independently.',
      'intro':'Last week built creative workflows in Blender and Godot. Today uses Unreal and a bounded job with saved checkpoints.',
      'close':'Ask for one accepted artifact and one precise failure. Keep the full workbook and downloadable project available.'}.items()}
    html=html[:b0]+'const BOOKENDS = '+json.dumps(bookends)+';'+html[b1:]
    html=html.replace('creative-ai-masterclass-1-deck/','creative-ai-masterclass-2-deck/')
    html=html.replace('Part 1 · Alex Coulombe Presents','Part 2 · Alex Coulombe Presents')
    html=html.replace('Part 1: Set Up From Scratch','Part 2: Let It Run')
    html=html.replace('Part 1 · Set Up From Scratch','Part 2 · Let It Run')
    html=html.replace('Masterclass, Part 1','Masterclass, Part 2')
    html=html.replace('Thu Nov 5, 2026','Thu Nov 12, 2026').replace('12–2p ET','11a–1p ET')
    html=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Build an AI-assisted Unreal Engine world, light it, animate it and render a cinematic. Full self-paced workbook and original sample project. November 12, 2026, 11a ET.">',html,count=1)
    html=re.sub(r'<meta property="og:description" content="[^"]*">','<meta property="og:description" content="AI for Unreal Engine 5.9 Preview: step-by-step creative workflows, native sample scenes and a 12-second cinematic.">',html,count=1)
    html=html.replace('<div class="close-ey">See you in Part 2</div><h2 class="close-title">Build it. Restart it.</h2><p class="close-sub">Part 2: Let It Run &middot; Wed Nov 11, 11a ET</p>',
                      '<div class="close-ey">Keep creating</div><h2 class="close-title">A world you can reopen.</h2><p class="close-sub">Your scene. Your evidence. Your next step.</p>')
    html=html.replace('https://alexcoulombepresents.com/classes/2026-11-04-creative-ai-masterclass-part-1','https://alexcoulombepresents.com/classes/2026-11-11-creative-ai-masterclass-part-2')
    html=html.replace('<div class="close-qr-row"><div class="qr-card"><img src="images/class-page.svg" alt="QR code for the class page"><div class="qr-label">Class page</div><div class="qr-badge b-teal">Class information</div></div></div>',
                      '<div class="contact-row"><a class="contact-pill" href="classroom/start-here.html">Open the full student workbook ↗</a></div>')
    # Isolate presentation preferences from Part 1 in the same browser.
    html=html.replace("'sd-cfg'","'sd-part2-cfg'")
    (ROOT/'index.html').write_text(html)
    print(len(lessons),'workbook steps;',sum(1+len(s['cases']) for s in sections)+4,'visible content slides plus settings')


if __name__=='__main__':
    build()
