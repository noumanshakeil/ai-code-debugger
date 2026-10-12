"""CLI for ai-code-debugger."""
from __future__ import annotations

import argparse

from .agent import dump_trace, run_agent

def main() -> None:
    p = argparse.ArgumentParser(description="Agent that explains stack traces, proposes patches, and runs a sandboxed Python snippet check.")
    p.add_argument("question", nargs="?", default="Calculate 12*(3+4)")
    p.add_argument("--trace", action="store_true")
    args = p.parse_args()
    result = run_agent(args.question)
    print(result.answer)
    if args.trace:
        print(dump_trace(result))

if __name__ == "__main__":
    main()
