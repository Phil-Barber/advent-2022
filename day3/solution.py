import itertools

Rucksack = str


def main(rucksacks: list[Rucksack]) -> int:
    mistakes = map(get_mistakes, rucksacks)
    all_mistakes = itertools.chain.from_iterable(mistakes)
    priorities = map(get_priority, all_mistakes)
    return sum(priorities)


def get_mistakes(rucksack: Rucksack) -> list[str]:
    set_left: set[str] = set()
    set_right: set[str] = set()
    comp_size = len(rucksack) / 2
    for idx, item in enumerate(rucksack):
        if idx < comp_size:
            set_left.add(item)
        else:
            set_right.add(item)
    mistakes = set_left & set_right
    if len(mistakes) > 1:
        raise Exception(f"\n{rucksack}\n{set_left}\n{set_right}\n{mistakes}")
    return mistakes


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
