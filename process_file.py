
import re
import csv

dict1 = {}
vlan = re.compile(r'.*address\s+(.*)', re.I|re.M)
v4v6 = re.compile(r'(\w+)\-.*interface\s+(.*)', re.I|re.M)

for line in open('v6', 'r'):
    m = re.findall(v4v6, line)
    if m:
        test = []           #PReserving key in list until next key
        test.append(m[0])   #m[0] is the vlan name matching
    else:
     try:
        key =  '_'.join(test[0]) # Getting reserve key to assign the values
        line = re.findall(vlan, line) # Filtering IP v4v6 addressess
        #if line:  #Instead of try and except you can use if loop if there is no else
            # Appending the multiple matching values to the same key
            #dict1.setdefault(key, []).append(line)
        dict1.setdefault(key, []).append(line)
     except:
        pass

# To put output into the CSV - pythonish way
#with open('eggs.csv', 'w') as f1:
#    writer=csv.writer(f1, delimiter=',',lineterminator='\n',)
#    for key, value in dict1.items():
#            v = [key, value]
#            v1 = " ".join( repr(e) for e in v )
#            writer.writerow(v)


#Iterate over the for loop
for key, value in dict1.items():
    print(key[:], value)

