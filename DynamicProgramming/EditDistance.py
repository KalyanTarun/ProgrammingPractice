# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 15:46:47 2019

@author: Tarun

Contributors = ['Akhilez']  # :P
"""
# Edit Distance problem using a recursive approach

min_depth = 99999999
nodes_recursive = []
nodes_dynamic = []


def edit_dist_recursive(str1, str2, m, n):
    # The following are three terminating conditions for the problem

    # If both the strings reach to end then no operations are required hence return 0
    if m == len(str1) and n == len(str2):
        return 0

    # If target string reaches to the end i.e the extra content of the source string is to be removed
    if n == len(str2):
        return len(str1) - m

    # If source string reaches to the end i.e contents need to be added to it
    if m == len(str1):
        return len(str2) - n

    nodes_recursive.append([str1[m], str2[n]])

    # If there is a match of characters then move both indices forward
    if str1[m] == str2[n]:
        return edit_dist_recursive(str1, str2, m + 1, n + 1)

    else:
        return 1 + min(
            edit_dist_recursive(str1, str2, m, n + 1),      # 1)Insert into source string i.e m,n+1
            edit_dist_recursive(str1, str2, m + 1, n + 1),  # 2)Replace the source string i.e m+1,n+1
            edit_dist_recursive(str1, str2, m + 1, n)       # 3)Remove the character in source string
        )


def edit_dist(str1, str2, m, n, depth=0):
    """
    In dynamic approach, we shall consider 'depth' of each node in the game tree.
    Each node shall have 3 children for the three operations - insert, replace, remove.

    The idea is that when there is a new node/operation to be performed, do it only if
    its depth is not greater than the minimum depth.
    """

    if m == len(str1) and n == len(str2):
        return depth

    if n == len(str2):
        return depth + len(str1) - m

    if m == len(str1):
        return depth + len(str2) - n

    nodes_dynamic.append([str1[m], str2[n], depth])

    if str1[m] == str2[n]:
        return edit_dist(str1, str2, m + 1, n + 1, depth)
    else:
        depth += 1
        global min_depth

        # if the next operation is going deeper than the minimum depth (of some previous solution/branch),
        # then do not go any deeper
        if depth > min_depth:
            return depth

        inserted = edit_dist(str1, str2, m, n + 1, depth)
        replaced = edit_dist(str1, str2, m + 1, n + 1, depth)
        removed = edit_dist(str1, str2, m + 1, n, depth)

        minimum = min(inserted, replaced, removed)

        # If any of the three solutions yielded a solution that is shallower than min_depth,
        # replace min_depth with new depth
        if minimum < min_depth:
            min_depth = minimum

        return minimum


def main():
    str1 = "Sunday"    # source string
    str2 = "Saturday"  # Target string

    print(edit_dist_recursive(str1, str2, 0, 0))
    print(edit_dist(str1, str2, 0, 0))

    print(f'Number of recursive nodes = {len(nodes_recursive)}')
    print(f'Number of dynamic nodes = {len(nodes_dynamic)}')

    print(f'Dynamic nodes: {nodes_dynamic}')
    print(f'Recursive nodes: {nodes_recursive}')


if __name__ == "__main__":
    main()
