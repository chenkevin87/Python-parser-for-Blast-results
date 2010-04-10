

import sys

#Open input file

file = sys.argv[1]
outfile = sys.argv[2]

input1 = open(file)
input2 = open(outfile)

inputs = input1.readlines()
outy = input2.readlines()

#open output file
output = open("totalE_out_rna.txt","w")

C = 0
total = ""
hits = 0
bin_1 = 0
bin_2 = 0
bin_3 = 0
bin_4 = 0
bin_5 = 0
bin_6 = 0
bin_7 = 0
bin_8 = 0
bin_9 = 0
bin_10 = 0
bin_11 = 0
bin_12 = 0
bin_13 = 0
bin_14 = 0
bin_15 = 0
bin_16 = 0
bin_17 = 0
bin_18 = 0
bin_19 = 0
bin_20 = 0
bin_21 = 0



for i in inputs:
    k = i.strip()
    k = k.split("|")
    if k[0] == "ref":
        e = i.strip().split(" ")
        e = e[-1].split("e")
        #print e[-1]
        if e[-1].find(".") >= 1:
            s = float(e[-1])
            if s >= 0.01:
                bin_2 = bin_2 + 1
            elif s < 0.01:
                bin_3 = bin_3 + 1                
        elif e[-1] == "-04":
            bin_4 = bin_4 + 1
        elif e[-1] == "-05":
            bin_5 = bin_5 + 1
        elif e[-1] == "-06":
            bin_6 = bin_6 + 1
        elif e[-1] == "-07":
            bin_7 = bin_7 + 1        
        elif e[-1] == "-08":
            bin_8 = bin_8 + 1
        elif e[-1] == "-09":
            bin_9 = bin_9 + 1
        elif e[-1] == "-10":
            bin_10 = bin_10 + 1
        elif e[-1] == "-11":
            bin_11 = bin_11 + 1        
        elif e[-1] == "-12":
            bin_12 = bin_12 + 1
        elif e[-1] == "-13":
            bin_13 = bin_13 + 1
        elif e[-1] == "-14":
            bin_14 = bin_14 + 1
        elif e[-1] == "-15":
            bin_15 = bin_15 + 1
        elif e[-1] == "-16":
            bin_16 = bin_16 + 1        
        elif e[-1] == "-17":
            bin_17 = bin_17 + 1
        elif e[-1] == "-18":
            bin_18 = bin_18 + 1
        elif e[-1] == "-19":
            bin_19 = bin_19 + 1
        elif e[-1] == "-20":
            bin_20 = bin_20 + 1
        else:
            bin_21 = bin_21 + 1
            


print "bin_2 : ", bin_2
print "bin_3 : ", bin_3
print "bin_4 : ", bin_4
print "bin_5 : ", bin_5
print "bin_6 : ", bin_6
print "bin_7 : ", bin_7
print "bin_8 : ", bin_8
print "bin_9 : ", bin_9
print "bin_10 : ", bin_10
print "bin_11 : ", bin_11
print "bin_12 : ", bin_12
print "bin_13 : ", bin_13
print "bin_14 : ", bin_14
print "bin_15 : ", bin_15
print "bin_16 : ", bin_16
print "bin_17 : ", bin_17
print "bin_18 : ", bin_18
print "bin_19 : ", bin_19
print "bin_20 : ", bin_20
print "bin_21 : ", bin_21

old = []
for i in outy:
    old.append(i.strip())


output.write( old[0] + "\t" + file + "\n")
output.write( old[1] + "\t" + str( bin_2) + "\n" )
output.write( old[2] + "\t" + str( bin_3) + "\n" )
output.write( old[3] + "\t" + str( bin_4) + "\n" )
output.write( old[4] + "\t" + str( bin_5) + "\n" )
output.write( old[5] + "\t" + str( bin_6) + "\n" )
output.write( old[6] + "\t" + str( bin_7) + "\n" )
output.write( old[7] + "\t" + str( bin_8) + "\n" )
output.write( old[8] + "\t" + str( bin_9) + "\n" )
output.write( old[9] + "\t" + str( bin_10) + "\n" )
output.write( old[10] + "\t" + str( bin_11) + "\n" )
output.write( old[11] + "\t" + str( bin_12) + "\n" )
output.write( old[12] + "\t" + str( bin_13) + "\n" )
output.write( old[13] + "\t" + str( bin_14) + "\n" )
output.write( old[14] + "\t" + str( bin_15) + "\n" )
output.write( old[15] + "\t" + str( bin_16) + "\n" )
output.write( old[16] + "\t" + str( bin_17) + "\n" )
output.write( old[17] + "\t" + str( bin_18) + "\n" )
output.write( old[18] + "\t" + str( bin_19) + "\n" )
output.write( old[19] + "\t" + str( bin_20) + "\n" )
output.write( old[20] + "\t" + str( bin_21) + "\n\n" )



