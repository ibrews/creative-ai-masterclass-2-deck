# Harbor of a Thousand Lanterns

Your shared kit contains twelve original recipes in Studio/harbor-kit.json. The 64-placement reference composition is Studio/harbor-city.json. Units are centimeters, yaw is degrees. Local X is each part's forward axis; the footbridge runs along local X.

In Starter, use Forage's Guided Tutorial to import the three original practice assets, then ask the native build_harbor_city tool to build once, or run Actions/06_build_city.py inside Unreal Editor. Open 05_HarborCity and LS_HarborCity. Run Actions/07_build_gallery.py to make the separate 06_KitGallery.

In Finished, those maps and the Forage sample are already present. Use duplicate_city with a new unused map name before remixing. The kit is composed from native actor families and editable JSON recipes, not a commercial city pack. To direct a new city, give the agent part IDs, placement counts, spacing, a focal point and camera views. Change one region and compare.

Suggested first prompt: duplicate_city("07_MyHarbor"), then add three market_stall parts at (-600,-2050,0), (0,-2050,0), (600,-2050,0), all yaw 0, named HK_MyMarket_1 through 3. Inspect, then save_current_scene.

The central monument must reference /Game/ForageBetaSample/SM_ForageToken, with its bound material/texture. Do not silently replace it with a primitive and call the Forage import complete.
