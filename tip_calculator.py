"""US-style tip calculator CLI tool.

Popular in the US because tipping is widely expected in restaurants.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass

SERVICE_TIP_RATES = {
    "standard": 15.0,
    "good": 18.0,
    "great": 20.0,
}


@dataclass(frozen=True)
class TipBreakdown:
    bill: float
    tip_percent: float
    tip_amount: float
    total: float
    people: int
    per_person: float


def compute_tip(bill: float, tip_percent: float, people: int = 1) -> TipBreakdown:
    """Compute tip totals for a bill."""
    if bill < 0:
        raise ValueError("Bill amount cannot be negative.")
    if tip_percent < 0:
        raise ValueError("Tip percent cannot be negative.")
    if people < 1:
        raise ValueError("People must be at least 1.")

    tip_amount = round(bill * (tip_percent / 100.0), 2)
    total = round(bill + tip_amount, 2)
    per_person = round(total / people, 2)

    return TipBreakdown(
        bill=round(bill, 2),
        tip_percent=round(tip_percent, 2),
        tip_amount=tip_amount,
        total=total,
        people=people,
        per_person=per_person,
    )


def render_breakdown(breakdown: TipBreakdown) -> str:
    return "\n".join(
        [
            f"Bill: ${breakdown.bill:.2f}",
            f"Tip ({breakdown.tip_percent:.1f}%): ${breakdown.tip_amount:.2f}",
            f"Total: ${breakdown.total:.2f}",
            f"Per person ({breakdown.people}): ${breakdown.per_person:.2f}",
        ]
    )


def run_live_demo() -> None:
    """Show a quick terminal demo with common US tipping scenarios."""
    scenarios = [
        ("Solo diner (standard)", 42.50, SERVICE_TIP_RATES["standard"], 1),
        ("Date night (good)", 86.40, SERVICE_TIP_RATES["good"], 2),
        ("Group dinner (great)", 175.90, SERVICE_TIP_RATES["great"], 5),
    ]

    print("LIVE DEMO: US Tip Calculator")
    print("=" * 30)
    for title, bill, tip_percent, people in scenarios:
        print(f"\n{title}")
        print("-" * len(title))
        print(render_breakdown(compute_tip(bill, tip_percent, people)))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="US-style tip calculator")
    parser.add_argument("--bill", type=float, help="Base bill amount")
    parser.add_argument(
        "--service",
        choices=SERVICE_TIP_RATES.keys(),
        default="standard",
        help="Service quality preset tip rate",
    )
    parser.add_argument(
        "--tip",
        type=float,
        default=None,
        help="Custom tip percentage (overrides --service)",
    )
    parser.add_argument("--people", type=int, default=1, help="Number of people splitting")
    parser.add_argument(
        "--live-demo",
        action="store_true",
        help="Run a quick multi-scenario demo in the terminal",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.live_demo:
        run_live_demo()
        return

    if args.bill is None:
        raise SystemExit("error: --bill is required unless --live-demo is used")

    tip_percent = args.tip if args.tip is not None else SERVICE_TIP_RATES[args.service]
    breakdown = compute_tip(args.bill, tip_percent, args.people)
    print(render_breakdown(breakdown))


if __name__ == "__main__":
    main()
