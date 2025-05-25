import os


class Card:
    def __init__(self, value, seed):
        self.value=value
        self.seed=seed

deck=[]
finaldecks=[[],[],[],[]]
tableau=[[],[],[],[],[],[],[]]
hand=[Card(0,3),Card(1,2),Card(11,0)]
seeds=["♠","♡","♣","♢"]
values=["A","1","2","3","4","5","6","7","8","9","10","J","Q","K"]



def screenRefresh():
    os.system("cls")
    print(""" SOLITARIO """) #Titolo della pagina

    #disegno deck + mano
    print(f"""
______  ______  ______  ______
|▒▒▒▒|  | {values[hand[0].value]}  |  | {values[hand[1].value]}  |  | {values[hand[2].value]}  |
|▒▒▒▒|  |    |  |    |  |    |
|▒▒▒▒|  | {seeds[hand[0].seed]}  |  | {seeds[hand[1].seed]}  |  | {seeds[hand[2].seed]}  |
¯¯¯¯¯¯  ¯¯¯¯¯¯  ¯¯¯¯¯¯  ¯¯¯¯¯¯""")
    #7 mazzi


screenRefresh()