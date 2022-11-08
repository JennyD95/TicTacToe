# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

field=[[0,0,0],[0,0,0],[0,0,0]]
# Press the green button in the gutter to run the script.

def draw():


    fieldString= "x\y 0 1 2\n"
    for x in range(3):
        fieldString+="  "+str(x)+" "
        for y in range(3):
            if y==1:
                fieldString+="|"

            if field[x][y]==0:
                fieldString+=" "
            elif field[x][y]==1:
                fieldString+="x"
            else: fieldString += "o"

            if y==1:
                fieldString+="|"

        if x!=2:
            fieldString +="\n    _____\n"


    print(fieldString)

def hasWon(player):
    win= False;

    for x in range(3):

        winY= True
        winX=True

        for y in range(3):
            if(field[x][y]!=player):
                winY=False
            if (field[y][x] != player):
                winX = False
        if winY or winX:
            draw()
            print("Spieler "+ str(player)+ " hat gewonnen!")
            return True

    if (field[0][0]==player and field[1][1]==player and field[2][2]==player) or (field[0][2]==player and field[1][1]==player and field[0][2]):
        draw()
        print("Spieler " + player + " hat gewonnen!")
        return True

    else: return False

def setTurn(player):

    while(True):
        try:
            x=int(input("\nSpieler"+ str(player)+" setze x:"))
            y= int(input("\nSpieler"+ str(player) +" setze y:"))
            if 2<x or 2<y or 0>x or 0>y:
                raise ValueError
            if(field[y][x]!=0):
                raise ValueError




        except ValueError:
            print("Die Eingabe war ungueltig. Bitte setze Sie einen Wert von 0-2 in die freien Felder.")

        else:
            field[y][x] = player
            break;


if __name__ == '__main__':
    win= False
    i=0
    while win==False:
        draw()
        setTurn(i%2+1)
        win=hasWon(i%2+1)
        i=i+1





# See PyCharm help at https://www.jetbrains.com/help/pycharm/




