import re

pattern= r"\d+\.*\d*\s+(-*\d+\.*\d*)"

InitialPart="""
# Gromacs Runs On Most of All Computer Systems
#
@    title "RMSD"
@    xaxis  label "Time (ps)"
@    yaxis  label "RMSD (nm)"
@TYPE xy
@ subtitle "Protein after lsq fit to C-alpha"""

inputfile=open("LJ.xvg","r")
outputfile=open("LJ_avg.xvg","w")

outputfile.write("%s\n"%InitialPart)

begin=input("Enter the begining frame of the trajectory: ")

end=input("Enter the ending frame of the trajectory: ")


values=[]

for data in inputfile.readlines():
    if re.search("^@|#",data):
        pass
    else:
        if re.search(pattern,data):
            values.append(float(re.search(pattern,data).groups()[0]))
            
print("Length of Values:%d\n"%len(values))
        
for x in range(int(begin),(int(end)-10)):
    
    sum=0.0
    
    for y in values[x:x+10]:
        
        sum=sum+y
        
    avg=float(sum)/10.0
    
    outputfile.write("%f\t%f\n"%((x*0.1),avg))
    
outputfile.close()
inputfile.close()
