import random

Cchoice=["Rock","Paper","Scissor"]              # list for computer

while True:
        print("ROCK PAPER and SCISSORS GAME:\n")

        youwin,computerwin=0,0

        for i in range(1,6):                    # 5 Round game
                print("ROUND",i,"START:\n")

                print("Please select any one option:")
                print("1.Rock","2.Paper","3.Scissor\n",sep="\n")  # choice any option but in number 1,2,3
                Yourchoice=int(input(""))

                if Yourchoice==1:
                        print("You select : Rock")
                        Yourchoice="Rock"
                elif Yourchoice==2:
                        print("You select : paper")
                        Yourchoice="Paper"
                elif Yourchoice==3:
                        print("You select : scissor")
                        Yourchoice="Scissor"
                else:
                        print("Invalid Choice")
                        break

                Computerchoice=random.choice(Cchoice)  #random select by computer choice
                print("Computer select:",Computerchoice)
                print("\n")

# comparing result and give the point.

                if Yourchoice==Computerchoice:    
                        youwin+=1
                        computerwin+=1
                        print("This Round is Draw\n")
                elif (Yourchoice=="Paper" and Computerchoice=="Rock") or (Yourchoice=="Rock" and Computerchoice=="Scissor") or(Yourchoice=="Scissor" and Computerchoice=="Paper"):
                        youwin+=1
                        print("You win this Round\n")
                else:
                        computerwin+=1
                        print("Computer win this Round\n")

                print("**********\n")

# if your point more than computer then you win and vice versa

        if youwin>computerwin:
                print("CONGRATULATIONS.....You Win the game:\n")
                print("And the Score is:\n" "Your score:",youwin,"and Computer score:",computerwin,sep=" ")
        elif computerwin>youwin:
                print("SO SAD......You Lose the game. Computer win the game:\n")
                print("And the Score is:\n" "Your score:",youwin,"and Computer score:",computerwin,sep=" ")
        else:
                print("Match Draw\n")
                print("And the Score is:\n" "Your score:",youwin,"and Computer score:",computerwin,sep=" ")
        
        print("\n")

        user_choice=input("Want to Play again?(Yes/Exit)")
        if user_choice=='yes' or user_choice=='Yes' or user_choice=='YES':
                continue             
        else:
                print("THANKYOU \nhope you enjoyed.")
                break