"""main project module. create a member-city matrix."""
from __future__ import division
from bs4 import BeautifulSoup
import requests
import time
import datetime
import sys
import __vector_similarity
import __weights
import re
import numpy as np
import __common_cities
import __recommender
import cProfile
import __server
import __csv
from os import listdir
from os.path import isfile, join

# from pycallgraph import PyCallGraph
# from pycallgraph.output import GraphvizOutput


CSV_SEPARATOR = ';'
LARGE_FORUMS = [
    "http://www.tripadvisor.com/ShowForum-g293910-i9303-Taiwan.html",
    "http://www.tripadvisor.com/ShowForum-g293915-i3686-Thailand.html",
    "http://www.tripadvisor.com/ShowForum-g293921-i8432-Vietnam.html",
    "http://www.tripadvisor.com/ShowForum-g293953-i7445-Maldives.html",
    "http://www.tripadvisor.com/ShowForum-g293951-i7006-Malaysia.html",
    "http://www.tripadvisor.com/ShowForum-g293889-i9243-Nepal.html",
    "http://www.tripadvisor.com/ShowForum-g293860-i511-India.html",
    "http://www.tripadvisor.com/ShowForum-g28926-i29-California.html",
    "http://www.tripadvisor.com/ShowForum-g28930-i18-Florida.html",
    "http://www.tripadvisor.com/ShowForum-g28927-i252-Colorado.html",
    "http://www.tripadvisor.com/ShowForum-g28943-i319-Michigan.html",
    "http://www.tripadvisor.com/ShowForum-g28951-i77-New_Jersey.html",
    "http://www.tripadvisor.com/ShowForum-g154967-i326-Nova_Scotia.html",
    "http://www.tripadvisor.com/ShowForum-g154922-i80-British_Columbia.html",
    "http://www.tripadvisor.com/ShowForum-g150805-i7-Yucatan_Peninsula.html",
    "http://www.tripadvisor.com/ShowForum-g190455-i550-Norway.html",
    "http://www.tripadvisor.com/ShowForum-g190372-i9179-Cyprus.html",
    "http://www.tripadvisor.com/ShowForum-g294451-i3250-Bulgaria.html",
    "http://www.tripadvisor.com/ShowForum-g189952-i223-Iceland.html",
    "http://www.tripadvisor.com/ShowForum-g294200-i9124-Egypt.html",
    "http://www.tripadvisor.com/ShowForum-g293740-i9186-South_Africa.html",
    "http://www.tripadvisor.com/ShowForum-g293794-i9249-Gambia.html",
    "http://www.tripadvisor.com/ShowForum-g294206-i9216-Kenya.html",
    "http://www.tripadvisor.com/ShowForum-g294291-i1357-Chile.html",
    "http://www.tripadvisor.com/ShowForum-g294311-i818-Peru.html",
    "http://www.tripadvisor.com/ShowForum-g294280-i1045-Brazil.html",
    "http://www.tripadvisor.com/ShowForum-g294266-i977-Argentina.html",
    "http://www.tripadvisor.com/ShowForum-g294331-i883-Fiji.html",
    "http://www.tripadvisor.com/ShowForum-g294338-i867-French_Polynesia.html",
    "http://www.tripadvisor.com/ShowForum-g294006-i2046-Oman.html",
    "http://www.tripadvisor.com/ShowForum-g293977-i1733-Israel.html",
    "http://www.tripadvisor.com/ShowForum-g293985-i2131-Jordan.html"
    ]
MEMBER_PAGE = "http://www.tripadvisor.com/members/"

# XXX refactor if time
def scrape_wanted_cities(member, soup):
    """get wanted cities for member from BeautifulSoup parsed members page."""

    # run through all the text in script tags
    for script_text in soup.find_all('script'):
        script_text = str(script_text)

        split_json = script_text.split("\"want\"],\"name\":\"")
        split_json2 = script_text.split("\"want\",\"fave\"],\"name\":\"")

        # no results
        if len(split_json) == 1 and len(split_json2) == 1:
            continue

        if len(split_json) < 51:
            return None

        # discard first split (not a city)
        cities = split_json[1:]

        # format all other cities
        for i in range(0, len(cities)):

            city_entry = cities[i]
            city = city_entry[:city_entry.index("\",\"")]
            cities[i] = city
            # if (city not in all_cities):
            #   all_cities.append(city)

            # member_sets will keep a unique list of cities with a
            # list of members who have been to that city
            if city in wanted_member_sets.keys():
                wanted_member_sets[city].append(member)
            else:
                wanted_member_sets[city] = [member]


    wanted_city_sets[member] = cities

    return cities



