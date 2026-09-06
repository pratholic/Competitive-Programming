import sys
from math import *
from collections import *
from itertools import *
from functools import *
from heapq import *
from bisect import *


INPUT_FILE = "final_product_chapter_1_input.txt"
OUTPUT_FILE = "output.txt"


def solve(t):
    n, a, b = map(int, input().split())

    ans = [1] * (2 * n)
    ans[-1] = b

    return ans


if __name__ == "__main__":

    with open(INPUT_FILE, "r") as fin:
        input = fin.readline

        T = int(input())

        answers = []

        for tc in range(1, T + 1):
            ans = solve(tc)
            answers.append(
                f"Case #{tc}: {' '.join(map(str, ans))}"
            )

    with open(OUTPUT_FILE, "w") as fout:
        fout.write("\n".join(answers))
        fout.write("\n")