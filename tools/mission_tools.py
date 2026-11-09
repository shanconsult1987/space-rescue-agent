"""Tools that expose mission operations to agent workflows."""

from app.missions import (
    get_active_missions,
    get_mission,
    get_missions,
)


def get_mission_status(mission_id):
    mission = get_mission(int(mission_id))

    if mission is None:
        return {
            "found": False,
            "mission_id": mission_id,
        }

    return {
        "found": True,
        "mission": mission,
    }


def list_all_missions():
    return get_missions()


def get_high_priority_missions():
    return [
        mission
        for mission in get_active_missions()
        if mission["priority"] == "high"
    ]