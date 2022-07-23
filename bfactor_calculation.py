import re
import math

#ATOM      2  CA  ARG A   1      -7.776   3.484  12.790  1.00  1.79           C

pattern=r"ATOM\s+\d+\s+(\w+)\s+\w+\s+\w+\s+(\d+)\s+(-*\d+\.*\d*)\s+(-*\d+\.*\d*)\s+(-*\d+\.*\d*)\s+(-*\d+\.*\d*)\s+(-*\d+\.*\d*)\s+\w+"

inputfile=open("Bfactor.pdb","r")
outputfile=open("Bfactor_nm.xvg","w")

for data in inputfile.readlines():
    #print(data)
    if re.search(pattern,data):
        print(data)
        res=re.search(pattern,data).groups()[1]
        Bfac=float(re.search(pattern,data).groups()[6])/10 #converting to nanometers
        atom=re.search(pattern,data).groups()[0]
        
        if atom == "CA":
            outputfile.write("%d\t%f\n"%(int(res),math.sqrt((3*Bfac)/math.pow((8*math.pi),2))))
        

