import random

#defining a function to describe game rules
def play(userNumList,randNum):
    result=[]
    hiddenNumList=list(randNum)
    counter=0
    while(len(result)<4):
        check1=False #Is number present?
        check2=False #Is it in correct place?
        check3=False #Checking the count of a specific number
        if(userNumList[counter] in hiddenNumList):
            check1=True
        if check1==True:    
            if(hiddenNumList[counter]==userNumList[counter]):
                check2=True
        if (userNumList.count(userNumList[counter])> hiddenNumList.count(userNumList[counter])):
            check3=True
        if (check1 and check2):
            result.append("1")
        elif (check1 and (not check2) and (not check3)):
            result.append("0")
        else:
            result.append(".")
        counter +=1
        
    return result

#User plays the game
def game():
    randNum=""

    print("\nNumber to Guess - XXXX")

    #Generating a random number (hidden pegs)
    for x in range(4):
        randNum+=str(random.randint(1,6))

    randNumLst=list(randNum)

    print("\n")
    
    playing=True
    while(playing==True):
        counter=0
        while(True):
            
            inputNum= input(str(counter+1)+"\tEnter a guess : ")
            inputNumLst = list(inputNum)

            #Manual terminatation
            if (inputNum == "0000"):
                print ("Terminated by user!")
                break
        
            #Validating input for a integer
            if not(inputNum.isdigit()):
                print("Please enter a valid input")
                continue
            #Validation input for its length
            if(len(inputNumLst)!=4):
                print("Please enter a 4 digit integer")
                continue

            #Validating input for the range of its elements(1-6)
            for num in inputNumLst:
                if(int(num)>6 or int(num)<1):
                    print("A digit must be between 1-6")
                    break
            else:
                counter+=1
                result=play(inputNumLst,randNum)
                print(result)
                if(result.count('1')==4):
                    print("Congratulations! you won the game..")
                    valid=False
                    while(valid==False):
                        replay= input("Do you want to play another game?(Yes/No) : ")
                        if (replay=="No"):
                            playing=False
                            valid=True
                            break
                            
                        elif (replay=="Yes"):
                            playing=True
                            valid=True
                            game()  #recursively restart the game
                        else:
                            valid=False
                            print("please enter a valid input!")
                elif(counter==8): #number of attempts exceeds
                    print("You lost the game!")
                    valid=False
                    while(valid==False):
                        replay= input("Do you want to play another game?(Yes/No) : ")
                        if (replay=="No"):
                            playing=False
                            valid=True
                            break
                        elif (replay=="Yes"):
                            playing=True
                            valid=True
                            game()
                        else:
                            valid=False
                            print("please enter a valid input!")            
                else:
                    continue
                break               
        break
    
game() #starting the game
     
            
            
            
            
    
    
