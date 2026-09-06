import sys
import os
from sys import stdin, stdout
from math import *
from collections import *
from itertools import *
from functools import *
from heapq import *
from bisect import *
from string import *
from decimal import *
from fractions import Fraction
import re

input = stdin.readline

def solve():
    # Write your solution here
    n = int(input())
    p = list(map(int, input().split()))

    i = 0
    grp = 1

    while i < n:
        j = i

        while j < n and  grp <= p[j] <= grp + 9:
            j += 1

        expected = min(10, n - grp + 1)


        if j - i != expected:
            print("No")
            return

        i = j

        grp += 10
    else:
        print("Yes")

# t = int(input())
# for _ in range(t):
solve()