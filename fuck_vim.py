input_file = open("all_cities.txt", 'r')


output_file = open("all_cities_insert.txt", 'w')

for line in input_file.readlines():
	split_line = line.split(' \'')
	newline = '(' + split_line[0] + ', \'' + split_line[1][:-2] + ')' + ',\n'
	output_file.write(newline)