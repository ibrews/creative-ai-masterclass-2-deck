"""Write the expanded classroom support notes alongside the original foundations."""

def write_addition_support(root):
    w=root/'workshop'
    notes={
    'Recipes/03-ai-connections.md':'''# AI routes in Unreal 5.9 Preview

The main route uses Unreal Assistant with your own signed-in Codex or Claude Code agent. Enable Unreal Assistant, Unreal MCP and All Toolsets. The panel manages its local editor connection. Follow the workbook's exact adapter and External Agent setup steps.

For a separate client, use Editor Preferences → Agentic Workflows → Model Context Protocol → select your client → Generate Client Config. Start your agent from that config's folder. Native default: http://127.0.0.1:8000/mcp . Four discovery meta-tools can represent many toolsets; ask for HarborWorkshopTools rather than assuming four means only four capabilities.

The original Harbor Workshop AI Tools plugin exposes list_parts, build_harbor_city, build_kit_gallery, duplicate_city, add_part, verify_city and save_current_scene using 5.9's built-in Toolset Registry. The source is included; no C++ build is needed.

ECABridge is a separate, optional free class download, precompiled for Windows CL60351404. The class project uses http://127.0.0.1:3001/mcp . Keep both server names/ports distinct. The core project leaves ECABridge disabled. One post-MRQ shutdown assertion was observed with it enabled; native Epic tools cover this class without it. Request only the categories you need and inspect real tool results, including errors in returned output.

Forage's included beta companion can also expose its tools over stdio: run the absolute project Plugins/ForageBeta/Tools/Win64/Forage.exe path with argument mcp. Configure your client's stdio server with that executable and args ["mcp"]. Do not put account secrets in a shared config.

Fallback: the numbered Actions run inside Unreal Editor. A local assistant can prepare files without a direct editor connection. Installed files alone do not prove a live connection.
''',
    'Recipes/06-harbor-city.md':'''# Harbor of a Thousand Lanterns

Your shared kit contains twelve original recipes in Studio/harbor-kit.json. The 64-placement reference composition is Studio/harbor-city.json. Units are centimeters, yaw is degrees. Local X is each part's forward axis; the footbridge runs along local X.

In Starter, use Forage's Guided Tutorial to import the three original practice assets, then ask the native build_harbor_city tool to build once, or run Actions/06_build_city.py inside Unreal Editor. Open 05_HarborCity and LS_HarborCity. Run Actions/07_build_gallery.py to make the separate 06_KitGallery.

In Finished, those maps and the Forage sample are already present. Use duplicate_city with a new unused map name before remixing. The kit is composed from native actor families and editable JSON recipes, not a commercial city pack. To direct a new city, give the agent part IDs, placement counts, spacing, a focal point and camera views. Change one region and compare.

Suggested first prompt: duplicate_city("07_MyHarbor"), then add three market_stall parts at (-600,-2050,0), (0,-2050,0), (600,-2050,0), all yaw 0, named HK_MyMarket_1 through 3. Inspect, then save_current_scene.

The central monument must reference /Game/ForageBetaSample/SM_ForageToken, with its bound material/texture. Do not silently replace it with a primitive and call the Forage import complete.
''',
    'Recipes/07-forage.md':'''# Free Forage classroom copy

The updated class package supplies ForageBeta under Unreal/Plugins. For an existing project, extract the separate Forage ZIP and copy its complete ForageBeta folder to that project's Plugins directory. Enable Forage Beta and restart. The Windows beta was published as 0.1.2b1 for 5.8.4 and 5.9 Preview; this class targets Windows 5.9 CL60351404.

Window → Forage → Guided Tutorial stages one original mesh with its material and texture. The second confirmation adds the three files to Content/ForageBetaSample. No Fab login is required for that practice exercise. In 5.9, browse directly to the folder if selection is empty. Finished already contains the imported sample; Starter excludes it so you can see the actual import.

Window → Forage → Open Dashboard searches this project's assets. For owned-library picks, the included companion supports:

```text
Forage.exe fab-handoff "stylized harbor fountain and market props" --limit 2 --editor-port 8000
```

Use the real executable path and editor port. Review picks using your own signed-in Fab library and let Epic handle the chosen compatible install. Inventory actual imported meshes before placing them. The public beta has a smaller command set than older member CLI builds; do not assume refresh-library or query exists in this executable. A no-match result is a valid outcome; our original kit remains usable by everyone.

Lab page, current download, tutorial and feedback: https://www.alexcoulombepresents.com/lab/forage . The class folder supplies free copies for attendees; no paid membership is needed for the shared exercise.
''',
    'Recipes/08-ai-59-and-canvas.md':'''# 5.9 AI features and optional Canvas lab

Primary references checked November 11–12, 2026:

- Release notes: https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-9-release-notes?lang=en-US
- Native MCP: https://dev.epicgames.com/documentation/unreal-engine/unreal-mcp-in-unreal-editor
- External agents in Unreal Assistant: https://dev.epicgames.com/documentation/unreal-engine/run-external-ai-agents-in-the-unreal-assistant-panel-in-unreal-engine
- Editor Python tools: https://dev.epicgames.com/documentation/unreal-engine/using-python-with-ai-agents-in-unreal-engine
- Canvas: https://dev.epicgames.com/documentation/unreal-engine/unreal-canvas-overview-in-unreal-engine

The required city route uses native MCP, original recipes, Forage's original practice selection and your existing assistant account. Optional Unreal Canvas has its own installation, model/provider and service requirements. Enable Unreal Canvas Bridge only when you want that lab; review optional component downloads before installing them.

Open Tools → Unreal Canvas. Capture the native city through Viewport Snapshot or Viewport Render. Use an Image model with a reference image to explore one new mood, then compare. This produces a concept image. Use a compatible Mesh model to create a prop, inspect it, import it to Content Browser, and place the actual imported mesh as a separate operation. A generated image is not a changed 3D level.

Spatial annotations let you mark a target in the 3D scene and carry prompts/captures into Canvas. Try one market-awning change; preserve the original take. Provider-dependent generation and the external-agent panel UI are guided workflows, not a promise that every account or platform was exercised in the native rehearsal. The release evidence states precisely what was run.
'''
    }
    for rel,text in notes.items():(w/rel).write_text(text)
