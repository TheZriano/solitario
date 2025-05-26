import os
import random


class Card:
    def __init__(self, value, seed, show=False):
        self.value=value
        self.seed=seed
        self.show=show

seeds=["♠","♡","♣","♢"]
values=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]


deck=[]
scrapsDeck=[]

finaldecks=[[],[],[],[]]

tableau=[
    [],
    [],
    [],
    [],
    [],
    [],
    []
    ]

hand=[]





def screenRefresh(message=""):
    os.system("cls")
    print(f""" SOLITARIO \n\nFai la tua mossa!\n{message}\n """) #Titolo della pagina

    #disegno deck + mano
    print(writeDeckAndHand())
    
    #4 mazzi finali
    print("\nScale:")
    print(writeFinalDecks())

    #tableau 7 mazzi
    print("Tableau:")
    print(writeTableau())


def writeFinalDecks():
    string="""F1)     F2)     F3)     F4)
______  ______  ______  ______\n"""
    for deck in finaldecks:
        if deck==[]:
            string+="|    |  "
            continue
        else:
            card=deck[-1]
            string+=f"|{values[card.value]+(' ' if card.value!=9 else '')} {seeds[card.seed]}|  "
    string+="\n|    |  |    |  |    |  |    |\n"
    for deck in finaldecks:
        if deck==[]:
            string+="|    |  "
            continue
        else:
            card=deck[-1]
            string+=f"|{seeds[card.seed]} {(' ' if card.value!=9 else '')+ values[card.value]}|  "
    string+="\n¯¯¯¯¯¯  ¯¯¯¯¯¯  ¯¯¯¯¯¯  ¯¯¯¯¯¯\n"
    return string

def writeTableau():
    rows=[
        "",
        "",
        "",
        "",
        "",
        ""]
    for i,deck in enumerate(tableau):

        
        if deck==[]:
            rows[0]+=f"{i+1})      "
            rows[1]+="______  "
            rows[2]+="|    |  "
            rows[3]+="|    |  "
            rows[4]+="|    |  "
            rows[5]+="¯¯¯¯¯¯  "
        else:
            rows[0]+=f"{i+1}){' '*(len(deck)*3+3)}"
            for card in deck:
                if card.show:
                    rows[1]+="___"
                    rows[2]+=f"|{values[card.value]+(' ' if card.value!=9 else '')}"
                    rows[3]+="|  "
                    rows[4]+=f"|{seeds[card.seed]} "
                    rows[5]+="¯¯¯"
                else:
                    rows[1]+="___"
                    rows[2]+=f"|▒▒"
                    rows[3]+="|▒▒"
                    rows[4]+=f"|▒▒"
                    rows[5]+="¯¯¯"

            rows[1]+="___  "
            rows[2]+=f" {seeds[card.seed]}|  "
            rows[3]+="  |  "
            rows[4]+=f"{(' ' if card.value!=9 else '')+ values[card.value]}|  "
            rows[5]+="¯¯¯  "

        

    string="\n".join(rows)
    return string
                
def writeDeckAndHand():
    rows=[
        "Mazzo:  Mano:",
        "______  ",
        "|▒▒▒▒|  ",
        "|▒▒▒▒|  ",
        "|▒▒▒▒|  ",
        "¯¯¯¯¯¯  ",
        ]
    for card in hand:
        if card.show:
            rows[1]+="___"
            rows[2]+=f"|{values[card.value]+(' ' if card.value!=9 else '')}"
            rows[3]+="|  "
            rows[4]+=f"|{seeds[card.seed]} "
            rows[5]+="¯¯¯"
        else:
            rows[1]+="___"
            rows[2]+=f"|▒▒"
            rows[3]+="|▒▒"
            rows[4]+=f"|▒▒"
            rows[5]+="¯¯¯"

    rows[1]+="___  "
    rows[2]+=f" {seeds[card.seed]}|  "
    rows[3]+="  |  "
    rows[4]+=f"{(' ' if card.value!=9 else '')+ values[card.value]}|  "
    rows[5]+="¯¯¯  "

    return "\n".join(rows)

def startGame():
    for seed in range(4):
        for value in range(13):
            deck.append(Card(value,seed))
    
    random.shuffle(deck)
    for i in range(7):
        for c in range(i+1):
            tableau[i].append(deck[-1])
            deck.pop(-1)
        tableau[i][-1].show=True

    hand.append(deck[-1])
    deck.pop(-1)
    hand[0].show=True
    screenRefresh()


startGame()

gameOn=True
while gameOn:
    command=input(">>>  ").split(" ")
    match command[0]:
        case "draw":
            hand.append(deck[-1])
            hand[-1].show=True
            deck.pop(-1)
            if len(deck)==0:
                random.shuffle(scrapsDeck)
                deck=scrapsDeck.copy()
                scrapsDeck=[]
            if len(hand)>3:
                hand[0].show=False
                scrapsDeck.append(hand[0])
                hand.pop(0)

        case "move":
            pass

        case _:
            screenRefresh("Mossa non valida!!")
            continue
    screenRefresh()