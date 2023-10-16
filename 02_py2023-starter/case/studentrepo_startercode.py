
def genReport(dd):
    dottedline = '-'*70
    template = '{0:8} | {1:10} | {2:3} | {3:3} | {4:3} | {5:3} | {6:3} | {7:6} | {8:3}'
    print('CLASS REPORT')
    print(dottedline)
    print(template.format('REGID', 'NAME', 'AGE', 'P', 'C', 'M', 'B', 'AVG', 'R'))
    print(dottedline)
    for regid in dd.keys():
        name = dd[regid]['name']
        age  = dd[regid]['age']
        regid = dd[regid]['regid']
        phy = dd[regid]['phy']
        chem = dd[regid]['chem']
        math = dd[regid]['math']
        bio = dd[regid]['bio']
        avg = dd[regid]['avg']
        rank = dd[regid]['rank']
        print(template.format( regid, name, age,phy, chem, math, bio, avg, rank))
    print(dottedline)

def write2file(dd, path):
    pass

# Read the csv file as a text file
path = r"students.csv"
f = open(path)
content  = f.readlines()
f.close()

print(content)
print('-'*60 + ' > First Step')



# ------------------------ csv file is read and its content is available for further processing

# Read the coloums --> name,age,regid,phy,chem,math,bio,avg,rank
# Read a row --> Vijay,14,HPE001,99,98,97,96,0,0
# Construct a dictionary out of the column and the row
# Add that dictionary to the main dictionry that represents the class
# Repeat this process for all the entries in the csv file

classdict = {}
coldata = content[0]
columns = [s.strip() for s in coldata.split(',')]

for rowdata in content[1:]:
    rows = [s.strip() for s in rowdata.split(',')]
    temp = dict(zip(columns, rows))
    classdict[temp['regid']] = temp

print(classdict)
print('-'*60 + ' > Second Step')

# ------------------------- csv data is in the form of a dictionary

# Access the dictionary iteratively and calculate the average marks and
# update in the dictionary

for regid in classdict.keys():
    sum_subjects = 0
    for key in ['phy', 'chem', 'math', 'bio']:
        sum_subjects += float(classdict[regid][key])
    classdict[regid]['avg'] = sum_subjects/4

print(classdict)
print('-'*60 + ' > Third Step')

# ------------------------- dictionary updated with average data

# Calculate the rank
# collect all the averages -> into a list
# arrange the averages in descending order
# iterate the entire dictionary and update the rank based on the descending
# order of averages

avgs = []
for regid in classdict.keys():
    avgs.append(classdict[regid]['avg'])
avgs = list(set(avgs))
avgs.sort(reverse=True)

rank = 1
for avg in avgs:
    for regid in classdict.keys():
        if(classdict[regid]['avg'] == avg):
            classdict[regid]['rank'] = rank
    rank += 1
    
'''
Go through the entire dictionary
In a given dictionary, get the average
Find the index of that average in the averages list (descending order)
Update the rank
'''


print(classdict)
print('-'*60 + ' > Fourth Step')   



# ------------------------- dictionary updated with rank data

# Re-write the csv file

path = r"students_completed.csv"
f = open(path, "w")
f.write(coldata)

for regid in classdict.keys():
    r = list(zip(*classdict[regid].items()))[1]
    rowdata = ','.join([str(i) for i in r]) + '\n'
    f.write(rowdata)

f.close()

# ------------------------- resultant csv file is now ready with averages and ranks updated

genReport(classdict)
