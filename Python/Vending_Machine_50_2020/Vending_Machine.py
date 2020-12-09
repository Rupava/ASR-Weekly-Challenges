import time

tea =["","ginger","masala","green"]
coffee =["","milk","filter","espresso"]
drinks =["","pepsi","coke","sprite"]

choice = input("State Choice: ")
start_time = time.time()

if choice[0] == "T":
    ch = int(choice[1])
    if ch >= len(tea):
        print("Invalid Choice")
    else:
        print(tea[ch])
if choice[0] == "C":
    ch = int(choice[1])
    if ch > len(coffee):
        print("Invalid Choice")
    else:
        print(coffee[ch])
if choice[0] == "D":
    ch = int(choice[1])
    if ch > len(drinks):
        print("Invalid Choice")
    else:
        print(drinks[ch])

print("--- %s seconds ---" % (time.time() - start_time))