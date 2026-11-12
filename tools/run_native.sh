#!/usr/bin/env bash
# Maintainer entrypoint. Paths are explicit; the host lease owns admission.
set -euo pipefail
: "${CLASS_SOURCE:?Absolute source checkout required}"
: "${CLASS_ENGINE:?Absolute engine directory required}"
: "${CLASS_OUTPUT:?Absolute output directory required}"
: "${CLASS_LEASE:?Host build-lane lease script required}"
: "${CLASS_OWNER:?Owner chat ID required}"
mkdir -p "$CLASS_OUTPUT/temp" "$CLASS_OUTPUT/user" "$CLASS_OUTPUT/ddc" "$CLASS_OUTPUT/evidence" "$CLASS_OUTPUT/logs"
export TEMP="$CLASS_OUTPUT/temp" TMP="$CLASS_OUTPUT/temp"
export LOCALAPPDATA="$CLASS_OUTPUT/user/AppData/Local"
export PYTHONDONTWRITEBYTECODE=1
export UE_LOCAL_ROOT="$CLASS_OUTPUT/ddc"
export SMALL_WORLDS_EVIDENCE="$CLASS_OUTPUT/evidence"
env "UE-LocalDataCachePath=$CLASS_OUTPUT/ddc" bash "$CLASS_LEASE" run \
  --owner-session "$CLASS_OWNER" \
  --owner-task "AI Masterclass Part 2 native rehearsal" \
  --project "$CLASS_SOURCE/workshop/Unreal" \
  --engine "$CLASS_ENGINE" \
  --purpose "Rehearse original classroom maps, kit and cinematics" \
  --disk-path "$CLASS_OUTPUT" --reserve-gib "${CLASS_RESERVE_GIB:-4}" \
  -- "$CLASS_ENGINE/Engine/Binaries/Win64/UnrealEditor-Cmd.exe" \
  "$CLASS_SOURCE/workshop/Unreal/PaperCity.uproject" \
  -unattended -nosplash -RenderOffscreen -NoSound -NoLiveCoding \
  "-UserDir=$CLASS_OUTPUT/user" "-abslog=$CLASS_OUTPUT/logs/native-rehearsal.log" \
  "-ExecutePythonScript=${CLASS_SCRIPT:-$CLASS_SOURCE/tools/rehearse_native.py}" \
  -stdout -FullStdOutLogOutput
