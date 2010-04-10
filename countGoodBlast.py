

import sys

#Open input file

file = sys.argv[1]
input1 = open(file)
#input2 = open(file)

inputs = input1.readlines()
#affy = input2.readlines()

#open output file
output = open(file + ".clean","w")

C = 0
total = ""
hits = 0

for i in inputs:
    k = i.strip()
    k = k.split(" ")
    if k[-1] == "Value":
        #print inputs[C-11]
        hits = hits+1
        output.write( "\n" )
        output.write( inputs[C-11] )
        output.write( inputs[C+2] )
        if inputs[C+3].strip().split("|")[0] == "ref":
            output.write( inputs[C+3] )
        if inputs[C+4].strip().split("|")[0] == "ref":
            output.write( inputs[C+4] )
        if inputs[C+5].strip().split("|")[0] == "ref":
            output.write( inputs[C+5] )                        
        if inputs[C+6].strip().split("|")[0] == "ref":
            output.write( inputs[C+5] ) 
        if inputs[C+7].strip().split("|")[0] == "ref":
            output.write( inputs[C+5] ) 
        if inputs[C+8].strip().split("|")[0] == "ref":
            output.write( inputs[C+5] ) 
        if inputs[C+9].strip().split("|")[0] == "ref":
            output.write( inputs[C+5] ) 
        if inputs[C+10].strip().split("|")[0] == "ref":
            output.write( inputs[C+5] ) 
        if inputs[C+11].strip().split("|")[0] == "ref":
            output.write( inputs[C+5] ) 
        if inputs[C+12].strip().split("|")[0] == "ref":
            output.write( inputs[C+5] ) 
        if inputs[C+13].strip().split("|")[0] == "ref":
            output.write( inputs[C+5] ) 
        if inputs[C+14].strip().split("|")[0] == "ref":
            output.write( inputs[C+5] ) 
        if inputs[C+15].strip().split("|")[0] == "ref":
            output.write( inputs[C+5] ) 
    
    C = C+1
    
print "Total Hits: ", hits
output.write ( "\nTotal Hits: " +  str(hits) )
