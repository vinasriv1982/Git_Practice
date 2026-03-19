#!/usr/bin/env python3
"""
Simple calculator CLI.

Run:
  python lab02.py
"""

print("github test")

from __future__ import annotations


def parse_number(text: str) -> float:
    """Parse a user-provided number string into a float."""
    text = text.strip()
    try:
        return float(text)
    except ValueError as exc:
        raise ValueError(f"Invalid number: {text!r}") from exc


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def compute(a: float, op: str, b: float) -> float:
    op = op.strip()
    if op == "+":
        return add(a, b)
    if op == "-":
        return subtract(a, b)
    if op == "*":
        return multiply(a, b)
    if op == "/":
        return divide(a, b)
    raise ValueError(f"Unsupported operator: {op!r}")


def prompt_number(label: str) -> float:
    while True:
        raw = input(f"{label} (number): ").strip()
        try:
            return parse_number(raw)
        except ValueError as e:
            print(e)


def prompt_operator() -> str:
    valid = {"+", "-", "*", "/"}
    while True:
        raw = input("Operator (+, -, *, /) or 'q' to quit: ").strip()
        if raw.lower() in {"q", "quit", "exit"}:
            return "q"
        if raw in valid:
            return raw
        print("Invalid operator. Try one of: +  -  *  /")


def main() -> None:
    print("Simple Calculator")
    print("Examples: 2 + 3, 10 / 2")
    print()

    while True:
        op = prompt_operator()
        if op == "q":
            print("Bye!")
            return

        a = prompt_number("First number")
        b = prompt_number("Second number")

        try:
            result = compute(a, op, b)
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}")
            print()
            continue

        # Display result with minimal formatting noise.
        if result == int(result):
            result_str = str(int(result))
        else:
            result_str = str(result)
        print(f"Result: {a} {op} {b} = {result_str}")
        print()


if __name__ == "__main__":
    main()