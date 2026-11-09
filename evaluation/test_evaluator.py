import unittest

from agents.evaluator import (
    check_active_endpoint,
    check_active_filter,
    check_active_function,
    run_unit_tests,
)


class EvaluatorTests(unittest.TestCase):

    def test_active_function_exists(self):
        self.assertTrue(check_active_function()["passed"])

    def test_active_filter_exists(self):
        self.assertTrue(check_active_filter()["passed"])

    def test_active_endpoint_exists(self):
        self.assertTrue(check_active_endpoint()["passed"])

    def test_unit_tests_pass(self):
        self.assertTrue(run_unit_tests()["passed"])


if __name__ == "__main__":
    unittest.main()