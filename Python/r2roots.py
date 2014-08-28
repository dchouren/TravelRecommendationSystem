output_file = open("r2_roots.txt", 'w')

first_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
second_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '\'', ' ']

for i in range(0, len(first_letter)):
	this_letter = first_letter[i]
	for j in range(0, len(second_letter)):
		second = second_letter[j]

		output_file.write("\"" + this_letter + second + "\", ")
		if j % 14 == 13:
			output_file.write('\n')