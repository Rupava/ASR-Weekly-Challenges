from prettytable import PrettyTable
import time

# SY03,TY05,SY07,TY08,SY02,TY14,SY04,SY15,TY04,SY11,TY09,SY16,SY17
# list iterate not using index 

data = input("Please Insert Attendence: ").replace(" ","")
present = data.split(",")

start_time = time.time()

sy = []
ty = []
sy_final = []
ty_final = []
diff = 0

for item in present:
    if item[0] == 'S':
        sy.append(item)

    if item[0] == 'T':
        ty.append(item)

sy.sort()
ty.sort()

sfc = int(sy[0].replace("SY",""))
tfc = int(ty[0].replace("TY",""))
lfc = min(sfc,tfc)

#############################################################

for i in range(len(sy)):
    ns = int(sy[i].replace("SY",""))
    os = int(sy[i-1].replace("SY",""))

    if i == 0:
        x = lfc
        if ns != lfc: 
            while ns != x:
                sy_final.append("Absent")
                x+=1
        sy_final.append(sy[i])
    
    diff = ns - os

    if diff > 1:
        for x in range(1,diff):
            sy_final.append("Absent")

    if i > 0:
        sy_final.append(sy[i])

#############################################################

for i in range(len(ty)):
    ns = int(ty[i].replace("TY",""))
    os = int(ty[i-1].replace("TY",""))
    
    if i == 0:
        x = lfc
        if ns != lfc: 
            while ns != x:
                ty_final.append("Absent")
                x = x+1
        ty_final.append(ty[i])

    diff = ns-os

    if diff > 1:
        for x in range(diff - 1):
            ty_final.append("Absent")

    if i > 0:
        ty_final.append(ty[i])

#############################################################

if len(sy_final) > len(ty_final):
    while len(sy_final) != len(ty_final):
        ty_final.append("Absent")
else:
    while len(sy_final) != len(ty_final):
        sy_final.append("Absent")

#############################################################

myTable = PrettyTable(["SY_Attendence","TY_Attendence"])

for i in range(len(sy_final)):
    myTable.add_row([sy_final[i],ty_final[i]])

print(myTable)
print("--- %s seconds ---" % (time.time() - start_time))
