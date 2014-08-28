from __future__ import division
import __member_city_matrix
from __member_city_matrix import create_member_city_matrix, get_all_members, get_all_cities
import datetime
import time
import sys
import __set
import heapq
from heapq import heappush, heappop



full_member_set_vectors = {}
full_city_set_vectors = {}
all_members = get_all_members()
all_cities = get_all_cities()

SIMILARITY_THRESHOLD = 0


# initialize our full_member_set_vectors and full_city_set_vectors dicts
# mostly just so we can test in main()
def initialize_sets():

	member_and_city_vectors = create_member_city_matrix()

	global full_member_set_vectors
	full_member_set_vectors = member_and_city_vectors[0]
	global full_city_set_vectors
	full_city_set_vectors = member_and_city_vectors[1]



# return sorenson similarity of set1 and set2
def sorenson(set1, set2):

	intersection = __set.find_intersection(set1, set2)
	set_size_1 = __set.get_size(set1)
	set_size_2 = __set.get_size(set2)

	similarity = 2.0 * intersection / (set_size_1 + set_size_2)

	return similarity


# return jaccard similarity of set1 and set2
def jaccard(set1, set2):

	intersection = __set.find_intersection(set1, set2)
	union = __set.find_union(set1, set2)

	if (union == 0):
		index = 1

	index = float(intersection) / union

	return index



# inverts first index in each two-tuple from a list
# helper method for find_k_similar
def invert_tuples(list_of_tuples):
	new_list = []
	for i in range(0, len(list_of_tuples)):
		old_tuple = list_of_tuples[i]
		inverted_index = -1 * old_tuple[0]
		new_tuple = (inverted_index, old_tuple[1])
		new_list.append(new_tuple)

	return new_list



# finds top k similar members to set1 from set2
def find_k_similar(k, set1, set2):

	similarity_max_heap = []

	num_members = len(set2)
	for i in range(0, num_members):

		member = all_members[i]
		similarity = __set.jaccard(set1, set2[member])

		member_similarity = (-1 * similarity, member) # -1 because python's
		# heap is a min-heap, use -1 to max it a max heap
		heappush(similarity_max_heap, member_similarity)

	top_k = []
	for i in range(0, k):
		top_k.append(heappop(similarity_max_heap))

	return invert_tuples(top_k)



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