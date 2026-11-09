"""Small GitHub CLI wrapper for workshop demonstrations."""

import json
import subprocess


def run_gh(arguments):
    result = subprocess.run(
        ["gh", *arguments],
        capture_output=True,
        text=True,
        check=False,
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())

    return result.stdout


def get_issue(issue_number):
    output = run_gh([
        "issue",
        "view",
        str(issue_number),
        "--json",
        "number,title,body,state,url",
    ])

    return json.loads(output)


def list_open_issues():
    output = run_gh([
        "issue",
        "list",
        "--state",
        "open",
        "--json",
        "number,title,url",
    ])

    return json.loads(output)


def comment_on_issue(issue_number, message):
    return run_gh([
        "issue",
        "comment",
        str(issue_number),
        "--body",
        message,
    ])


if __name__ == "__main__":
    print(json.dumps(list_open_issues(), indent=2))