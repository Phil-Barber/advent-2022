import collections


def main(calory_lines) -> int:
    calory_counter = collections.Counter()
    elf_idx = 0
    for calories in calory_lines:
        if not calories:
            elf_idx += 1
            continue
        calory_counter[elf_idx] += int(calories)
    return calory_counter.most_common(1)[0][1]


def input_lines() -> list[str]:
    with open("input") as input_file:
        return list(input_file.readlines())


if __name__ == "__main__":
    inputs = input_lines()
    inputs = [line[:-1] for line in inputs if line[0]]
    # print(inputs[0])
    # print(inputs[-1])
    # print(len(inputs))
    answer = main(inputs)
    print(f"Answer: {answer}")
