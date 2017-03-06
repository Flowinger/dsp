import pandas as pd
import re
from collections import OrderedDict
data = pd.read_csv('/Users/flowinger/ds/metis/metisgh/prework/dsp/python/faculty.csv', sep=',', skipinitialspace=True)

first_names = []
last_names = []
names = []
titles = []
faculty_dict = {}

# Q6
def create_faculty_dict(df):
	for name in data['name']:
		names.append(name.split(' '))
	for name in names:
		first_names.append(" ".join(name[:-1]))
		last_names.append(name[-1])

	data['first name'] = first_names
	data['last name'] = last_names
	for title in data['title']:
		#title = title.replace(' of Biostatistics', '')
		#title = title.replace(' is Biostatistics', '')
		titles.append(re.findall(r'.*[\w+\sP]rofessor', title))
	data['title'] = titles

	for i in range(len(data)-1):
		if last_names[i] not in faculty_dict:
			faculty_dict[last_names[i]] = [data['title'][i], data['degree'][i], data['email'][i]]
		else:
			faculty_dict[last_names[i]].append([data['title'][i], data['degree'][i], data['email'][i]])
	return faculty_dict

create_faculty_dict(data)
print(list(sorted(faculty_dict.items())[:3]))

# Q7
professor_dict = {}

def create_professor_dict(df):
	for i in range(len(data)-1):
		if last_names[i] not in professor_dict:
			professor_dict[(first_names[i], last_names[i])] = [data['title'][i], data['degree'][i], data['email'][i]]
		else:
			professor_dict[(first_names[i], last_names[i])].append([data['title'][i], data['degree'][i], data['email'][i]])
	return professor_dict

create_professor_dict(data)
print(list(sorted(professor_dict.items()))[:3])

# Q8
ordered_prof_dict = OrderedDict(sorted(professor_dict.items(), key = lambda prof: prof[0][1]))
print(ordered_prof_dict)

