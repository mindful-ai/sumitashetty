import json

# Reporting functions

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


print('-'*60 + ' > First Step')

# ------------------------ csv file is read and its content is available for further processing




print('-'*60 + ' > Second Step')

# ------------------------- csv data is in the form of a dictionary




print('-'*60 + ' > Third Step')

# ------------------------- dictionary updated with average data




print('-'*60 + ' > Fourth Step')

# ------------------------- dictionary updated with rank data

# Re-write the csv file

print('-'*60 + ' > Fifth Step')

# ------------------------- resultant csv file is now ready

genReport()


