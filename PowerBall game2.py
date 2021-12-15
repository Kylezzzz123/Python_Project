# PowerBall game
import random
#input
count = 1
list = []
while count < 7:
        num_input = int(input(f"Enter your number {count}: "))
        if 0 < num_input <=64 and num_input not in list:
            list.append(num_input)
            count += 1
        else:
            print("Please enter a number bettwen 0 to 64 and do not repeat your previous numbers! ")
print(list)

#random

while True:
    listRandom = []
    for i in range(6):
        print("Please enter to star!", end="\t")
        input()
        ran_number = int(random.randint(1,64))
        if ran_number not in listRandom:
            listRandom.append(ran_number)
            print(listRandom)

    if listRandom == list:
        print(f"Your numbers {listRandom} = Random numbers {listRandom}")
        print("You Win!")
    else:
        print(f"Your numbers {listRandom} ✖  Random numbers {listRandom} ")
        print("See you again!")
    break