import numpy
import csv

def write_city_set_vectors(city_set_vectors, output_file):
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



def write_numpy_matrix(matrix, output_file):
    """write numpy matrix to a csv file."""

    numpy.savetxt(output_file, matrix, delimiter=";")



def extract_numpy_matrix(input_file):
    """import a csv file to a numpy matrix."""

    return numpy.loadtxt(open(input_file,"rb"), delimiter=";", dtype="float32")



def write_dict(my_dict, output_file):

    writer = csv.writer(open('dict.csv', 'wb'))
    for key, value in my_dict.items():
        writer.writerow([key, value])



def extract_dict(input_file):

    reader = csv.reader(open('dict.csv', 'rb'))
    mydict = {}
    for x in reader:
        mydict[x[0]] = int(x[1].split(', '))
        mydict[x[0]][:0][1:]
        mydict[x[0]][-1:][:-1]

    return mydict