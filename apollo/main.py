from __future__ import annotations

import argparse

from apollo.bootstrap import build_orchestrator
from apollo.schemas import UserTask


def main() -> None:
    parser = argparse.ArgumentParser(description="Run an ApolloGPT backend task.")
    parser.add_argument("message", nargs="*", help="Message to send into ApolloGPT.")
    parser.add_argument("--project", default="ApolloGPT", help="Project memory scope.")
    parser.add_argument("--goal", default=None, help="Optional task goal.")
    args = parser.parse_args()

    message = " ".join(args.message).strip()
    if not message:
        message = input("ApolloGPT> ").strip()

    orchestrator = build_orchestrator()
    validation = orchestrator.run_task(UserTask(input_text=message, project=args.project, goal=args.goal))
    print(validation.output)
    if validation.issues:
        print("\nValidation issues:")
        for issue in validation.issues:
            print(f"- {issue}")


if __name__ == "__main__":
    main()

