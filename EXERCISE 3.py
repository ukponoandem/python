#COUNTING MATCHING ITEMS

COUNTING_ITEMS = [2,3,4,4,4,3,1,6,5,9,15,5,6,12,1,10,]
USER_COUNTER = int(input("ENTER A VALUE: "))
COUNT = 0
for COUNTER in COUNTING_ITEMS:
    if COUNTER == USER_COUNTER:
        COUNT = COUNT+ 1

print(f"TOTAL VALUE", COUNT)