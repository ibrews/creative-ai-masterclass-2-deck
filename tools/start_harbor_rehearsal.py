"""Keep the editor alive for actual native MCP scene construction."""
import json
from pathlib import Path
import os
import unreal as ue
import harbor_tools
ue.EditorPythonScripting.set_keep_python_script_alive(True)
ue.log('HARBOR_ROTATOR_PROBE '+str(ue.Rotator(11,22,33))+' keyword '+str(ue.Rotator(pitch=11,yaw=22,roll=33)))
ue.log('HARBOR_MCP_READY')
(Path(os.environ['SMALL_WORLDS_EVIDENCE'])/'harbor-ready.json').write_text(json.dumps({'engine':ue.SystemLibrary.get_engine_version(),'ready':True}))
