"""Forage, native 5.9 AI and the original Harbor City teaching route."""
NOTES='https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-9-release-notes?lang=en-US'
MCP='https://dev.epicgames.com/documentation/unreal-engine/unreal-mcp-in-unreal-editor'
PANEL='https://dev.epicgames.com/documentation/unreal-engine/run-external-ai-agents-in-the-unreal-assistant-panel-in-unreal-engine'
PYTHON='https://dev.epicgames.com/documentation/unreal-engine/using-python-with-ai-agents-in-unreal-engine'
CANVAS='https://dev.epicgames.com/documentation/unreal-engine/unreal-canvas-overview-in-unreal-engine'
FOLDER='https://drive.google.com/drive/folders/1KRlqQv1tcr6ADRweYq-Z56itprH5UknJ'
FORAGE='https://www.alexcoulombepresents.com/lab/forage'


def add_lessons(lesson):
    lesson('01 · Get ready','second-brain','Give your agent the Unreal field guide','Useful techniques, with your own project memory kept separate.',[
        'The class ZIP includes Second Brain: the existing creative-workflow foundations plus sixteen Unreal techniques. Open Second Brain/unreal/Start Here.html for the offline searchable guide, or read Second Brain/unreal/README.md.',
        'Ask your local assistant to search this folder for a relevant symptom before guessing. Each technique gives actions, a visible check and its evidence scope. The package uses original classroom and generic examples, not client files or an internal knowledge index.',
        'Keep your own goals, private design reasons and progress in Studio/project-memory.md. Reading the guide needs no connector installation. The optional acp-kit connector supports macOS/Linux; Windows learners can use local files and the HTML guide.'
    ],'Read the supplied Second Brain/unreal/README.md. Find the Rotator, light-color and native MCP tool-discovery recipes. For each, cite its file and stable ID, summarize the gotcha and say what check proves it was handled. Keep my own project memory in Studio; do not search other folders or send my files anywhere.',
       'Your assistant can retrieve a specific Unreal technique and cite the supplied file before using it.',
       'If Second Brain is absent, download the updated class ZIP or its separate companion package. Do not connect an internal or workplace knowledge base as a substitute.',
       ['16 Unreal techniques','Offline search + readable files','Generic classroom examples','Your memory stays local'],[('Class companion download',FOLDER),('Existing Second Brain portal','https://www.alexcoulombepresents.com/members/second-brain')])

    lesson('02 · Meet your AI art team','ai59','What changed in 5.9 Preview?','Open a scene, talk to your agent and watch the editor work.',[
        'Open the Finished project and load /Game/SmallWorlds/Maps/05_HarborCity. This is the supplied original kit assembled into a larger miniature port; the central token arrived through Forage.',
        '5.9 brings external agents into the Unreal Assistant panel, expands native MCP toolsets and improves editor Python. The workshop includes a small native MCP toolset so your agent can build and remix this city.',
        'Unreal Canvas adds a separate experimental workspace for generated media, meshes and spatial annotations. We will distinguish edits to real scene actors from generated images of the scene. Optional provider setup is covered later.'
    ],'', 'You can navigate the city, locate the Forage monument and name the tools you will use.',
       'If the Finished map is absent, download Finished from the class folder. A Starter intentionally contains no generated maps.',
       ['Unreal Assistant + your agent','Native Unreal MCP','Editor Python + custom tools','Forage asset selection','Canvas + spatial annotations'],[('5.9 Preview release notes',NOTES)])

    lesson('02 · Meet your AI art team','native-connect','Connect your agent inside Unreal','The panel connects the current editor for you.',[
        'In Edit → Plugins confirm Unreal Assistant, Unreal MCP and All Toolsets are enabled. Restart if you changed a plugin. Open Window → Unreal Assistant, or click Assistant on the status bar.',
        'For Codex or Claude Code, install its CLI and sign in with your own account. The panel also needs Node.js and the matching ACP adapter: npm install -g @agentclientprotocol/codex-acp or npm install -g @agentclientprotocol/claude-agent-acp. Restart Unreal after installation.',
        'Open Edit → Editor Preferences → General → Unreal Assistant → External Agent. Select your agent and enable Use External Agent. Review the project command approval and choose Allow to run that agent. Send the read-only prompt below and expand Required Actions to see the tools.'
    ],'Read only: identify this Unreal editor’s project, engine and available toolsets. Find HarborWorkshopTools and list its part IDs. Report which scene is open and which actors I selected. Do not modify the project.',
       'The agent reports PaperCity, the 5.9 engine and twelve kit IDs from real tools.',
       'If the adapter is missing, restart the editor to refresh PATH. Alternative: Editor Preferences → Agentic Workflows → Model Context Protocol → choose your client → Generate Client Config; run the external agent from the generated config’s folder. The fallback Actions scripts also work.',
       ['Enable plugins','Choose your own signed-in agent','Allow this project command','Read-only scene query'],[('External agent panel setup',PANEL),('Native MCP setup and config',MCP)])

    lesson('02 · Meet your AI art team','first-win','Your first AI-directed city edit','One prompt, a visible new market and a saved variation.',[
        'Start from Finished with 05_HarborCity open. Ask the agent to duplicate it using HarborWorkshopTools.duplicate_city with variant_name 07_MyHarbor. Keep 05_HarborCity as your reference.',
        'Use the prompt below. Watch Required Actions: the agent should inspect the catalog, duplicate the map and add three market_stall parts at the specified positions. Approve edits for this workshop copy when the client asks.',
        'Inspect the new stalls in the Outliner, frame one with F and compare the variation with the reference. Ask the agent to save_current_scene. This is a native scene change you can select, move and reopen.'
    ],'Use the native HarborWorkshopTools. Read list_parts, then duplicate_city("07_MyHarbor"). In that new map add three market_stall parts named HK_MyMarket_1, HK_MyMarket_2 and HK_MyMarket_3 at (-600,-2050,0), (0,-2050,0), (600,-2050,0), yaw 0 degrees. Show me the saved map and the created actor labels, then save_current_scene. Do not change the reference map or add downloads.',
       'The new map contains three named native market stalls and the reference is unchanged.',
       'If 07_MyHarbor already exists, choose another unused name. If tools are not discovered, reopen the editor with Harbor Workshop AI Tools enabled; do not assume a chat response changed the scene.',
       ['Duplicate → add 3 parts → inspect → save','Three placements, not one vague city prompt'])

    lesson('03 · Forage and your kit','forage-install','Your free Forage copy','The class package includes the Windows beta.',[
        'The updated class project includes Plugins/ForageBeta. Open Edit → Plugins, search Forage Beta and confirm it is enabled. If you are using another project, extract the supplied Forage Windows ZIP and copy its complete ForageBeta folder into that project’s Plugins folder.',
        'Check the descriptor path: Plugins/ForageBeta/ForageBeta.uplugin. Restart Unreal, then find Window → Forage → Guided Tutorial and Open Dashboard.',
        'Use the bundled original practice pack for our shared exercise. It needs no Fab account or paid asset pack. Forage selects and brings existing assets into a project; our agent composes those assets into a scene.'
    ],'Read only: verify ForageBeta/ForageBeta.uplugin and Tools/Win64/Forage.exe in this project. Explain how I open the Guided Tutorial. Do not sign into Epic or buy anything for me.',
       'Window → Forage is present in the 5.9 Windows editor.',
       'If Unreal asks to compile a plugin, verify you used the class Windows package and exact engine build. The current beta is Windows-only; other platforms can inspect the Finished project and reference media.',
       ['Free to class attendees','Windows 5.9 Preview','Original practice pack','No Fab sign-in for this exercise'],[('Forage download and install guide',FORAGE),('Class downloads',FOLDER)])

    lesson('03 · Forage and your kit','forage-import','Import only the parts you need','One mesh, its material and its texture.',[
        'Use a fresh Starter project for the import exercise. Open Window → Forage → Guided Tutorial. The first dialog asks to stage the practice selection in this project’s Saved/ForageBeta folder. Choose Yes to stage it.',
        'Read the second dialog. It lists the three selected files and asks before adding them to project Content. Choose Yes. This separates preview/staging from the actual import.',
        'Press Ctrl+Space and open Content → ForageBetaSample. Locate SM_ForageToken, M_ForageToken and T_ForageToken. Drag SM_ForageToken into the viewport. In the tested 5.9 layout the browser selection can be empty, so browse to the folder directly.'
    ],'Inspect /Game/ForageBetaSample. Report the imported Static Mesh, Material and Texture, and the mesh’s material reference. Do not substitute an unrelated Engine shape. We will use this actual imported token in our city.',
       'Three native content files exist and the token displays with its bound material and texture.',
       'If files already exist in Finished, use a fresh Starter for the before/after exercise. Preserve modified imports. Missing files usually mean the second import confirmation was declined.',
       ['Stage selection','Review 3 files','Approve Content import','Place the actual mesh'])

    lesson('03 · Forage and your kit','kit-gallery','Explore the twelve-part city kit','Readable recipes make a useful vocabulary for your agent.',[
        'In Finished, open /Game/SmallWorlds/Maps/06_KitGallery. In Starter, run Actions/07_build_gallery.py inside Unreal, or ask HarborWorkshopTools.build_kit_gallery to create the gallery.',
        'Open Studio/harbor-kit.json. The exact IDs are quay, townhouse, warehouse, tower, bridge, market_stall, tree, lantern, boat, arch, plaza and skyrail. Dimensions and positions are centimeters; yaw is degrees.',
        'Select a KIT_ anchor and expand its Outliner folder. Each part is composed from named native mesh actors. Ask the agent for a catalog ID and placement; spawn_part or the add_part MCP tool assembles the complete recipe.'
    ],'Read Studio/harbor-kit.json and the native list_parts tool. Describe the twelve parts. Propose a canal city, a hillside village and a floating market using this same kit. For each, name the focal point, five part IDs and one camera. Do not build the three ideas yet.',
       'You can name a real part, see its native construction and direct its placement with dimensions.',
       'If the gallery already exists, open it rather than rerunning the builder. To move or duplicate an assembled family manually, select its whole hierarchy; selecting one child only moves that mesh.',
       ['12 reusable recipes','Native actor families','Exact IDs + centimeters','One kit, many worlds'])

    lesson('03 · Forage and your kit','harbor-build','Build the Harbor of a Thousand Lanterns','A complete city from one native AI tool call.',[
        'In a Starter, complete the Forage practice import first. Read Studio/harbor-city.json: it contains 64 placements from the original kit, including quays, a market, footbridges, boats and an elevated skyrail.',
        'Ask the connected agent to call HarborWorkshopTools.build_harbor_city. The supplied tool builds /Game/SmallWorlds/Maps/05_HarborCity and LS_HarborCity. Alternative: File → Execute Python Script → Actions/06_build_city.py.',
        'Inspect the city, the three cameras and the central Forage token. Open /Game/SmallWorlds/Cinematics/LS_HarborCity, enable camera cuts and play the 12-second sequence. Compare it with the supplied result movie.'
    ],'Use native Unreal MCP to find HarborWorkshopTools. Verify the Forage practice mesh is installed, read list_parts, then call build_harbor_city once. Inspect the real map, call verify_city and show the three cameras and LS_HarborCity. Preserve any existing maps; if 05_HarborCity exists, open it instead of rebuilding.',
       'A saved city contains 64 recipe anchors, the actual Forage mesh, three cameras and a native three-shot sequence.',
       'If the Forage sample is absent, the builder stops before making a map. Import it first. If a partial map exists after an error, preserve it and retry from a new Starter copy.',
       ['Forage supplies the hero asset','Kit supplies the city vocabulary','Native MCP performs the build','You direct the result'])

    lesson('03 · Forage and your kit','forage-owned','Bring your own Fab library into the city','Let Forage scout; choose what belongs in your scene.',[
        'Open Window → Forage → Open Dashboard to search assets already in this project. For the native Fab handoff, use the included companion’s fab-handoff command or connect its stdio MCP server to your assistant.',
        'Ask for a shortlist of owned packs for one specific replacement: a fountain, a tree family or a harbor prop. The beta companion command is: Forage.exe fab-handoff "stylized harbor fountain and market props" --limit 2 --editor-port 8000. Use your actual Unreal MCP port.',
        'Review the picks in your signed-in Fab library. Choose and install a compatible pack through Epic’s editor flow, then have the agent list its actual imported mesh paths before placing anything. Keep the original class kit when you do not own a suitable pack.'
    ],'Using Forage, shortlist up to two packs from my own signed-in Fab library for a stylized harbor fountain. Show the pack names, whether I own them, compatibility and the proposed download before any install. After I choose and install, inspect actual /Game mesh paths and propose a replacement in my city variation. Do not purchase, guess asset paths or redistribute another creator’s pack.',
       'You have a reviewed shortlist or an honest “no matching owned asset” result; any placed mesh has a verified project path.',
       'Library access needs your own Epic sign-in. A missing cache or unsupported library route is not proof you own a pack. Continue with the supplied kit and original practice mesh. The public beta does not expose every command from earlier member CLI builds.',
       ['Local project search','Owned-library shortlist','You choose the pack','Verify imported paths'],[('Forage beta and compatibility',FORAGE)])

    lesson('04 · Create with 5.9 AI','python-tools','Let the agent use editor Python','5.9 can discover APIs and run one useful script.',[
        'Ask your agent to find EditorToolset’s PythonScriptingTools and call its read_me tool once. It can use search_symbols and get_symbol to inspect the installed Python API.',
        'For a batch of edits, ask it to prepare one editor script instead of hundreds of single-actor calls. Through execute_python, imports belong at top level and the final expression is the returned result.',
        'Use the prompt below in your city variation. Inspect the returned labels and native geometry. The supplied HarborWorkshopTools already wraps our most common tasks, so beginners need not write a toolset themselves.'
    ],'In my current city variation only, inspect the available PythonScriptingTools schema and call read_me. Use one editor Python script to list all HK_MyMarket_ actors and return their names and locations as the final expression. Do not edit anything. Use symbol lookup if an API is uncertain; print output alone is not the tool’s return value.',
       'Actual actor names and coordinates return from the live editor, using a built-in 5.9 tool.',
       'If execute_python rejects a nested or star import, put imports at top level and use explicit module names. If the toolset is absent, enable All Toolsets and reconnect.',
       ['Discover the live API','One script for a batch','Return a real result'],[('Python with AI agents',PYTHON)])

    lesson('04 · Create with 5.9 AI','ecabridge','Your free ECABridge extension','Use it when you need its additional editor commands.',[
        'The class folder supplies an optional ECABridge download for Windows UE 5.9.0 CL60351404; leave it disabled for the required route. It is precompiled; keep its complete plugin folder. For another project, copy ECABridge into Plugins with the editor closed, then enable ECA Bridge and restart.',
        'If you install it, this project configures ECABridge at http://127.0.0.1:3001/mcp. Epic’s native Unreal MCP remains at port 8000. Add ECABridge as a separate HTTP MCP server in your client; keep both names and ports distinct.',
        'Begin with a read-only level query and inspect the returned project. Load the needed categories rather than assuming every command is listed initially. Use the bridge for an additional task only after its actual schema and result are visible.'
    ],'Read only: connect to ECABridge at http://127.0.0.1:3001/mcp. Discover its tools and current level, confirm PaperCity and UE 5.9, and explain one command that would help our scene. Keep native Unreal MCP at port 8000. Do not rebuild plugins or change the city.',
       'The client can distinguish native Unreal MCP from ECABridge and retrieve real scene information.',
       'A shutdown assertion was observed after a two-job MRQ run with this optional bridge enabled. Keep it disabled for the core class and rendering; native MCP and Actions cover the required route. A different engine changelist may need a different binary. Do not let a compiler prompt turn this class exercise into an engine build.',
       ['Free class copy','Win64 CL60351404','Native MCP :8000','ECABridge :3001'])

    lesson('04 · Create with 5.9 AI','canvas','Unreal Canvas: turn the scene into a creative brief','Optional service-dependent lab; preserve the native city.',[
        'Enable Unreal Canvas Bridge in Edit → Plugins if it is available in your build, restart, then open Tools → Unreal Canvas. Follow the build’s setup dialog and select a provider/model you already have access to. Review any download and service cost before starting.',
        'Open a city camera. In Canvas Toolbox, use Viewport Snapshot or Viewport Render to bring a reference view into the canvas. Select an Image tool that accepts a reference image. Add the capture and paste the prompt below. Generate one result, then compare it with the reference.',
        'Save the result as a separate concept image. This changes the image, not the city actors. To use a generated prop, select a compatible Mesh tool with a suitable prop image, inspect the output in its viewer, choose Import to Content Browser, then place that actual imported asset in your variation.'
    ],'Use this harbor-city view as the composition reference. Explore a rain-soaked evening with teal reflections, amber market awnings and one prominent clockwork fountain. Keep the canal layout and camera recognizable. Produce one concept image; do not claim the 3D level has changed.',
       'You have a separately labeled concept result and can explain whether you generated media or imported a real mesh.',
       'Provider/model availability varies. If no supported model is configured, keep the supplied native result and read the workflow. This optional generation route is documented, not a claim that every student account or cloud provider was tested.',
       ['Capture the real scene','Generate one concept','Compare','Import a mesh separately'],[('Canvas setup, tools and costs',CANVAS)])

    lesson('04 · Create with 5.9 AI','spatial-annotations','Point at what you want to change','Use a spatial note to give AI a concrete target.',[
        'In a Canvas-enabled project variation, open the 3D Annotation panel supplied by Unreal Canvas Spatial Annotations. Mark the market area or select an actor; add one short instruction describing the desired change.',
        'Send the viewport capture and its supported annotation data into Canvas. Use the relevant spatial modification tool, choose your configured model and generate one alternative. Compare the annotated region and the rest of the image.',
        'For a native edit, ask the connected editor agent to identify the named market actors and make the equivalent scene change in your variation. Re-render and compare. A generated preview and an actor edit are two different outputs you can use together.'
    ],'Use my marked market area as the target. In the concept, try red-and-cream awnings while keeping the canal and camera recognizable. Then propose the corresponding native material changes on the named HK_MyMarket_ actor family. Show the proposal before editing the native scene.',
       'The instruction identifies a place or actor and the comparison shows which result is media and which is native scene content.',
       'If annotations or the model are unavailable, select the target actors, capture the viewport and supply their labels with the prompt. Keep the same specific target and comparison workflow.',
       ['Mark one place','Describe one change','Compare generated media','Apply a native edit separately'],[('Canvas spatial annotations',CANVAS)])

    lesson('10 · Your MegaJam launchpad','jam-plan','Turn today’s scene into a jam game','Recommendation: enter small, finish playable and learn in public.',[
        'The Epic AI MegaJam runs November 12–15. Pick a tiny idea that fits the revealed theme. Our suggestion: Lantern Courier, a short harbor route with three deliveries, a timer and a clear win state. Adapt the mechanic to the theme instead of submitting only the class environment.',
        'Keep this class project as your reference. In a new game copy, ask the agent for one playable loop before adding art or more districts. Choose solo or a small team and assign gameplay, art and testing ownership.',
        'Use this schedule: Thursday, playable loop; Friday, first packaged playtest; Saturday, clarity and polish; Sunday, final test, capture and upload with time to spare. Carry forward your Forage workflow, kit vocabulary, MCP tools and saved project memory.'
    ],'Help me turn my own class variation into a tiny Epic AI MegaJam game. First ask me for the revealed theme and my available time. Propose three one-sentence mechanics using the kit, then help me choose one. Plan one level, one core interaction, a clear win/lose condition, a packaged playtest and a 30–60 second gameplay capture. Treat the class kit as supplied/pre-existing material to declare. Do not register, submit, purchase or publish for me.',
       'You leave with a specific game idea, a first playable milestone and a realistic build schedule.',
       'If you only have a cinematic or pretty scene, add the player’s action and goal before expanding the environment. Keep a small downloadable target; experimental web packaging can be its own later experiment.',
       ['Class scene → playable loop','One mechanic • one level','Package early','Playtest • polish • submit'],[('Epic announcement','https://www.unrealengine.com/news/2026-epic-ai-megajam'),('Join and current details','https://itch.io/jam/2026-epic-ai-megajam')])

    lesson('10 · Your MegaJam launchpad','jam-checklist','Leave class ready to enter','Your next step is a playable milestone, not another tool install.',[
        'Open the organizer’s jam page, read its linked Official Rules and join if you are eligible. Its summary says 18+ with an active Epic account; teams may have up to five humans. The Student category requires current higher-education enrollment, not just this masterclass.',
        'Submission closes Sunday November 15 at 8:59 p.m. Eastern / 5:59 p.m. Pacific. Prepare a packaged playable game, a 30–60 second gameplay video and the requested team details. Declare earlier prompts, scripts and assets, including this supplied class kit.',
        'Before leaving: write your one-sentence game, first milestone and next work session in Studio/jam-brief.md. Share an idea with a potential teammate if you want. Your assistant can help draft a dev log; you choose what to share.'
    ],'Create Studio/jam-brief.md from my chosen idea and the official jam page. Include the theme, player goal, controls, one-level scope, original gameplay to build, supplied asset/tool disclosures, owners, next work session, packaging target, playtest checklist, video plan and my upload deadline with a buffer. Mark eligibility and rule checks as my decisions. End with exactly one next action.',
       'You have a bounded competition plan and know what must become playable before submission.',
       'A workshop attendance certificate is not student-category eligibility. Confirm the full rules and current organizer updates yourself; do not assume class files or a source-project ZIP are a finished game entry.',
       ['Join if eligible','Build custom gameplay','Declare supplied assets','Gameplay video + packaged build','Sun Nov 15 • 8:59 p.m. ET'],[('Registration, deadlines and checklist','https://itch.io/jam/2026-epic-ai-megajam'),('Official Rules','https://epicgames.box.com/s/a7xcgl07fqoieeb99sjtd3juhj4agc4z')])


def order_lessons(lessons):
    early=['start','accounts','open-folder','open-unreal','second-brain','ai59','native-connect','first-win',
           'forage-install','forage-import','kit-gallery','harbor-build','forage-owned',
           'python-tools','ecabridge','canvas','spatial-annotations']
    by_id={x['id']:x for x in lessons}
    ending=['jam-plan','jam-checklist']
    ordered=[by_id[i] for i in early]+[x for x in lessons if x['id'] not in early+ending]+[by_id[i] for i in ending]
    for l in ordered:
        if l['id'] in ['contract','python-check']:l['group']='05 · Build the world'
    labels={}
    for l in ordered:
        group=l['group'].split(' · ',1)[1]
        if group not in labels:labels[group]=str(len(labels)+1).zfill(2)+' · '+group
        l['group']=labels[group]
    return ordered
