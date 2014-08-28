"""module is used to find common cities between members."""

def common_cities(members, city_sets):
    """return common cities between list of members."""

    common_cities = city_sets[members[0]]

    for i in range(1, len(members)):

        new_cities = city_sets[members[i]]
        common_cities = list(set(common_cities).intersection(new_cities))

    # print common_cities
    return common_cities


def common_cities_excluding(members, member_to_exclude, city_sets):
    """return common cities between list of members but excluding
    member_to_exclude."""

    cities = common_cities(members, city_sets)
    cities = [x for x in cities
                        if x not in city_sets[member_to_exclude]]

    return cities


def shrink_common_cities(common_cities, member_to_add, city_sets):
    """return cities member_to_add has in common with existing common_cities
    list."""

    new_cities = city_sets[member_to_add]
    common_cities = [x for x in
                        list(set(common_cities).intersection(new_cities))]

    return common_cities


def filter_common_cities(common_cities, members_to_add,
                            city_sets):
    """find cities members_to_add have in common with existing
    common_cities list between members until there are no cities in
    common. return common_cities and members who make up those cities."""

    members = []

    for i in range(0, len(members_to_add)):

        next_member = members_to_add[i]

        temp_common_cities = shrink_common_cities(common_cities,
            next_member, city_sets)
        if temp_common_cities:
            common_cities = temp_common_cities
            members.append(next_member)
        else:
            return (common_cities, members)

    return (common_cities, members)


def fewest_common_cities(members_to_add, city_sets):
    """find cities members have in common until there are no cities in
    common. return common_cities and members who make up those cities."""

    first_member = members_to_add[0]
    common_cities = city_sets[first_member]

    return filter_common_cities(common_cities, members_to_add,
                                    city_sets)


def fewest_common_cities_excluding(members_to_add, member_to_exclude,
                                        city_sets):
    """find smallest set of common cities between members_to_add,
    excluding member_to_exclude."""

    first_member = members_to_add[0]
    common_cities = city_sets[first_member]
    common_cities = [x for x in common_cities
                        if x not in city_sets[member_to_exclude]]

    return filter_common_cities(common_cities, members_to_add,
                            city_sets)

