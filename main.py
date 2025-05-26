import os
import random

#crea un oggetto Card che abbia un valore (value) un seme (seed) e un valore visibile/nascosto (show)
class Card:
    def __init__(self, value, seed, show=False):
        self.value=value
        self.seed=seed
        self.show=show

#associano simboli a semi e valori numerici
seeds=["♠","♡","♣","♢"]
values=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]



def screenRefresh(message=""):
    #Disegna sulla console tutti i dati (deck, hand, tableau, e finaldecks) cancellando tutto prima
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
    #disegna le scale finali, restituisce la stringa DA STAMPARE
    string="""f1)     f2)     f3)     f4)
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
    #disegna il tableau, restituisce la stringa DA STAMPARE
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
    #disegna il mazzo (carta girata) e le carte della mano, restituisce la stringa DA STAMPARE
    rows=[
        "Mazzo:  Mano:",
        "______  ",
        ("|▒▒▒▒|  "if deck!=[] else "|    |"),
        ("|▒▒▒▒|  "if deck!=[] else "|    |"),
        ("|▒▒▒▒|  "if deck!=[] else "|    |"),
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
    if hand!=[]:
        rows[1]+="___  "
        rows[2]+=f" {seeds[card.seed]}|  "
        rows[3]+="  |  "
        rows[4]+=f"{(' ' if card.value!=9 else '')+ values[card.value]}|  "
        rows[5]+="¯¯¯  "
    else:
        rows[1]+="______  "
        rows[2]+=f"|    |  "
        rows[3]+="|    |  "
        rows[4]+=f"|    |  "
        rows[5]+="¯¯¯¯¯¯  "

    return "\n".join(rows)

def startGame():
    #inizializza i settaggi del gioco mescolando il mazzo e inizializzando il tableau

    global deck
    global scrapsDeck
    global finaldecks
    global tableau
    global hand

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
    #CICLO PRINCIPALE DEL GIOCO
    #ogni input viene diviso e letto come un comando, ogni comando lo schermo si aggiorna
    #se il comando non è valido compare un messaggio di errore

    command=input(">>>  ").split(" ") 

    match command[0]:
        case "draw":
            #Pesca la ultima carta dal mazzo (deck) (indice -1),
            #la aggiunge alla mano (hand),
            #se la mano ha piu di tre carte la prima è messa nella pila degli scarti (scrapsDeck)
            #quando il mazzo è vuoto la pila degli scarti mescolata e diventa il nuovo mazzo
            if deck!=[]:
                hand.append(deck[-1])
                hand[-1].show=True
                deck.pop(-1)
                if len(hand)>3:
                    hand[0].show=False
                    scrapsDeck.append(hand[0])
                    hand.pop(0)
                if len(deck)==0:
                    random.shuffle(scrapsDeck)
                    deck=scrapsDeck.copy()
                    scrapsDeck=[]
            else:
                screenRefresh("Mossa non valida, Mazzo vuoto!")
                continue
            

        case "move":
            if len(command)==3: command.append("1")
            if command[1] in ["hand","1","2","3","4","5","6","7"] and command[2] in ["1","2","3","4","5","6","7","f"] and command[3].isdigit():
                if command[1]=="hand":
                    if hand==[]:
                        screenRefresh("Mossa non valida")
                        continue
                    card=hand[-1]
                    if command[2] in ["1","2","3","4","5","6","7"]:
                        if tableau[int(command[2])-1][-1].value==card.value+1 and tableau[int(command[2])-1][-1].seed%2!=card.seed%2:
                            hand.pop(-1)
                            tableau[int(command[2])-1].append(card)
                        else:
                            screenRefresh("Mossa non valida")
                            continue
                    elif command[2] =="f":

                        if (finaldecks[card.seed]==[] and card.value==0) or finaldecks[card.seed][-1].value==card.value-1:
                            hand.pop(-1)
                            finaldecks[card.seed].append(card)
                        else:
                            screenRefresh("Mossa non valida")
                            continue
                elif command[1] in ["1","2","3","4","5","6","7"]:
                    if len(tableau[int(command[1])-1])>=int(command[3]) and tableau[int(command[1])-1][-int(command[3])].show:
                        cards=tableau[int(command[1])-1][-int(command[3]):]
                    else:
                        screenRefresh("Mossa non valida")
                        continue
                    if command[2] =="f":
                        if len(cards)==1:
                            card=cards[0]
                            if (finaldecks[card.seed]==[] and card.value==0) or finaldecks[card.seed][-1].value==card.value-1:
                                tableau[int(command[1])-1].pop(-1)
                                finaldecks[card.seed].append(card)
                                if tableau[int(command[1])-1]!=[]: tableau[int(command[1])-1][-1].show=True
                            else:
                                screenRefresh("Mossa non valida")
                                continue
                        else:
                            screenRefresh("Mossa non valida")
                            continue
                    elif command[2] in ["1","2","3","4","5","6","7"] and command[2]!=command[1]:
                        if tableau[int(command[2])-1]==[]:
                            tableau[int(command[2])-1].extend(cards)
                            del tableau[int(command[1])-1][-int(command[3]):]
                            if tableau[int(command[1])-1]!=[]: tableau[int(command[1])-1][-1].show=True

                        elif tableau[int(command[2])-1][-1].value==cards[0].value+1 and tableau[int(command[2])-1][-1].seed%2!=cards[0].seed%2:
                            tableau[int(command[2])-1].extend(cards)
                            del tableau[int(command[1])-1][-int(command[3]):]
                            if tableau[int(command[1])-1]!=[]: tableau[int(command[1])-1][-1].show=True
                        else:
                            screenRefresh("Mossa non valida")
                            continue
                    else:
                        screenRefresh("Mossa non valida")
                        continue
                    


                    

            else:
                screenRefresh("Mossa non valida")
                continue

        case "restart":
            startGame()

        case "exit":
            gameOn=False

        case _:
            screenRefresh("Mossa non valida!!")
            continue
    if len(finaldecks[0])==13 and len(finaldecks[1])==13 and len(finaldecks[2])==13 and len(finaldecks[3])==13:
        screenRefresh("HAI VINTO!!")
        gameOn=False
        continue
    screenRefresh()

input("Premi invio per chiudere il gioco! ")