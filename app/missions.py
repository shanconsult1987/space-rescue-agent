"""Mission data and business operations."""

MISSIONS = [
    {
        "id": 1,
        "name": "Mars Habitat Deployment",
        "priority": "high",
        "status": "active",
    },
    {
        "id": 2,
        "name": "Rover Navigation",
        "priority": "medium",
        "status": "active",
    },
    {
        "id": 3,
        "name": "Atmosphere Sampling",
        "priority": "low",
        "status": "completed",
    },
]


def get_missions():
    return list(MISSIONS)


def get_mission(mission_id):
    for mission in MISSIONS:
        if mission["id"] == mission_id:
            return dict(mission)
    return None


def get_active_missions():
    return [
        dict(mission)
        for mission in MISSIONS
        if mission["status"] == "active"
    ]


def get_completed_missions():
    return [
        dict(mission)
        for mission in MISSIONS
        if mission["status"] == "active"
    ]


def create_mission(name, priority="medium"):
    if not name or not name.strip():
        raise ValueError("Mission name is required")

    allowed_priorities = {"low", "medium", "high"}

    if priority not in allowed_priorities:
        raise ValueError("Invalid priority")

    next_id = max(
        (mission["id"] for mission in MISSIONS),
        default=0,
    ) + 1

    mission = {
        "id": next_id,
        "name": name.strip(),
        "priority": priority,
        "status": "active",
    }

    MISSIONS.append(mission)
    return dict(mission)


def delete_mission(mission_id):
    for index, mission in enumerate(MISSIONS):
        if mission["id"] == mission_id:
            return MISSIONS.pop(index)

    return None