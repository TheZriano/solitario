import os


class Card:
    def __init__(self, value, seed, show=False):
        self.value=value
        self.seed=seed
        self.show=show

deck=[]
finaldecks=[[],[],[],[]]

tableau=[
    [Card(0,3),Card(1,2,show=True),Card(11,0,show=True)],
    [Card(0,3),Card(1,2,show=True),Card(11,0,show=True)],
    [],
    [Card(0,3),Card(1,2,show=True),Card(11,0,show=True)],
    [Card(0,3),Card(1,2,show=True),Card(11,0,show=True)],
    [Card(0,3),Card(1,2,show=True),Card(11,0,show=True)],
    []
    ]

hand=[Card(0,3),Card(1,2),Card(11,0)]
seeds=["♠","♡","♣","♢"]
values=["A","1","2","3","4","5","6","7","8","9","10","J","Q","K"]



def screenRefresh():
    os.system("cls")
    print(""" SOLITARIO """) #Titolo della pagina

    #disegno deck + mano
    print(f"""Mazzo:  Mano:
______  ______  ______  ______
|▒▒▒▒|  | {values[hand[0].value]}  |  | {values[hand[1].value]}  |  | {values[hand[2].value]}  |
|▒▒▒▒|  |    |  |    |  |    |
|▒▒▒▒|  | {seeds[hand[0].seed]}  |  | {seeds[hand[1].seed]}  |  | {seeds[hand[2].seed]}  |
¯¯¯¯¯¯  ¯¯¯¯¯¯  ¯¯¯¯¯¯  ¯¯¯¯¯¯""")
    
    #4 mazzi finali
    print("Scale:")
    print(writeFinalDecks())

    #tableau 7 mazzi
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
            string+=f"|{values[card.value]}  {seeds[card.seed]}|  "
    string+="\n|    |  |    |  |    |  |    |\n"
    for deck in finaldecks:
        if deck==[]:
            string+="|    |  "
            continue
        else:
            card=deck[-1]
            string+=f"|{seeds[card.seed]}  {values[card.value]}|  "
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
                    rows[2]+=f"|{values[card.value]} "
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
            rows[4]+=f" {values[card.value]}|  "
            rows[5]+="¯¯¯  "

        

    string="\n".join(rows)
    return string
                



screenRefresh()

input(">>>  ")