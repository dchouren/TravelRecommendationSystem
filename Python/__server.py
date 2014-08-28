DATABASE = 'tripnoti_site'
USER = 'root'
PASSWORD = 'oscar130Z/'



def create_table(title, col_names, output_file):
	"""create table."""

	cmd = "CREATE TABLE " + title + ' ('
	cmd += "`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,"
	cmd += "`user` VARCHAR( 80 ) NOT NULL,"

	for i in range(0, len(col_names) - 1):
		col_title = "`" + col_names[i] + "`"
		cmd += col_title + ' DECIMAL( 10, 6 ) NOT NULL,'

	cmd += ("`" + col_names[len(col_names) - 1] + "`"
			+ ' DECIMAL( 10, 6 ) NOT NULL);')

	open(output_file, 'w').write(cmd)




def upload_matrix(row_names, col_names, matrix):
	"""upload matrix with row_names and col_names to server."""



if __name__ == "__main__":
	print "__server is main"
