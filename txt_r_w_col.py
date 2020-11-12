## assume we are given a text file with each line separated by space; the first 6 lines (0-->5) are headers.
with open('84-12_04Nov20.txt', 'r') as rf:
	with open('new_copy.txt', 'w') as wf:
		for idx, line in enumerate(rf):
			if idx >= 6 and if idx <= 8:
				# wf.write(line) ###### line by line, separated by \n

				# wf.write(line.split()[0]) # saved into one line separated by space. #.split(0) to separate "columns".

				wf.write('%-15s %s\n' % (line.split()[0],line.split()[2])) ##### %-15s means left justify a 15-space field for a string

			if idx > 8:
				break



