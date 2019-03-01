# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 15:46:47 2019

@author: Tarun
"""


def EditDist(str1, str2, m, n):
    if m == len(str1) and n == len(str2):
        return 0

    if n == len(str2):
        return len(str2) - m

    if m == len(str1):
        return len(str1) - n

    if str1[m] == str2[n]:
        return EditDist(str1, str2, m + 1, n + 1)

    else:
        return min(EditDist(str1, str2, m, n + 1), EditDist(str1, str2, m + 1, n + 1), EditDist(str1, str2, m + 1, n)) + 1


def main():
    str1 = "Sunnyday"
    str2 = "Saturday"
    print(EditDist(str1, str2, 0, 0))


if __name__ == "__main__":
    main()