def scrape_visited_cities(member):
    """scrape cities visited by the member (url).
        return an array of cities."""

    MEMBER_PAGE = "http://www.tripadvisor.com/members/"
    request = requests.get(MEMBER_PAGE + member)

    # print MEMBER_PAGE + member

    data = request.text
    soup = BeautifulSoup(data)

    # want_count = soup.find_all('span', class_='pin_counts pc_want')

    # if want_count != None and not re.search('(0)', str(want_count)):
    #     scrape_wanted_cities(member, soup)


    # run through all the text in script tags
    for script_text in soup.find_all('script'):
        script_text = str(script_text)

        split_json = script_text.split("\"flags\":[\"been\"],\"name\":\"")

        # no results
        if len(split_json) == 1:
            continue

        # discard first split (not a city)
        cities = split_json[1:]

        # format all other cities
        for i in range(0, len(cities)):

            city_entry = cities[i]
            city = city_entry[:city_entry.index("\",\"")]
            cities[i] = city
            if city not in all_cities:
                all_cities.append(city)

            # member_sets will keep a unique list of cities with a
            # list of members who have been to that city
            if city in member_sets.keys():
                member_sets[city].append(member)
            else:
                member_sets[city] = [member]

    city_sets[member] = cities

    return cities



def scrape_top_users(forum_url):
    """return list of "expert" member urls from this forum."""

    request = requests.get(forum_url)

    data = request.text
    soup = BeautifulSoup(data)

    # run through all the text in script tags
    expert_div = soup.find_all('div', class_="expertbox")

    split_experts = str(expert_div).split(
        "<div class=\"nameposts\">\n<a href=\"/members-forums/")

    # print split_experts

    experts = split_experts[1:]

    for i in range(0, len(experts)):

        experts_entry = experts[i]
        expert_name = experts_entry[:experts_entry.index('\"')]
        experts[i] = expert_name
        if expert_name not in all_members:
            all_members.append(expert_name)

    return experts


def readAllCities():

    mypath = "/home/dchouren/Documents/workspace/TripNoticeRecommendationSystem/memberPages/";
    experts = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

    for j in range(0, len(experts)):
        thisExpert = experts[j]
        readVisitedCities(thisExpert)



def readVisitedCities(member):

    # print MEMBER_PAGE + member
    mypath = "/home/dchouren/Documents/workspace/TripNoticeRecommendationSystem/memberPages/";
    memberPage = open(mypath + member, 'r')
    memberHtml = memberPage.read()

    soup = BeautifulSoup(memberHtml)

    member = member[:-4]

    print member

    # want_count = soup.find_all('span', class_='pin_counts pc_want')

    # if want_count != None and not re.search('(0)', str(want_count)):
    #     scrape_wanted_cities(member, soup)
    been = soup.find('span', class_='pin_counts pc_been').get_text()
    strippedBeen = been[1:-1]
    beenCount = int(strippedBeen.replace(",", ""))
    if beenCount < 50:
        return None

    all_members.append(member)

    # run through all the text in script tags
    for script_text in soup.find_all('script'):
        script_text = str(script_text)

        split_json = script_text.split("\"flags\":[\"been\"],\"name\":\"")

        # no results
        if len(split_json) == 1:
            continue

        # discard first split (not a city)
        cities = split_json[1:]
        # print len(cities)

        # format all other cities
        for i in range(0, len(cities)):

            city_entry = cities[i]
            city = city_entry[:city_entry.index("\",\"")]
            cities[i] = city
            if city not in all_cities:
                all_cities.append(city)

            # member_sets will keep a unique list of cities with a
            # list of members who have been to that city
            if city in member_sets.keys():
                member_sets[city].append(member)
            else:
                member_sets[city] = [member]

    city_sets[member] = cities

    return cities


def get_all_members():
    """return list of all members."""

    return all_members


def get_all_cities():
    """return list of all cities."""

    return all_cities




def fill_member_set_vectors(member_sets, all_members):
    """fill members who visted vectors from sorted member_sets and
    all_members."""

    member_lists = member_sets.values()
    num_members = len(all_members)

    member_set_vectors = {}

    for i in range(0, len(member_sets)):

        this_city = all_cities[i]
        these_members = member_sets[this_city]

        members_vector = []

        for j in range(0, num_members):

            this_member = all_members[j]
            if this_member in these_members:
                members_vector.append(1)
            else:
                members_vector.append(0)

        member_set_vectors[this_city] = members_vector

    return member_set_vectors



def fill_city_set_vectors(city_sets, all_cities):
    """fill vector of cities each member has visited from sorted city_sets and
        all_cities."""

    members = city_sets.keys()
    num_cities = len(all_cities)

    city_set_vectors = {}

    for i in range(0, len(city_sets)):

        this_member = members[i]
        these_cities = city_sets[this_member]

        cities_vector = []

        for j in range(0, num_cities):

            this_city = all_cities[j]
            if this_city in these_cities:
                cities_vector.append(1)
            else:
                cities_vector.append(0)

        city_set_vectors[this_member] = cities_vector

    return city_set_vectors



def create_member_city_matrix():
    """create a member-city matrix and return a tuple with the full member
    set vectors and the full city set vectors."""

    # for i in range(0, len(LARGE_FORUMS)):

    #     experts = scrape_top_users(LARGE_FORUMS[i])

    #     for j in range(0, len(experts)):

    #         scrape_visited_cities(experts[j])

    experts = readAllCities()

    full_member_set_vectors = fill_member_set_vectors(member_sets, all_members)
    full_city_set_vectors = fill_city_set_vectors(city_sets, all_cities)

    return (full_member_set_vectors, full_city_set_vectors)



