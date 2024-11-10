#!/usr/bin/env python3
from brain_games.cli import name
from brain_games.scripts.brain_even import is_even
from brain_games.scripts.brain_calc import calc


def main():
    print("Welcome to the Brain Games!")
    print(f"Hello, {name}!")
    is_even()
    calc()


if __name__ == "__main__":
    main()
