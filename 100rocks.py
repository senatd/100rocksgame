from multiprocessing.managers import ValueProxy


popo = [0] * 100
loser = []

while len(popo) > 0: 

    while len(popo) >= 1:
        try:
            user1 = int (input ("[USER 1] how many rocks would you like to pick?: ")) 
        except ValueError:
            print("Please enter a valid integer")    
            continue       
        if user1 <= 6 and user1 <= len(popo):
            loser.append("USER 1")
            for x in range(user1):
                popo.pop()             
            break    
        elif user1 > 6:
                print("you can not pick a number that is larger than 6!")
                continue
        elif user1 > len(popo):
                print("there are only {} rocks left".format(len(popo)))
                continue
        else:
            print("enter and integer that is greater than 6")
            continue


    while len(popo) >= 1:
        try:
            user2 = int (input ("[USER 2] how many rocks would you like to pick?: "))
        except ValueError:
            print("Please enter a valid integer")    
            continue                  
        if user2 <= 6 and user2 <= len(popo):
            loser.append("USER 2")
            for x in range(user2):
                popo.pop()         
            break
        elif user2 > 6:
            print("you can not pick a number that is larger than 6!")
            continue

        elif user2 > len(popo):
            print("there are only {} rocks left".format(len(popo)))
            continue
        else:
            print("enter and integer that is greater than 6")
            continue

print("YOU LOST", loser[-1])
