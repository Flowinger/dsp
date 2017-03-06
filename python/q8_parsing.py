# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

file = open('/Users/flowinger/ds/metis/metisgh/prework/dsp/python/football.csv', encoding='utf-8')
rows = []
difference = {}

def read_file(file):
	for line in file:
		line = line.strip('\ufeff').strip('\n').split(',')
		rows.append(line)
	descr = rows.pop(0)
	return rows

def goal_difference(table):
	for team in table:
		difference[team[0]] = abs(int(team[5]) - int(team[6]))
	return min(difference, key=difference.get)

# easier version
df = pd.read_csv('/Users/flowinger/ds/metis/metisgh/prework/dsp/python/football.csv', sep=',', skipinitialspace=True)
print(df.head())
def goal_differences(file):
	goal_differences = abs(df['Goals'] - df['Goals Allowed'])
	df['Goals difference'] = goal_differences
	print(df)
	return df['Team'].ix[df['Goals difference'].idxmin()]

