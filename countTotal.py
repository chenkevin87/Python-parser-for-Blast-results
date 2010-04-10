
import sys

#Open input file

file = sys.argv[1]
input1 = open(file)
#input2 = open(file)

inputs = input1.readlines()
#affy = input2.readlines()

#open output file
output = open("stat.txt","a")

C = 0
total = ""

for i in inputs:
    if i[0] == ">":
        C = C+1
    else:
        total = total + i.strip()
        
#print total
#print "total char: ", len(total)     
#print "total EST: ", C
#print "avarge lenght: ", len(total)/C

print file, " ", len(total), " ", C, " ", len(total)/C
output.write(file + " " + str(len(total)) + " " + str(C) + " " + str(len(total)/C) + "\n")
