import random
import math

MAX_BET = 1000
MIN_BET = 1
RAWS = 3
COLS = 3

szimb_ertekek = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
}

nyeres_ertek = {
    "A" : 4,
    "B" : 3,
    "C" : 2,
}

def nyeres(columns, lines, bet, values):
    nyeremeny = 0
    nyero_sor = []
    for line in range(lines):
        symbol = columns [0][line]
        for column in columns:
            symbol_nezes = column[line]
            if symbol != symbol_nezes:
                break
        else:
            nyeremeny += values[symbol] * bet
            nyero_sor.append(f"{line+1}.")
    return nyeremeny-bet, nyero_sor



def gep(rows, cols, szimbolumok):
    szimb_ertek = []
    for szimb, szimb_ertekek in szimbolumok.items():
        for _ in range(szimb_ertekek):
            szimb_ertek.append(szimb)
    
    columns = []
    for _ in range(cols):
        column = []
        jelenlegi_szimb = szimb_ertek [:]
        for _ in range(rows):
            ertek = random.choice(jelenlegi_szimb)
            jelenlegi_szimb.remove(ertek)
            column.append(ertek)
        columns.append(column)
    return columns



def nyomtat_gep(columns, sorok):
    for row in range(sorok):             #range(len(columns[0])):
        for j, column in enumerate(columns):
            if j != len(columns) -1:
                print(column[row], end =" | ")
            else:
                print(column[row], end ="")
        print()




def deposit():
    while True:
        amount = input("Mennyit akarsz berakni? ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("A mennyiségnek nagyobnak kell lenni mint 0! ")

        else:
            print("Adjon meg számot! ")
    return amount



def sorbol_szam():
    while True:
        lines = input("Hány sorban fogadsz? (1-" + str(RAWS) + ") ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= RAWS:
                break
            else:
                print("írj be számot! (1-" + str(RAWS) + ")")

        else:
            print("Adjon meg számot! ")
    return lines
    


def fogadas(egyenleg,sorok):
    max = egyenleg/sorok
    while True:
        bet = input(f"Mennyiben fogadsz? (max {math.floor(max)}): ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET and bet <= max:
                break
            else:
                print(f"írj be számot {MIN_BET} és {math.floor(max)} között!")

        else:
            print("Adjon meg számot! ")
    return bet



def main():
    egyenleg = deposit()
    while True:
        print(f"jelenlegi egyenleged {egyenleg}")
        valasz = input("press enter to spin (q to quit).")
        if valasz == "q" or egyenleg<=0:
            print(f"Az összes nyereményed: {egyenleg}")
            break

        sorok = sorbol_szam()
        while True:
            bet = fogadas(egyenleg,sorok)
            total_bet = bet * sorok
            if total_bet > egyenleg:
                print("nem jó")
            else: break


        display = gep(RAWS, COLS, szimb_ertekek)
        nyomtat_gep(display, sorok)
        nyeremeny, nyero_sor = nyeres(display, sorok, total_bet, nyeres_ertek )
        if nyeremeny > 0:
            print(f"nyertél: {nyeremeny}")
        else:
            print(f"vesztettél: -{bet*sorok}")
        print(f"nyertél a sorban ", *nyero_sor)
        egyenleg += nyeremeny


main()
