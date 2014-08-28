import heapq
import __common_cities
import copy
import operator

def weighted_city_set(std_dict, weighting_matrix, all_members, all_cities,
	city_sets):
	"""weight cities based on weights from std_dict and weighting_matrix."""

	city_weights = {}

	members = std_dict.keys()
	city_weights_keys = []
	for i in range(0, len(members)):
		member = members[i]
		cities = city_sets[member]
		member_weight = std_dict[member]
		term_weights = weighting_matrix[all_members.index(member)]

		for i in range(0, len(cities)):
			city = cities[i]
			this_term_weight = term_weights[all_cities.index(city)]
			if city in city_weights_keys:
				city_weights[city] += member_weight * this_term_weight
			else:
				city_weights[city] = member_weight * this_term_weight
				city_weights_keys.append(city)

	return city_weights



# def top_k_weighted(k, weighted_city_set):

# 	# top_k = heapq.nlargest(k, weighted_city_set, key=weighted_city_set.get)
# 	top_k = sorted(weighted_city_set, key=weighted_city_set.get, reverse=True)

# 	return top_k



def top_k_recommendations(k, weighted_city_set, member, city_sets):
	"""sort weighted_city_set and return the top k items not in member's
	city_set."""

	sorted_weighted_cites = sorted(weighted_city_set,
		key=weighted_city_set.get, reverse=True)

	recs = [x for x in sorted_weighted_cites if x not in city_sets[member]]

	return recs[:k]