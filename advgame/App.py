import zoro
import luffy
import random
import sys
import time

def print_slow(str):
    for char in str:
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()


def story():
    username = input("Welcome to Athena's Fortune. The quest all the pirate's have been searching for decades.\nEnter your name,Pirate:")
    print("Most of the pirates have been searching for the treasure as it will also crown as the Pirate King.")

    print("By the way I'm your Navigator.We don't have so much time to waste,Captain",username,'.')
    print("Let's pick up your Quartermaster.")
    print("You have two choices.\nZoro or Luffy")
    zoro.zoro()
    luffy.luffy()
    choice = input("Pick your companion(1/2):")

    if choice == '1':
        print("Quartermaster Zoro is ready for the fortune.")
    elif choice == '2':
        print("Quartermaster Luffy is ready for the fortune")
    else:
        print("Please check your input.")

    print("Now as a crew, we need to defeat the Mighty,King of the Pirates,Captain Roger to get atleast a probablity\nto conquer the Athena's Treasure")
    print("Inorder to defeat him we need to defeat his vice captain Silvers Rayleigh and his crew lead Shanks")
    print("Silvers Rayleigh!The complete ocean fears when they hear his name.")
    print("Challenge level 1 Starts!")
    print("K.O")
    def diceroll():
     m = []
     k = random.randint(1, 6) + random.randint(1, 6)
     m.append(k)
     if k in range(2,3):
        print_slow("Critical loss!Sorry Captain we've failed the fortune.")
        return False
     elif k in range(4,7):
        print_slow("Sorry Captain we've lost the fortune.")
        return False
     elif k in range(8,10):
        print("We've won the challenge,Captain.")
        return True
     else:
        print("What a win,Captain!")
        return True
        

    if diceroll() == True:
        print("Next up is the strongest man on the sea,Shanks!\nThe man that can even kill 2 sharks at a time.")
        print("Challenge Level 2 Starts!")
        print("K.O")
        if diceroll() == True:
            print("We've conquered the armies of Captain Roger, now we've the pirate king himself. ")
            print("Well we should start preparing ourself to defeat him rather than praising him.")
            print("Challenge Level 3 and Final Challenge Starts")
            print("K.O")
            if diceroll() == True:
                print("Congratulations captain!")
                print("We now have a possibility to find the Athena's Treasure.")
                print("There must be something that can lead us to the Treasure let's search the whole ship,Captain")
                if choice == '1':
                    print("Ah, yes our Quartermaster Zoro has found a scroll on Roger's Cabinet.")
                else:
                    print("Ah, yes our Quartermaster Luffy has found a scroll on Roger's Cabinet.")

                print('“Don''t seek for the treasure. If you seek it, you wont find it, because the thing you are seeking for is right in front of you."')
                right = input("What does that mean? Do you have any idea, Captain?:")
                right.islower()
                if right == 'ship':
                        print("Yes! We've found the treasure!")
                        print("Oh Yeah I've got it it's the ship itself!")
                        print("*******They find the hidden precious treasure in the ship.********")
                        print("*******Captain", username,"got crowned as the Pirate King.********")
                        print("Game Over.")
                else:
                        print("Oh Yeah I've got it it's the ship itself!")
                        print("*******They find the hidden precious treasure in the ship.********")
                        print("*******Captain", username,"got crowned as the Pirate King.********")
                        print("Game Over.")
                return
                
            
              
    else :
        print("Game Over.")
        return 
