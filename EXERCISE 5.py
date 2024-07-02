#EXERCISE FIVE
USER_LIST = [1,2,3,4,5,6]
empty_list=[]
for i in range(len(USER_LIST)-1,-1,-1):
 empty_list.append(USER_LIST[i])
print("REVERSED LIST",empty_list)


user = [1,2,3,4,5,6,7]
user.sort(reverse=True)
print(user)