"""Command-line interface for running the PB2S agentic suit."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from attention_loop import AttentionLoop
from instruction_agentic_code_suit_Architecture import AgenticSuit
from ledger import SafetyLedger

DEFAULT_LEDGER_PATH = Path(".pb2s/ledger.jsonl")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run PB2S agentic suit")
    parser.add_argument("signal", nargs="?", help="Signal content to process")
    parser.add_argument(
        "--signal-file",
        type=Path,
        help="Path to a file containing the signal to process",
    )
    parser.add_argument(
        "--label",
        default="signal",
        help="Label to associate with the processed signal",
    )
    parser.add_argument(
        "--no-ledger",
        action="store_true",
        help="Disable ledger persistence",
    )
    parser.add_argument(
        "--ledger-path",
        type=Path,
        default=DEFAULT_LEDGER_PATH,
        help="Path to the ledger JSONL file (default: %(default)s)",
    )
    parser.add_argument(
        "--maintenance",
        action="store_true",
        help="Trigger maintenance check instead of processing a signal",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    ledger = None if args.no_ledger else SafetyLedger(args.ledger_path)
    loop = AttentionLoop(suit=AgenticSuit(), ledger=ledger)

    if args.maintenance:
        result = loop.maintenance_if_due(reason="cli")
        print(json.dumps(result or {"status": "no-maintenance"}, ensure_ascii=False))
        return 0

    signal = args.signal
    if args.signal_file:
        signal = args.signal_file.read_text(encoding="utf-8")
    if signal is None:
        signal = sys.stdin.read()
    payload = loop.process_signal(signal, label=args.label)
    print(json.dumps(payload, ensure_ascii=False))
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
