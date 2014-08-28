import numpy

def write_city_set_vectors_csv(city_set_vectors, output_file):
    """writes the table of members and cities from city_set_vectors
    to a csv file given by output_file."""

    if output_file == None:
        output_file = 'temp_output.csv'
    if output_file[-4:] != '.csv':
        output_file = output_file + '.csv'

    output = open(output_file, 'w')
    output.seek(0)
    output.truncate()

    # write cities (col names)
    for i in range(0, len(all_cities)):
        output.write(CSV_SEPARATOR + all_cities[i])

    output.write('\n')

    # write vectors with row names
    for i in range(0, len(all_members)):

        this_city_set = city_set_vectors[all_members[i]]

        output.write(all_members[i]) # row name
        for j in range(0, len(this_city_set)):
            output.write(CSV_SEPARATOR + str(this_city_set[j]))
        output.write('\n')

    output.close()



def write_numpy_matrix_csv(matrix, output_file):
    """write numpy matrix to a csv file."""

    numpy.savetxt(output_file, matrix, delimiter=";")