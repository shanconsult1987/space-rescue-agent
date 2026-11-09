# SpaceRescue Functional Specification

## Purpose

SpaceRescue manages missions for a Mars exploration program.

## Mission fields

- id: unique integer
- name: non-empty string
- priority: low, medium or high
- status: active or completed

## Current endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | /missions | List all missions |
| GET | /missions/active | List active missions |
| GET | /missions/{id} | Retrieve one mission |
| POST | /missions | Create a mission |
| DELETE | /missions/{id} | Delete a mission |

## Business rules

1. Mission names cannot be empty.
2. Priority must be low, medium or high.
3. New missions are active.
4. Mission IDs must be unique.
5. Completed missions must not appear in the active list.

## Quality requirements

- Use standard-library Python for the core application.
- Provide unit tests for business behavior.
- Return JSON from HTTP endpoints.
- Return useful HTTP error codes.
- Keep the code suitable for a beginner workshop.