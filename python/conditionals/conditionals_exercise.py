# devs_money = 100
# dev_can_play_smash = False
#Here we area ssigning 2 variables and storing the data, 100 and False insed them

# if devs_money > 10 and dev_can_play_smash:
#     print("Dev enter a smash tornament!")
    #Here we a starting an if statement with the conditional being,
    #if devs_money is bigger than 10 and if dev_can_play_smash is True.
# elif devs_money < 10 and dev_can_play_smash:
#     print("Dev is too pour to enter")
    #Here we a starting an if statement with the conditional being,
    #if devs_money is bigger than 10 and if dev_can_play_smash is True.
# else:
#     print("Dev just can't play smash")
    #Now if all the previous conditionals have been False we execute the else statement.


#USING ELID
# mark = input("State mark: ")
# if mark >= "85":
#     print("Distinction")
# elif mark < "85" and mark >= "65":
#     print("Pass")
# else:
#     print("Fail")

#WITHOUT USING ELIF
mark = input("State mark: ")

print("Distinciton" if mark > "85" else "Pass" if mark <= "85" and mark >= "65" else "Fail")