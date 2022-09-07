tot3 = "1", "2", "3"
tot8 = "4", "5", "6", "7", "8"
hoger8 = "9", "10", "11", "12", "13"
invalid = "sorry dat snap ik niet"

def bollen1():
    print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar Vanille ijs is.")
    bollen1 = input("Hoeveel bolletjes wilt u? \n")
    if bollen1 == tot3:
        stap2()
    else:
        vervolg1()

def vervolg1():
    bollen2 = input("ik verstond het niet goed dus ik vraag het nogmaals. Hoeveel bolletjes wilt u? \n")
    if bollen2 == tot8:
        print("dan krijgt u van mij een bakje met", bollen2, "bolletjes")
    else:
        vervolg2

def vervolg2():
    bollen3 = input("sorry hoeveel bolletjes zei je? \n")
    if bollen3 == hoger8:
          print("Sorry, zulke grote bakken hebben we niet")

def stap2():
    bakhoorn = input("""wilt u het in
    a. bakje
    b. hoorntje""")
    if bakhoorn == "a":
        return
    elif bakhoorn == "b":
        return  
    else:
        invalid
        tot3 = "1", "2", "3"
tot8 = "4", "5", "6", "7", "8"
hoger8 = "9", "10", "11", "12", "13"
invalid = "sorry dat snap ik niet"

def bollen1():
    print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar Vanille ijs is.")
    bollen1 = input("Hoeveel bolletjes wilt u? \n")
    if bollen1 == tot3:
        stap2()
    else:
        vervolg1()

def vervolg1():
    bollen2 = input("ik verstond het niet goed dus ik vraag het nogmaals. Hoeveel bolletjes wilt u? \n")
    if bollen2 == tot8:
        print("dan krijgt u van mij een bakje met", + bollen2, "bolletjes")
    else:
        vervolg2

def vervolg2():
    bollen3 = input("sorry hoeveel bolletjes zei je? \n")
    if bollen3 == hoger8:
          print("Sorry, zulke grote bakken hebben we niet")

def stap2():
    bakhoorn = input("""wilt u het in
    a. bakje
    b. hoorntje""")
    if bakhoorn == "a":
        return
    elif bakhoorn == "b":
        return  
    else:
        invalid
bollen1()
vervolg1()
vervolg2()
stap2()



#Stap 1 – van het stappen plan voor de werknemer is dat hij/zij vraagd: “Hoeveel bolletjes wilt u?”.
#Aan de hand van het antwoord kunnen er een aantal dingen gebeuren:
 #  A. bij een getal van 1 t/m 3 ga je naar stap 2
  # B. bij een getal van 4 t/m 8 sla je stap 2 over en krijg je de tekst te zien: “Dan krijgt u van mij een bakje met {aantal} bolletjes”
   #C. bij een getal van hoger dan 8 krijg je de tekst te zien “Sorry, zulke grote bakken hebben we niet” en wordt deze stap herhaald
   #D. anders krijg je de tekst te zien: “Sorry dat snap ik niet...” en wordt deze stap herhaald

#Stap 2 – Nu moet de volgende vraag gesteld worden: “Wilt u deze {aantal} bolletje(s) in A) een hoorntje of B) een bakje?”
 #  A. bij een keuze van A of B ga je naar stap 3
  # B. anders krijg je de tekst te zien: “Sorry, dat snap ik niet...” en wordt deze stap herhaald.

#Stap 3 – Als laatste krijg je te zien “Hier is uw {hoorntje/bakje} met {aantal} bolletje(s). Wilt u nog meer bestellen? (Y/N)”
 #  A. bij Y als als antwoord ga je terug naar stap 1 en herhaalt zich het proces
  # B. bij N als als antwoord stopt het programma en krijg je de boodschap: “Bedankt en tot ziens!”
   #C. anders krijg je de tekst te zien: “Sorry, dat snap ik niet...” en wordt deze stap herhaald
aantalbol = 0
verpakkingbol = 0
def start():
    bestellingen(aantalbol)
   
    print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")
def bestellingen(aantalbol):
    aantalbol = int(input("hoeveel bolletjes wil je? \n"))
    if aantalbol == aantalbol <= 4:
        verpakking(aantalbol, verpakkingbol)
    elif aantalbol == aantalbol > 4 and aantalbol <= 8:
        einde(aantalbol, verpakkingbol)
    elif aantalbol == aantalbol > 8:
        print("Sorry, zulke grote bakken hebben we niet")
    else:
        print("sorry dat snap ik niet") + bestellingen(aantalbol)


def verpakking(aantalbol, verpakkingbol):
    bakhoorn = input("wilt u deze", aantalbol, "bolletjes in a. bakje b. hoorntje?\n")
    if bakhoorn == "a":
        einde(verpakkingbol, aantalbol)
    elif bakhoorn == "b":
        einde()
    else:
        print("sorry dat snap ik niet") + verpakking(aantalbol)



def einde(aantalbol, verpakkingbol):
    nogmeer = input("Hier is uw " + str(verpakkingbol, "met" + str(aantalbol, "bolletjes. Wilt u nog meer bestellen (Y/N)")))
    if nogmeer == "Y":
        start(aantalbol, verpakkingbol)
    elif nogmeer == "N":
        print("bedankt en tot ziens")
    else:
        print("sorry dat snap ik niet") + einde(aantalbol, verpakkingbol)

start()



#hieronder versie 2

def verpakking(aantalbol):
    bakhoorn = input("wilt u deze" + str(aantalbol) + "bolletjes in a. bakje b. hoorntje?\n")
    if bakhoorn == "a":
        einde(bakhoorn)
    elif bakhoorn == "b":
        einde(bakhoorn)
    else:
        print("sorry dat snap ik niet")
        verpakking


def einde(aantalbol, bakhoorn):
    print("hier is uw " + bakhoorn + "met" + str(aantalbol) + "bolletje(s)")
    nogmeer = input("wilt u nog meer bestellen   ja/nee\n")
    if nogmeer == "ja":
        start()
    elif nogmeer == "nee":
        print("Bedankt en tot ziens")
    else:
        print("sorry dat snap ik niet")
        einde()
    