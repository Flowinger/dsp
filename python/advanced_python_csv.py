import re
import csv

def get_emails(file):
	#emails = str(df['email']).split('\n')
	faculty = open('/Users/flowinger/ds/metis/metisgh/prework/dsp/python/faculty.csv')
	file2 = []
	
	for line in faculty:
		line = line.strip()
		file2.append(line)
	emails = re.compile(r'\w*@.*?.edu')
	matches = emails.findall(str(file2))
	return matches
print(get_emails(file0))

def write_to_csv(res):
	csv_file = '/Users/flowinger/ds/metis/metisgh/prework/dsp/python/emails.csv'
	
	with open(csv_file, 'w') as csvfile:
		writer = csv.writer(csvfile, lineterminator='\n')
		for email in res:
			writer.writerow([email])
write_to_csv(get_emails(file0))

