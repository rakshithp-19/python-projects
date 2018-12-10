import csv 
hypo = ['%','%','%','%','%','%']

with open ('data.csv') as csvfile:
    readcsv = csv.reader(csvfile, delimiter = ',')
    data = []
    print("The given training examples are:")
    for row in readcsv:
        print(row)
        if row[len(row)-1].upper() == 'YES':
            data.append(row)
            
print("The positive training examples are:")
for x in data:
    print(x)
print("\n")

T_E = len(data)
i=0
j=0
k=0
print("Steps of find-s algorithm are:",hypo)
list = []
p=0
d = len(data[p])-1
for j in range(d):
    list.append(data[i][j])
    
hypo = list

i = 1
for i in range(T_E):	
	for k in range(d):
		if hypo[k]!=data[i][k]:
			hypo[k]='?';
			k=k+1;
		
		else:
			hypo[k];
	print(hypo);
i=i+1;
			

    
print("The maximally specific hypothesis is:")
list = []
for i in range(d):
    list.append(hypo[i])
print(list)
    