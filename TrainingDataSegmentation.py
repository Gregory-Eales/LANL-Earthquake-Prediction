from progressbar import *

def segment_data():

	# progressbar code
	widgets = ['Test: ', Percentage(), ' ', Bar(marker='-',left='[',right=']'),
           ' ', ETA(), ' ', FileTransferSpeed()] #see docs for other options

	pbar = ProgressBar(widgets=widgets, maxval=629145481)
	pbar.start()

	# open the original file and save the column names
	original_path = "/Users/Greg/Desktop/LANL-Data/LANL-Training-Data.csv"
	original_file = open(original_path, "r")
	column_name = original_file.readline()

	# start the loop variables
	path = "/Users/Greg/Desktop/LANL-Data/LANL-Training-Data/Training-Data"

	file_number = 0
	segment_file_path = path+get_file_number(file_number)+".csv"
	segment_file = open(segment_file_path, "w")
	segment_file.write(column_name)
	last_line = 100
	line_number = 0
	
	for line in original_file:
		line_number += 1
		pbar.update(line_number)

		if float(line.split(",")[1]) > last_line:
			segment_file.close()
			file_number += 1
			segment_file_path = path+get_file_number(file_number)+".csv"
			segment_file = open(segment_file_path, "w")
			segment_file.write(column_name)
			
		last_line = float(line.split(",")[1])

		segment_file.write(line)

	segment_file.close()

	pbar.finish()


def get_file_number(n):
	n = str(n)
	n = "0"*(3-len(n)) + n
	return n


segment_data()
