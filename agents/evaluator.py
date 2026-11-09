"""Deterministic evaluation of SpaceRescue implementation."""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def check_active_function():
    source = (ROOT / "app" / "missions.py").read_text(
        encoding="utf-8"
    )

    passed = "def get_active_missions(" in source

    return {
        "check": "active_function_exists",
        "passed": passed,
        "evidence": "Found get_active_missions definition."
        if passed
        else "Function definition not found.",
    }


def check_active_filter():
    source = (ROOT / "app" / "missions.py").read_text(
        encoding="utf-8"
    )

    passed = (
        "def get_active_missions(" in source
        and 'mission["status"] == "active"' in source
    )

    return {
        "check": "active_filter",
        "passed": passed,
        "evidence": (
            "Active status filter found in source."
            if passed
            else "Expected active status filter not found."
        ),
    }


def check_active_endpoint():
    source = (ROOT / "app" / "server.py").read_text(
        encoding="utf-8"
    )

    passed = 'path == "/missions/active"' in source

    return {
        "check": "active_endpoint",
        "passed": passed,
        "evidence": (
            "Active endpoint route found."
            if passed
            else "Active endpoint route not found."
        ),
    }


def run_unit_tests():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "unittest",
            "discover",
            "-s",
            "tests",
            "-v",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    return {
        "check": "unit_tests",
        "passed": result.returncode == 0,
        "evidence": result.stdout + result.stderr,
    }


def evaluate():
    checks = [
        check_active_function(),
        check_active_filter(),
        check_active_endpoint(),
        run_unit_tests(),
    ]

    passed = sum(1 for item in checks if item["passed"])
    total = len(checks)

    return {
        "passed": passed,
        "total": total,
        "score": round((passed / total) * 100, 2),
        "success": passed == total,
        "checks": checks,
    }