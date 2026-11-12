"""Original workshop tools using Unreal 5.9's built-in Toolset Registry."""
import json
from pathlib import Path
import unreal
import toolset_registry
from toolset_registry.registration import Registration


@unreal.uclass()
class HarborWorkshopTools(unreal.ToolsetDefinition):
    """Build and remix the original Harbor City classroom kit. Inspect parts first.
    New-map builders refuse existing outputs; use a fresh Starter for a rerun."""

    @toolset_registry.tool_call(mode=unreal.ToolAccessMode.READ)
    @staticmethod
    def list_parts() -> str:
        """List exact kit IDs, dimensions and material components for scene composition."""
        import harbor_kit
        return harbor_kit.CATALOG.read_text()

    @toolset_registry.tool_call(mode=unreal.ToolAccessMode.WRITE)
    @staticmethod
    def build_harbor_city() -> str:
        """Build the supplied 64-placement Harbor City in a new 05_HarborCity map.
        Import the original Forage practice sample first. Preserve existing maps."""
        import harbor_kit
        return json.dumps(harbor_kit.build_city())

    @toolset_registry.tool_call(mode=unreal.ToolAccessMode.WRITE)
    @staticmethod
    def build_kit_gallery() -> str:
        """Create a new 06_KitGallery map displaying all twelve reusable recipes."""
        import harbor_kit
        return json.dumps(harbor_kit.build_gallery())

    @toolset_registry.tool_call(mode=unreal.ToolAccessMode.WRITE)
    @staticmethod
    def add_part(part_id: str, x: float, y: float, z: float, yaw: float, name: str) -> str:
        """Add one catalog part in the current map, using centimeters and yaw degrees.
        Args:
            part_id: Exact ID from list_parts.
            x: World X in centimeters.
            y: World Y in centimeters.
            z: Base world Z in centimeters.
            yaw: Rotation around Z in degrees.
            name: Unique HK_ actor anchor label; never reuse an existing name.
        Returns:
            JSON containing the labels of all created actors.
        """
        import harbor_kit
        actors = unreal.get_editor_subsystem(unreal.EditorActorSubsystem).get_all_level_actors()
        if not name.startswith('HK_') or any(a.get_actor_label() == name for a in actors):
            raise ValueError('Use a unique HK_ name.')
        return json.dumps([a.get_actor_label() for a in harbor_kit.spawn_part(part_id, x, y, z, yaw, name)])

    @toolset_registry.tool_call(mode=unreal.ToolAccessMode.WRITE)
    @staticmethod
    def duplicate_city(variant_name: str) -> str:
        """Copy the supplied city into a new map and open it before remixing.
        Args:
            variant_name: New map name using only letters, digits and underscores.
        Returns:
            The path of the new map. Existing maps are protected.
        """
        import harbor_kit
        if not variant_name.replace('_', '').isalnum():
            raise ValueError('Use letters, digits and underscores only.')
        path = '/Game/SmallWorlds/Maps/' + variant_name
        if unreal.EditorAssetLibrary.does_asset_exist(path):
            raise ValueError('Map already exists: ' + path)
        copied = unreal.EditorAssetLibrary.duplicate_asset('/Game/SmallWorlds/Maps/05_HarborCity', path)
        if not copied:
            raise RuntimeError('Could not duplicate city')
        unreal.EditorAssetLibrary.save_asset(path)
        unreal.get_editor_subsystem(unreal.LevelEditorSubsystem).load_level(path)
        return path

    @toolset_registry.tool_call(mode=unreal.ToolAccessMode.WRITE)
    @staticmethod
    def save_current_scene() -> str:
        """Save the current map and dirty content after the learner reviews a remix."""
        unreal.get_editor_subsystem(unreal.LevelEditorSubsystem).save_current_level()
        unreal.EditorLoadingAndSavingUtils.save_dirty_packages(True, True)
        return unreal.EditorLevelLibrary.get_editor_world().get_path_name()

    @toolset_registry.tool_call(mode=unreal.ToolAccessMode.READ)
    @staticmethod
    def verify_city() -> str:
        """Check all recipe anchors, three cameras and the actual Forage mesh in the current Harbor City."""
        import harbor_kit
        return json.dumps(harbor_kit.verify_city())


_registration = Registration([HarborWorkshopTools])
