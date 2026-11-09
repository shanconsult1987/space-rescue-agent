import unittest

from app import missions


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
        self.assertEqual(len(result), 2)
        self.assertTrue(
            all(item["status"] == "active" for item in result)
        )

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