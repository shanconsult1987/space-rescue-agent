---
description: Testing rules for Python test files.
applyTo: "tests/**/*.py"
---

# Testing instructions

- Use unittest.
- Use descriptive test names.
- Test normal behavior and invalid input.
- Keep tests independent.
- Restore modified global state in tearDown.
- Do not use network access in unit tests.
- Do not rely on execution order.
- Do not remove a test because it exposes a defect.