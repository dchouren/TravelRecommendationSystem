"""Compare vectors for similarity."""
from __future__ import division
import datetime
import time
import sys
import __set
import numpy as np
import __statistics
import heapq
from heapq import heappush, heappop
from copy import copy



# full_member_set_vectors = {}
# full_city_set_vectors = {}
# all_members = get_all_members()
# all_cities = get_all_cities()

SIMILARITY_THRESHOLD = 0
METRICS = ['jaccard', 'sorenson']


# initialize our full_member_set_vectors and full_city_set_vectors dicts
# mostly just so we can test in main()
# def initialize_sets():

#   member_and_city_vectors = create_member_city_matrix()

#   global full_member_set_vectors
#   full_member_set_vectors = member_and_city_vectors[0]
#   global full_city_set_vectors
#   full_city_set_vectors = member_and_city_vectors[1]



def sorenson(set1, set2):
    """return sorenson similarity of set1 and set2."""

    intersection = __set.find_intersection(set1, set2)
    set_size_1 = __set.get_size(set1)
    set_size_2 = __set.get_size(set2)

    similarity = 2.0 * intersection / (set_size_1 + set_size_2)

    return similarity



def jaccard(set1, set2):
    """return jaccard similarity of set1 and set2."""

    intersection = __set.find_intersection(set1, set2)
    union = __set.find_union(set1, set2)

    if (union == 0):
        index = 1

    index = float(intersection) / union

    return index



def invert_tuples(list_of_tuples):
    """invert first index in each tuple from a list.
        helper method for find_k_similar."""
    new_list = []
    for i in range(0, len(list_of_tuples)):
        old_tuple = list_of_tuples[i]
        inverted_index = -1 * old_tuple[0]
        new_tuple = (old_tuple[2], inverted_index, old_tuple[1])
        new_list.append(new_tuple)

    return new_list



def find_k_similar_dict(k, set1, set2, metric):
    """find top k similar keys in set2 (dict with list as value) to set1 (list) using a specified metric to compares lists."""

    metric = metric.lower()
    # default metric to jaccard
    if not(metric in METRICS):
        metric = 'jaccard'

    similarity_max_heap = []

    length = len(set2)
    for i in range(0, length):

        key = set2.keys()[i]

        if (metric == 'jaccard'):
            similarity = jaccard(set1, set2[key])
        elif (metric == 'sorenson'):
            similarity = sorenson(set1, set2[key])

        similarity_tuple = (-1 * similarity, key) # -1 because python's
        # heap is a min-heap, use -1 to max it a max heap
        heappush(similarity_max_heap, similarity_tuple)

    top_k = []
    for i in range(0, k):
        top_k.append(heappop(similarity_max_heap))

    return invert_tuples(top_k)



def similar_row_heap(sample, matrix, row_names, metric):
    """return a max heap of similar matrix rows to a sample using metric."""

    metric = metric.lower()
    # default metric to jaccard
    if not(metric in METRICS):
        metric = 'jaccard'

    similarity_max_heap = []

    length = len(matrix)

    mean_total = 0
    similarity = []
    num_samples = length
    samples = []

    for i in range(0, length):

        if (metric == 'jaccard'):
            similarity_score = jaccard(sample, matrix[i])
        elif (metric == 'sorenson'):
            similarity_score = sorenson(sample, matrix[i])

        if (similarity_score == 1.0): # we must be testing against this same
            # user
            num_samples -= 1
            continue
        else:
            similarity.append( (similarity_score, row_names[i]) )
            mean_total += similarity_score

    samples = [x[0] for x in similarity]
    mean = np.mean(samples)
    std_dev = np.std(samples)

    for i in range(0, num_samples):

        # tuple will be (-sim score, std dev from mean, row name)
        # use negative sim score because python's
        # heapq is a min-heap, use -1 to make it a max heap
        similarity_tuple = (-1 * similarity[i][0], __statistics.z_score(
            mean, similarity[i][0], std_dev), similarity[i][1])
        heappush(similarity_max_heap, similarity_tuple)

    return similarity_max_heap



def pop_k_tuples(k, similarity_max_heap):
    """return top k results from row similarity heap."""

    max_heap = copy(similarity_max_heap)
    # top_k = []
    # for i in range(0, k):
    #     top_k.append(heappop(max_heap))

    top_k = heapq.nlargest(k, similarity_max_heap)

    return invert_tuples(top_k)



def pop_k_members(k, similarity_max_heap):
    """return top k members from max_heap."""

    max_heap = copy(similarity_max_heap)
    top_k_tuples = pop_k_tuples(k, max_heap)
    top_k_members = [x[0] for x in top_k_tuples]

    return top_k_members



def pop_std_tuples(std_threshold, similarity_max_heap):
    """return results from row similarity heap with a threshold std_dev."""

    max_heap = copy(similarity_max_heap)
    std_dev_tuples = []

    popped = heappop(max_heap)
    popped_std_dev = popped[1]

    while(popped_std_dev > std_threshold):
        std_dev_tuples.append(popped)
        popped = heappop(max_heap)
        popped_std_dev = popped[1]

    return invert_tuples(std_dev_tuples)



def pop_std_members(std_threshold, similarity_max_heap):
    """return members from row similarity heap with a threshold std_dev."""

    max_heap = copy(similarity_max_heap)
    std_dev_tuples = pop_std_tuples(std_threshold, similarity_max_heap)
    std_dev_members = [x[0] for x in std_dev_tuples]

    return std_dev_members



def std_dict(tuples_list):
    """make a dict between member and std."""

    stds = {}
    for i in range(0, len(tuples_list)):
        stds[tuples_list[i][0]] = tuples_list[i][2]

    return stds



if __name__ == "__main__":

    print "\n"
    start = time.time()

    initialize_sets()
    test_set = full_city_set_vectors['mariatan']
    top_k = find_k_similar(10, test_set, full_city_set_vectors)

    end = time.time()
    elapsed_time = end - start

    print "\n"
    print elapsed_time
    print datetime.datetime.time(datetime.datetime.now())
    print "\a"