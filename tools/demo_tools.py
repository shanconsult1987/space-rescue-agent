"""Run a local demonstration of SpaceRescue tools."""

from tools.mission_tools import (
    get_high_priority_missions,
    get_mission_status,
    list_all_missions,
)


def main():
    print("\n1. All missions")
    print(list_all_missions())

    print("\n2. Mission 1 status")
    print(get_mission_status(1))

    print("\n3. High-priority active missions")
    print(get_high_priority_missions())


if __name__ == "__main__":
    main()