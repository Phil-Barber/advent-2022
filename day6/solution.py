import collections


def main(signal: str) -> int:
    marker_len = 14
    buffer: "collections.deque[str]" = collections.deque()
    for count, char in enumerate(signal, 1):
        buffer.append(char)
        if len(buffer) > marker_len:
            buffer.popleft()
        if len(buffer) == marker_len and len(list(set(buffer))) == marker_len:
            return count


def input_lines() -> list[str]:
    with open("input") as input_file:
        return list(input_file.readlines())


if __name__ == "__main__":
    inputs = input_lines()
    input = inputs[0][:-1]
    print(input)
    answer = main(input)
    print(f"Answer: {answer}")
