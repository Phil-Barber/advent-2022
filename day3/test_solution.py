import pytest

from solution import Group, Rucksack, get_badge, get_priority, main

example_input = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]


def test_example_input() -> None:
    assert main(example_input) == 70


@pytest.mark.parametrize(
    "group, badge",
    [
        (example_input[:3], "r"),
        (example_input[3:], "Z"),
    ],
)
def test_get_badge(group: Group, badge: set[str]) -> None:
    assert get_badge(group) == badge


@pytest.mark.parametrize(
    "mistakes, priority",
    [
        ("p", 16),
        ("L", 38),
        ("P", 42),
        ("v", 22),
        ("t", 20),
        ("s", 19),
        ("a", 1),
        ("z", 26),
        ("A", 27),
        ("Z", 52),
    ],
)
def test_get_mistakes(mistakes: set[str], priority: int) -> None:
    assert get_priority(mistakes) == priority
