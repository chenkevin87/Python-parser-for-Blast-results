
import sys

#Open input file

file = sys.argv[1]
input1 = open(file)
#input2 = open(file)

inputs = input1.readlines()
#affy = input2.readlines()

#open output file
output = open("n50.txt","a");

C = 0;
total = "";
D = []; #list of # of basepair
eSize = 0;
flag = 0;

for i in inputs:
    if i[0] == ">":
        C = C+1
        D.append(eSize)
        eSize = 0;
    else:
        total = total + i.strip()
        eSize = eSize + len(i.strip())
        
D.remove(0);
D.append(eSize);
print "total number of EST: ", len(D)

D.sort()
D.reverse()

t50 = len(total)/2;
d50 = 0;
dcount = 0;
for i in D:
    d50 = d50 + D[i];
    dcount = dcount + 1;
    if d50 >= t50:
        print "n50", D[dcount], D[dcount+1]
        output.write(file + " " + str(D[dcount+1]) + "\n")
        break;
        

        

#print total
#print "total char: ", len(total)     
#print "total EST: ", C
#print "avarge lenght: ", len(total)/C

print file, " ", len(total), " ", C, " ", len(total)/C
#output.write(file + " " + str(len(total)) + " " + str(C) + " " + str(len(total)/C) + "\n")