def make_matrix(all_members, all_cities, full_city_set_vectors):
    """make all of this into a nice matrix."""

    # city_set_vectors = full_city_set_vectors.values()
    # print city_set_vectors

    list_of_city_sets = []

    for i in range(0, len(all_members)):
        city_set_vector = full_city_set_vectors[all_members[i]]
        cities_tuple = tuple(city_set_vector)
        list_of_city_sets.append(cities_tuple)
     # = [tuple(x) for x in city_set_vectors]

    member_city_matrix = np.array(list_of_city_sets, dtype='f')

    return member_city_matrix



if __name__ == "__main__":

    TEST_MEMBER = sys.argv[1]

    all_members = []
    all_cities = []
    member_sets = {} # dict with cities as keys and a list of members
    # who have visted the city as values
    city_sets = {} # dict with members as keys and a list of cities they've
    # visited as values
    wanted_member_sets = {}
    wanted_city_sets = {}

    start_time = time.time()
    print "\n" + str(datetime.datetime.time(datetime.datetime.now())) + "\n"


    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    else:
        output_file = None

    member_and_city_vectors = create_member_city_matrix()
    full_member_set_vectors = member_and_city_vectors[0]
    full_city_set_vectors = member_and_city_vectors[1]

    mark_time = time.time()
    print "done scraping: " + str(mark_time - start_time)

    # __weights.tf_idf(full_city_set_vectors.values())

    member_city_matrix = make_matrix(all_members, all_cities,
        full_city_set_vectors)

    tf_idf_mc_matrix = __weights.tf_idf_matrix(member_city_matrix, member_sets,
        all_cities)


    print "done tf_idf: " + str(time.time() - mark_time)
    mark_time = time.time()

    test_set = full_city_set_vectors[TEST_MEMBER]

    k = min(10, len(all_members) - 1)
    similar_row_heap = __vector_similarity.similar_row_heap(
        tf_idf_mc_matrix[all_members.index(TEST_MEMBER)],
        tf_idf_mc_matrix, all_members, TEST_MEMBER)

    print "done similar_row_heap: " + str(time.time() - mark_time)
    mark_time = time.time()

    top_k = __vector_similarity.pop_k_tuples(k, similar_row_heap)

    top_k_members = __vector_similarity.pop_k_members(k, similar_row_heap)

    top_k_common_cities = __common_cities.fewest_common_cities(
        top_k_members, city_sets)
    top_k_common_cities_excluding = __common_cities.\
                fewest_common_cities_excluding(
                            top_k_members, TEST_MEMBER, city_sets)

    std_theshold = 1.0
    top_std = __vector_similarity.pop_std_tuples(std_theshold, similar_row_heap)

    top_std_members = __vector_similarity.pop_std_members(std_theshold,
                            similar_row_heap)

    top_std_common_cities = __common_cities.fewest_common_cities(
        top_std_members, city_sets)
    top_std_common_cities_excluding = __common_cities.\
                fewest_common_cities_excluding(
                            top_std_members, TEST_MEMBER, city_sets)

    print "done common cities: " + str(time.time() - mark_time)
    mark_time = time.time()

    std_weights = __vector_similarity.std_dict(top_std)
    weighted_cities = __recommender.weighted_city_set(std_weights,
        tf_idf_mc_matrix, all_members, all_cities, city_sets)
    # top_k_cities = __recommender.top_k_weighted(k, weighted_cities)

    top_k_recs = __recommender.top_k_recommendations(10, weighted_cities,
        TEST_MEMBER, city_sets)

    print "done recommending: " + str(time.time() - mark_time)
    mark_time = time.time()

    # __server.create_table('members_cities', all_cities, 'members_cities.txt')
    # __csv.write_numpy_matrix(member_city_matrix, 'member_city_matrix.csv')
    # __csv.write_numpy_matrix(tf_idf_mc_matrix, 'tf_idf_mc_matrix.csv')
    # new_mc_matrix = __csv.extract_numpy_matrix('member_city_matrix.csv')

    # __csv.write_dict(full_city_set_vectors, 'city_vector.csv')
    # new_city_vector = __csv.extract_dict('city_vector.csv')
    # __csv.write_dict(full_member_set_vectors, 'member_vector.csv')
    # new_member_vector = __csv.extract_dict('member_vector.csv')

    # print "done writing: " + str(time.time() - mark_time)
    # mark_time = time.time()

    # top_k = __vector_similarity.find_k_similar_rows(k, test_set,
    # tf_idf_mc_matrix, all_members, 'jaccard')


    # write_member_city_matrix_csv(full_city_set_vectors, output)


    end_time = time.time()
    elapsed_time = end_time - start_time

    print ("\nparsed %d cities for %d members in "
    "%f seconds\n" % (len(all_cities), len(all_members), elapsed_time))
    # print "wrote matrix to %s\n" % sys.argv[1]

    print datetime.datetime.time(datetime.datetime.now())
    print "\a"

# with PyCallGraph(output=GraphvizOutput()):
#     code_to_profile()
