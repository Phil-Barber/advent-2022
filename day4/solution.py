AssignmentPair = tuple[str, str]


class Assignment:
    def __init__(self, assignment: str) -> None:
        start, end = assignment.split("-")
        self.start = int(start)
        self.end = int(end)

    def __repr__(self) -> str:
        return f"[{self.start}, {self.end}]"

    def contains(self, other: "Assignment") -> bool:
        return self.start <= other.start and self.end >= other.end

    def overlaps(self, other: "Assignment") -> bool:
        return self.start <= other.end and self.end >= other.start


def assignment_contians_or_contained_in(one: Assignment, other: Assignment) -> bool:
    return one.contains(other) or other.contains(one)


def main(assignment_pairs: list[AssignmentPair]) -> int:
    assignments = [(Assignment(a), Assignment(b)) for a, b in assignment_pairs]
    return sum(one.overlaps(other) for one, other in assignments)


def input_lines() -> list[str]:
    with open("input") as input_file:
        return list(input_file.readlines())


if __name__ == "__main__":
    inputs = input_lines()
    inputs = [tuple(line[:-1].split(",")) for line in inputs if line[0]]
    answer = main(inputs)
    print(f"Answer: {answer}")
