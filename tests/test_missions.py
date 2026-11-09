import unittest
from unittest.mock import patch

from app import missions
from app.server import MissionHandler


class MissionTests(unittest.TestCase):

    def setUp(self):
        self.original = [dict(item) for item in missions.MISSIONS]

    def tearDown(self):
        missions.MISSIONS.clear()
        missions.MISSIONS.extend(self.original)

    def test_get_missions_returns_all(self):
        self.assertEqual(len(missions.get_missions()), 3)

    def test_get_mission_existing(self):
        result = missions.get_mission(1)
        self.assertEqual(result["name"], "Mars Habitat Deployment")

    def test_get_mission_missing(self):
        self.assertIsNone(missions.get_mission(999))

    def test_active_missions_excludes_completed(self):
        result = missions.get_active_missions()
        self.assertEqual([item["id"] for item in result], [1, 2])
        self.assertTrue(all(item["status"] == "active" for item in result))

    def test_completed_missions_returns_only_active(self):
        result = missions.get_completed_missions()
        self.assertEqual([item["id"] for item in result], [1, 2])
        self.assertTrue(all(item["status"] == "active" for item in result))

    def test_get_active_missions_endpoint(self):
        handler = MissionHandler.__new__(MissionHandler)
        handler.path = "/missions/active"

        with patch.object(handler, "send_json") as send_json:
            handler.do_GET()

        send_json.assert_called_once_with(200, missions.get_active_missions())

    def test_get_completed_missions_endpoint(self):
        handler = MissionHandler.__new__(MissionHandler)
        handler.path = "/missions/completed"

        with patch.object(handler, "send_json") as send_json:
            handler.do_GET()

        send_json.assert_called_once_with(200, missions.get_completed_missions())

    def test_create_mission(self):
        result = missions.create_mission("Water Recovery", "high")
        self.assertEqual(result["name"], "Water Recovery")
        self.assertEqual(result["status"], "active")

    def test_create_mission_rejects_empty_name(self):
        with self.assertRaises(ValueError):
            missions.create_mission("")

    def test_create_mission_rejects_invalid_priority(self):
        with self.assertRaises(ValueError):
            missions.create_mission("Test", "urgent")

    def test_delete_mission(self):
        result = missions.delete_mission(1)
        self.assertEqual(result["id"], 1)
        self.assertIsNone(missions.get_mission(1))


if __name__ == "__main__":
    unittest.main()