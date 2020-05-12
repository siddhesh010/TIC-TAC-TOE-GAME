import random,sys
print("      |      |      \n","-"*18,"\n      |      |      \n","-"*18,"\n      |      |      \t")
print("-------------------------------------------------------------WELCOME TO TIC-TAC-TOE GAME------------------------------------------------------------------------")
def check_row_win(bot):
    for i in range(0,6,3):
        if (data[i]==data[i+1]==data[i+2]==bot):
            print("{} WON THE GAME :) :) :)".format(bot))
            replay()
                
def check_column_win(bot):
    for i in range(0,3):
        if (data[i]==data[i+3]==data[i+6]==bot):
            print("{} WON THE GAME :) :) :)".format(bot))
            replay()
                
def check_diagonal_win(bot):
    if (data[0]==data[4]==data[8]==bot):
            print("{} WON THE GAME :) :) :)".format(bot))
            replay()
    elif(data[2]==data[4]==data[6]==bot):
             print("{} WON THE GAME :) :) :)".format(bot))
             replay()
            
   
                
def check_tie():
    if len(marked)==8:
        print('THE GAME HAS TIED :) :) :)')
        replay()
            
    
def replay():
    input_=input("DO YOU WISH TO PLAY AGAIN?\nPRESS[y/n] ")
    if input_=='y':
        for i in range(0,9):
            data[i]=''
    else:
        print('EXITING THE GAME :( :( :(')
        sys.exit()


def exit_game():
    input_=input("DO YOU WISH TO EXIT THE GAME?\nPRESS[y/n] ")
    if input_== 'y':
        print('\nEXITING THE GAME :( :( :( ')
        sys.exit()
    
while True:
    mark=input("ENTER YOURE CHOICE:\n'X' OR 'O' ")
    if mark=='o'or mark=='x' or mark=='X' or mark=='0':
        mark=mark.upper()
    else:
        stop=True
        while stop:
            mark=input("PLEASE ENTER A VALID INPUT\n'X' OR 'O' ")
            exit_game()
            if mark=='o'or mark=='x' or mark=='X' or mark=='0':
                mark=mark.upper()
                stop=False
            

    if mark=='X':
        player="X"
        pc="O"
    else:
        pc="X"
        player="O"
        
    o1=''
    o2=''
    o3=''
    o4=''
    o5=''
    o6=''
    o7=''
    o8=''
    o9=''
    data=[o1,o2,o3,o4,o5,o6,o7,o8,o9]

    print("  {}  |  {}  |  {}  \n".format(0,1,2),"-"*15,"\n  {}  |  {}  |  {}  \n".format(3,4,5),"-"*15,"\n  {}  |  {}  |  {}  \t".format(6,7,8))
    print(" The Game will accept your input as shown above")
    print("\n PRESS THE CORRESPONDING KEY TO ENTER YOURE MOVE")

    marked=[]


    
    
    
    
    choice=input("ENTER YOURE MOVE: ")
    if choice in ['0','1','2','3','4','5','6','7','8']:
        choice=int(choice)
        
    else:
        print("ENTER A VALID INPUT")
        exit_game()
        choice=input("ENTER YOURE MOVE: ")
        while not choice in ['0','1','2','3','4','5','6','7','8']:
            choice=input("ENTER YOURE MOVE: ")
            
        
    
        
    while choice in marked:
        print("YOU CANNOT OVERWRITE AN ALREADY MARKED CHOICE")
        exit_game()
        choice=int(input("\nENTER YOURE MOVE:"))
        

    marked.append(choice)
    

    pc_choice=random.randint(0,8)
    while pc_choice in marked:
        pc_choice=random.randint(0,8)
        
    

    
        
    
    for i in range(0,9):
        if i==choice:
            data[i]=player
            
    for i in range(0,9):
        if i==pc_choice:
            data[i]=pc
            
    check_diagonal_win(player)
    check_diagonal_win(pc)
    check_row_win(player)
    check_row_win(pc)
    check_column_win(player)
    check_column_win(pc)
    check_tie() 
        
    #board=print("  {}  ||  {}  \n".format(data[0],data[1],data[2]),"-"*15,"\n  {}  |  {}  |  {}  \n".format(data[3],data[4],data[5]),"-"*15,"\n  {}  |  {}  |  {}  \t".format(data[6],data[7],data[8]))
    print("  {}  |  {}  |  {}  \n".format(data[0],data[1],data[2]),"-"*15,"\n  {}  |  {}  |  {}  \n".format(data[3],data[4],data[5]),"-"*15,"\n  {}  |  {}  |  {}  \t".format(data[6],data[7],data[8]))

        
        

