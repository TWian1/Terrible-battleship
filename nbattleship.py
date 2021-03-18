import random
#prints the board for the game

def printboard(n, f, t):
    print(f + "\n")
    print("\n \n  A B C D E F G H I J")
    for i in range(10):
        string = str(i) + " "
        for k in n[i]:
            if k in ["1", ")", "(", "^", "v"] and t:
                string = string + "0 "
            else:
                string = string + k + " "
        print(string)
def addship(n, t):
    while True:
        o = 0
        shipcoos = []
        ore = random.randint(0, 1)
        if ore == 0:
            x = random.randint(0, 9)
            y = random.randint(0, 10 - n)
        else:
            x = random.randint(0, 10 - n)
            y = random.randint(0, 9)
        if not(t[y][x] in ["1", ")", "(", "^", "v"]):
            for k in range(n):
                if ore == 0:
                    if t[y + k][x] in ["1", ")", "(", "^", "v"]:
                        o = 1
                        break
                else:
                    if t[y][x + k] in ["1", ")", "(", "^", "v"]:
                        o = 1
                        break
        else:
            continue
        if o == 1:
            continue
        for z in range(n):
            if ore == 0:
                if z == 0:
                    t[y + z][x] = "^"
                elif z == n - 1:
                    t[y + z][x] = "v"
                else:
                    t[y + z][x] = "1"
            else:
                if z == 0:
                    t[y][x + z] = "("
                elif z == n - 1:
                    t[y][x + z] = ")"
                else:
                    t[y][x + z] = "1"
        for d in range(n):
            if ore == 0:
                shipcoos.append([str(y + d), str(x)])
            else:
                shipcoos.append([str(y) + str(x + d)])
                
          
        return shipcoos
    
def main():
    v = ""
    m = ""
    #Title
    
    print("\n Battleship!!! \n")
    
    #Makes the board
    
    board = [["0" for i in range(10)] for k in range(10)]
    board2 = [["0" for h in range(10)] for j in range(10)]
    
    #tells addship to add a ship to the board
    
    ship1 = addship(5, board)
    ship2 = addship(4, board)
    ship3 = addship(4, board)
    ship4 = addship(3, board)
    ship5 = addship(3, board)
    ship6 = addship(2, board)
    
    ship7 = addship(5, board2)
    ship8 = addship(4, board2)
    ship9 = addship(4, board2)
    ship10 = addship(3, board2)
    ship11 = addship(3, board2)
    ship12 = addship(2, board2)
    aes = [ship7, ship8, ship9, ship10, ship11, ship12]
    ays = [ship1, ship2, ship3, ship4, ship5, ship6]
    validlet = "ABCDEFGHIJ"
    validnum = "0123456789"
    
        #tells printboard to print the board
    
    printboard(board,  "Your board", False)
    printboard(board2, "\n opponents board", True)
    for j in range(999999):
        Guess = input("\n guess a coordanite: ").upper()
        Aiguessy = random.randint(0, 9)
        Aiguessx = random.randint(0, 9)
        Aiguessxl = validlet[Aiguessx]
        if board[Aiguessy][Aiguessx] in ["0", "s"]:
            m = "Ai missed on " + Aiguessxl + str(Aiguessy)
            board[Aiguessy][Aiguessx] = "s"
        else:
            m = "Ai hit on " + Aiguessxl + str(Aiguessy)
            board[Aiguessy][Aiguessx] = "x"
        if not(len(Guess) == 2):
            print("Invalid Coordanites.\n Try Again...")
            continue
        elif not(Guess[0] in validlet) or not(Guess[1] ):
            print("Invalid Coordanites.\n Try Again...")
        else:
            if board2[int(Guess[1])][validlet.index(Guess[0])] in ["0", "s"]:
                board2[int(Guess[1])][validlet.index(Guess[0])] = "s"
                v = "You missed on " + Guess
            else:
                board2[int(Guess[1])][validlet.index(Guess[0])] = "x"
                v = "You hit on " + Guess
                for u in aes:
                    if [int(Guess[1]), validlet.index(Guess[0])] in u:
                        aes.remove([int(Guess1), validlet.index(Guess[0])])
        print("\n")
        printboard(board, "Your Board", False)
        printboard(board2, "Your Opponents Board", True)
        if len(ship7) == 0:
            print("death to a ship")
        if len(ship8) == 0:
            print("death to a ship")
        if len(ship9) == 0:
            print("death to a ship")
        if len(ship10) == 0:
            print("death to a ship")
        if len(ship11) == 0:
            print("death to a ship")
        if len(ship12) == 0:
            print("death to a ship")
        print(v)
        print(m)
main()