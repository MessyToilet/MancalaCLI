import shutil
import os


if __name__ == "__main__":
    gameOn = True
    playerOne = True
    boardAmount = [
        4, 4, 4, 4, 4, 4, 0,
        4, 4, 4, 4, 4, 4, 0,
    ]
    boardChoice = [
        "a", "b", "c", "d", "e", "f"
    ]
    msgs = {0: "\033[1mPlaying...\033[0m", -1: "\033[1mInvalid Tnput!\033[0m", -2: "\033[1mInvalid Choice!\033[0m"}
    msgCode = 0
    while gameOn:
        termWidth = shutil.get_terminal_size().columns
        leftSide = (termWidth // 2) - 20
        padding = " " * leftSide
        
        for i, ele in enumerate(boardAmount):
            ele = int(ele)
            if ele < 10:
                boardAmount[i] = " " + str(ele)
            else: 
                ele = str(ele)

        if playerOne:
            playerTurn = "Player One's"
        else:
            playerTurn = "Player Two's"

        os.system("cls")
        print(f"( \033[1m'q' to QUIT\033[0m )    ( \033[1m{playerTurn} Turn\033[0m )    ( {msgs[msgCode]} )")
        print()

        if not playerOne:
            print(padding + " " * 4, end="")
            for chr in boardChoice:
                print("    " + chr, end="")
            print()
        else:
            print()

        print(f"{padding}+----+----+----+----+----+----+----+----+")
        print(f"{padding}|    | {boardAmount[12]} | {boardAmount[11]} | {boardAmount[10]} | {boardAmount[9]} | {boardAmount[8]} | {boardAmount[7]} |    |")
        print(f"{padding}| {boardAmount[13]} +----+----+----+----+----+----+ {boardAmount[6]} |")
        print(f"{padding}|    | {boardAmount[0]} | {boardAmount[1]} | {boardAmount[2]} | {boardAmount[3]} | {boardAmount[4]} | {boardAmount[5]} |    |")
        print(f"{padding}+----+----+----+----+----+----+----+----+")

        if playerOne:
            print(padding + " " * 4, end="")
            for chr in boardChoice[::-1]:
                print("    " + chr, end="")
            print()
        else:
            print()

        # print(boardChoice)
        # print(boardAmount)

        userChoice = str(input(f"Choice: "))
        
        chosenBin = -1
        if userChoice == 'q':
            gameOn = False
        elif userChoice in boardChoice:
            msgCode = 0
            if playerOne:
                if userChoice == 'a':
                    chosenBin = 5
                elif userChoice == 'b':
                    chosenBin = 4
                elif userChoice == 'c':
                    chosenBin = 3
                elif userChoice == 'd':
                    chosenBin = 2
                elif userChoice == 'e':
                    chosenBin = 1
                elif userChoice == 'f':
                    chosenBin = 0
            else:
                if userChoice == 'a':
                    chosenBin = 12
                elif userChoice == 'b':
                    chosenBin = 11
                elif userChoice == 'c':
                    chosenBin = 10
                elif userChoice == 'd':
                    chosenBin = 9
                elif userChoice == 'e':
                    chosenBin = 8
                elif userChoice == 'f':
                    chosenBin = 7 
        else:
            msgCode = -1

        if userChoice in boardChoice and int(boardAmount[chosenBin]) == 0:
            msgCode = -2

        boardAmount[chosenBin] = 0
        playerOne = not playerOne