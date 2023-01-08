#!/usr/bin/python
# coding=utf-8
import sys


def levenstein(str1, str2):
    n, m = len(str1), len(str2)
    if n > m:
        str1, str2 = str2, str1
        n, m = m, n

    cur_row = range(n + 1)
    for i in range(1, m + 1):
        prev_row, cur_row = cur_row, [i] + [0] * n
        for j in range(1, n + 1):
            add = prev_row[j] + 1
            delete = cur_row[j - 1] + 1
            change = prev_row[j - 1]
            if str1[j - 1] != str2[i - 1]:
                change += 1
            cur_row[j] = min(add, delete, change)

    return cur_row[n]


def pr(s1: str):
    s1 = s1.replace("\\n", "").split()
    s2 = ''
    for s in s1:
        if s != '':
            s2 += s
    return s2


if __name__ == '__main__':
    f1, f2 = sys.argv[1], sys.argv[2]

    with open(f1) as fp:
        str1 = fp.readlines()
        str1 = pr(str(str1))
        print(str1)
    with open(f2) as fp:
        str2 = fp.readlines()
        str2 = pr(str(str2))
        print(str2)
    diff = levenstein(str1, str2)
    max_len = max(len(str1), len(str2))
    print((max_len - diff) / max_len)
