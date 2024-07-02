user_program = [2,3,4,4,4,5,6]
for user in user_program:
    if user not in user_program:
        user.append(user)
print("the removal",user )
