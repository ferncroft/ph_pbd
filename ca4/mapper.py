import sys
def read_file(changes_file):
    # use strip to strip out spaces and trim the line.
    data = [line.strip() for line in open(changes_file, 'r')]
    return data
    
def save_commits(commits, any_file):
    my_file = open(any_file, 'w')
    my_file.write('Revision,Author,Date\n')
    for commit in commits:
        my_file.write(commit['revision']+','+commit('author')+','+commit('date')+'\n')
    my_file.close()

def get_commit(data):
    data = data.strip()
    no_of = data.count('|')
    # parse each of the commits and put them into a list of commits
    details = data.split('|')
            # the author with spaces at end removed.
    my_date = details[2].strip()
    my_time = my_date[11:20]
    my_date = my_date[:10]
    commit = {'revision': details[0].strip(), 'author': details[1].strip(),
                'date': my_date, 'time':my_time, 'number_of_lines': details[3].strip().split(' ')[0]
            }
    return commit


# Now we loop over lines in the system input
for line in sys.stdin:
    # Strip the line of whitespace and split into a list
    line = line.strip()
    if line == 72*'-':
        bHeaderRecord = True
    elif bHeaderRecord == True:
        bHeaderRecord = False
        commit = get_commit(line)
#        print('output',commit.get('revision') + ',' + commit['author'] + ',' + commit['date'])
      #  print(commit['revision'] + ',' + commit['author'] + ',' + commit['date'])
        print(commit.get('revision')+ ',' + commit.get('author') + ',' + commit.get('date')+','+commit.get('time')+','+commit.get('number_of_lines'))

#if __name__ == '__main__':
    #do things for the test
    