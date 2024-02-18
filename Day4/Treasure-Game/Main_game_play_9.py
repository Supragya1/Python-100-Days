while(True):
    choice = input("Do you want to play easy version or hard version of the Treasure game (easy or hard)\n")
    if(choice.lower() == "easy"):
        import Treasure_finding_7
        while(True):
            choice2 = input("Do you want to play the harder version (yes or no)\n")
            if(choice2.lower() == "yes"):
                import Treasure_Map_creation_6
                Treasure_Map_creation_6.map = []
                import Treasure_finding_hard_8
                break
            elif(choice2.lower() == "no"):
                print("Thank you for playing the game")
                break
            else:
                print("Invalid Choice")
                print("Please select the correct choice")
        break
    elif(choice.lower() == "hard"):
        import Treasure_finding_hard_8
        break
    else:
        print("Invalid Choice")
        print("Please select the correct choice")