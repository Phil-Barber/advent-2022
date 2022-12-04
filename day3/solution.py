import functools
import operator
import typing

Rucksack = str
Group = tuple[Rucksack, Rucksack, Rucksack]


def main(rucksacks: list[Rucksack]) -> int:
    badges = map(get_badge, get_groups(rucksacks))
    priorities = map(get_priority, badges)
    return sum(priorities)


def get_groups(rucksacks: list[Rucksack]) -> typing.Iterator[Group]:
    group: list[Rucksack] = []
    for rucksack in rucksacks:
        if len(group) == 3:
            yield typing.cast(Group, tuple(group))
            group = []
        group.append(rucksack)
    yield typing.cast(Group, tuple(group))


def get_badge(group: Group) -> list[str]:
    common = list(functools.reduce(operator.and_, map(set, group)))
    if len(common) != 1:
        raise Exception(f"nope\n{group}\n{common}")
    return common[0]


def get_priority(mistake: str) -> int:
    order = ord(mistake)
    return order - 38 if mistake.isupper() else order - 96


def input_lines() -> list[str]:
    with open("input") as input_file:
        return list(input_file.readlines())


if __name__ == "__main__":
    inputs = input_lines()
    inputs = [line[:-1] for line in inputs if line[0]]
    answer = main(inputs)
    print(f"Answer: {answer}")
