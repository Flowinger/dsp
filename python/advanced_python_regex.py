import pandas as pd
import re
from collections import Counter


file1 = pd.read_csv('/Users/flowinger/ds/metis/metisgh/prework/dsp/python/faculty.csv', sep=',', skipinitialspace=True)
faculty = open('/Users/flowinger/ds/metis/metisgh/prework/dsp/python/faculty.csv')


def get_degrees(df):
	'''Find the different degrees and their frequencies'''
	degrees = re.findall(r'[A-Z].*[A-Z]', str(df['degree']))
	degreeDict = {}
	for degree in degrees:
		degree = degree.replace('.','')
		if len(degree.split(' ')) > 1:
				for i in degree.split(' '):
					degreeDict[i] = degreeDict.get(i, 0) + 1
		else:
			degreeDict[degree] = degreeDict.get(degree, 0) + 1

	print(degreeDict)
get_degrees(file1)

def get_titles(df):
	'''Find the different titles and their frequencies without regex'''
	titles = {}
	for title in df['title']:
		title = re.sub(r' is ', ' of ', title)
		titles[title] = titles.get(title, 0) + 1
	print(titles)
	print('Number of titles: ' + str(sum(titles.values())))
get_titles(file1)

def get_titles_regex(file):
	''' Find the different titles and their frequencies with regex'''
	file0 = []
	for line in file:
		line = line.strip()
		file0.append(line)
	
	title = re.sub(r' is ', ' of ', str(file0))
	titles = re.compile(r'(\w*\s\w*\s|\w*\s)of\sBiostatistics')
	matches = titles.findall(str(title))

	match_count = {}	
	for match in matches:
		match_count[match] = match_count.get(match, 0) + 1
	print(match_count)
	print('Number of titles: ' + str(sum(match_count.values())))
	
get_titles_regex(faculty)

def get_emails(file):
	faculty = open('/Users/flowinger/ds/metis/metisgh/prework/dsp/python/faculty.csv')
	file2 = []
	for line in faculty:
		line = line.strip()
		file2.append(line)
	emails = re.compile(r'\w*@.*?.edu')
	matches = emails.findall(str(file2))
	return matches
get_emails(faculty)

# print markdown table for Q3
print('Email |')
print('--- |')
for i in get_emails(faculty):
	print(i, ' |')

def get_email_domains(file):
	faculty = open('/Users/flowinger/ds/metis/metisgh/prework/dsp/python/faculty.csv')
	file2 = []
	for line in faculty:
		line = line.strip()
		file2.append(line)
	emails = re.compile(r'@.*?.edu')
	matches = emails.findall(str(file2))
	matches = list(set(matches))
	email_list = {}
	for i in matches:
		email_list[i] = 0
		for x in file1['email']:
			if re.search(i, x):
				email_list[i] += 1
	return email_list
get_email_domains(faculty)

# print markdown table for Q4
print('Email domain | Count |')
print('| --- | --- |')
domains = get_email_domains(faculty)
for i, j in domains.items():
	print(i, ' |', j, ' |')



