# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 15:46:47 2019

@author: Tarun
"""

min_depth = 99999999
nodes_recursive = []
nodes_dynamic = []


def EditDistRecursive(str1, str2, m, n):
    if m == len(str1) and n == len(str2):
        return 0

    if n == len(str2):
        return len(str1) - m

    if m == len(str1):
        return len(str2) - n

    nodes_recursive.append([str1[m], str2[n]])

    if str1[m] == str2[n]:
        return EditDistRecursive(str1, str2, m + 1, n + 1)

    else:
        return min(EditDistRecursive(str1, str2, m, n + 1), EditDistRecursive(str1, str2, m + 1, n + 1), EditDistRecursive(str1, str2, m + 1, n)) + 1


def EditDist(str1, str2, m, n, depth=0):
    if m == len(str1) and n == len(str2):
        return depth

    if n == len(str2):
        return depth + len(str1) - m

    if m == len(str1):
        return depth + len(str2) - n

    nodes_dynamic.append([str1[m], str2[n], depth])

    if str1[m] == str2[n]:
        return EditDist(str1, str2, m + 1, n + 1, depth)
    else:
        depth += 1
        global min_depth

        if depth > min_depth:
            return depth

        inserted = EditDist(str1, str2, m, n + 1, depth)
        replaced = EditDist(str1, str2, m + 1, n + 1, depth)
        removed = EditDist(str1, str2, m + 1, n, depth)

        minimum = min(inserted, replaced, removed)
        if minimum < min_depth:
            min_depth = minimum

        return minimum


def main():
    str1 = "Sunday"
    str2 = "Saturday"

    print(EditDistRecursive(str1, str2, 0, 0))
    print(EditDist(str1, str2, 0, 0))

    print(f'Number of recursive nodes = {len(nodes_recursive)}')
    print(f'Number of dynamic nodes = {len(nodes_dynamic)}')

    print(f'Dynamic nodes: {nodes_dynamic}')
    print(f'Recursive nodes: {nodes_recursive}')


if __name__ == "__main__":
    main()
