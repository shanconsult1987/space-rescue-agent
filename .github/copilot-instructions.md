# SpaceRescue Repository Instructions

You are working on a small Python application for managing Mars missions.

## Project rules

- Use Python standard library wherever practical.
- Do not introduce FastAPI, Flask, Django, Uvicorn or Gunicorn.
- Keep the repository simple and easy to teach.
- Preserve the existing application behavior.
- Do not introduce Azure OpenAI.
- Do not hardcode API keys or secrets.
- Use PowerShell-compatible commands in documentation.

## Development rules

- Read the relevant source files before making changes.
- Make the smallest change that satisfies the issue.
- Add or update unittest tests for behavior changes.
- Run the complete test suite after code changes.
- Do not claim tests passed unless they were executed.
- Do not delete tests to make a build pass.

## Agent behavior

- Planner: produce a plan, do not edit files.
- Developer: implement only the approved task.
- Reviewer: inspect changes and report findings.
- Evaluator: run objective checks and report evidence.

## Safety

- Never expose credentials.
- Do not execute destructive commands without approval.
- Do not merge pull requests automatically.
- Ask for human approval when requirements are unclear.