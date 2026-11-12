# AI routes in Unreal 5.9 Preview

The main route uses Unreal Assistant with your own signed-in Codex or Claude Code agent. Enable Unreal Assistant, Unreal MCP and All Toolsets. The panel manages its local editor connection. Follow the workbook's exact adapter and External Agent setup steps.

For a separate client, use Editor Preferences → Agentic Workflows → Model Context Protocol → select your client → Generate Client Config. Start your agent from that config's folder. Native default: http://127.0.0.1:8000/mcp . Four discovery meta-tools can represent many toolsets; ask for HarborWorkshopTools rather than assuming four means only four capabilities.

The original Harbor Workshop AI Tools plugin exposes list_parts, build_harbor_city, build_kit_gallery, duplicate_city, add_part, verify_city and save_current_scene using 5.9's built-in Toolset Registry. The source is included; no C++ build is needed.

ECABridge is a separate, optional free class download, precompiled for Windows CL60351404. The class project uses http://127.0.0.1:3001/mcp . Keep both server names/ports distinct. The core project leaves ECABridge disabled. One post-MRQ shutdown assertion was observed with it enabled; native Epic tools cover this class without it. Request only the categories you need and inspect real tool results, including errors in returned output.

Forage's included beta companion can also expose its tools over stdio: run the absolute project Plugins/ForageBeta/Tools/Win64/Forage.exe path with argument mcp. Configure your client's stdio server with that executable and args ["mcp"]. Do not put account secrets in a shared config.

Fallback: the numbered Actions run inside Unreal Editor. A local assistant can prepare files without a direct editor connection. Installed files alone do not prove a live connection.
