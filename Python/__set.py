from __future__ import division

# return set size (number of nonzero entries)
def get_size(set):

    size = 0
    for i in range(0, len(set)):
        if (set[i] != 0):
            size += 1

    return size


# return set size (sum of nonzero entries)
def additive_size(set):

    size = 0
    for i in range(0, len(set)):
        if (set[i] != 0):
            size += set[i]

    return size


# return size of intersection between two sets
# set span assumed to be same size
def find_intersection(set1, set2):

    intersection = 0
    for i in range(0, len(set1)):
        if (set1[i] != 0 and set2[i] != 0):
            intersection += 1

    return intersection


# return the size of the union between set1 and set2
# sets assumed to have same underlying attributes
def find_union(set1, set2):

    union = 0
    for i in range(0, len(set1)):
        if (set1[i] != 0 or set2[i] != 0):
            union += 1

    return union


