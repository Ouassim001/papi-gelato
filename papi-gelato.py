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

bonh1 = """---------[papi-gelato]---------
            bolletjes   1 x 1.10 = €1.10
            hoorntjes   1 x 1.25 = €1.25
            bakje       0 x 0.75 = €0.00
                                --------+
            totaal                 €2.35"""

bonh2 = """---------[papi-gelato]---------
            bolletjes   2 x 1.10 = €2.20
            hoorntjes   1 x 1.25 = €1.25
            bakje       0 x 0.75 = €0.00
                                --------+
            totaal                 €3.45"""

bonh3 = """---------[papi-gelato]---------
            bolletjes   3 x 1.10 = €3.30
            hoorntjes   1 x 1.25 = €1.25
            bakje       0 x 0.75 = €0.00
                                --------+
            totaal                 €4.45"""

bonh4 = """---------[papi-gelato]---------
            bolletjes   4 x 1.10 = €4.40
            hoorntjes   1 x 1.25 = €1.25
            bakje       0 x 0.75 = €0.00
                                --------+
            totaal                 €5.45"""

bonh5 = """---------[papi-gelato]---------
            bolletjes   4 x 1.10 = €4.40
            hoorntjes   1 x 1.25 = €1.25
            bakje       0 x 0.75 = €0.00
                                --------+
            totaal                 €5.45"""

bonb1 = """---------[papi-gelato]---------
            bolletjes   1 x 1.10 = €1.10
            hoorntjes   0 x 1.25 = €0.00
            bakje       1 x 0.75 = €0.75
                                --------+
            totaal                 €1.85"""

bonb2 = """---------[papi-gelato]---------
            bolletjes   2 x 1.10 = €2.20
            hoorntjes   0 x 1.25 = €0.00
            bakje       1 x 0.75 = €0.75
                                --------+
            totaal                 €2.95"""

bonb3 = """---------[papi-gelato]---------
            bolletjes   3 x 1.10 = €3.30
            hoorntjes   0 x 1.25 = €0.00
            bakje       1 x 0.75 = €0.75
                                --------+
            totaal                 €4.05"""

bonb4 = """---------[papi-gelato]---------
            bolletjes   4 x 1.10 = €4.40
            hoorntjes   0 x 1.25 = €0.00
            bakje       1 x 0.75 = €0.75
                                --------+
            totaal                 €5.15"""

bonb5 = """---------[papi-gelato]---------
            bolletjes   5 x 1.10 = €5.50
            hoorntjes   0 x 1.25 = €0.00
            bakje       1 x 0.75 = €0.75
                                --------+
            totaal                 €6.25"""






invalid = "Sorry dat snap ik niet"
def start():
    print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")
    aantalbol = int(input("hoeveel bolletjes wil je? \n"))
    return aantalbol


def verpakking(aantalbol):
    bakhoorn = input("wilt u deze " + str(aantalbol) + "bolletje(s) in   a. een hoorntje OF  b. een bakje")
    if bakhoorn == "a":
        return "hoorn"
    elif bakhoorn == "b":
        return "bakje"
    return bakhoorn


smaakaantal = ["1", "2", "3", "4", "5", "6", "7", "8"]

def smaak1(bakhoorn):
    smaak1 = input("hoeveel bolletjes wilt u met de smaak aardbei?\n")
    return smaakaantal

def smaak2(bakhoorn):
    smaak2  = input("hoeveel bolletjes wilt u met de smaak chocolade?\n")
    return smaakaantal

def smaak3(bakhoorn):
    smaak3 = input("hoeveel bolletjes wilt u met de smaak munt?\n")
    return smaakaantal

def smaak4(bakhoorn):
    smaak4 = input("hoeveel bolletjes wilt u met de smaak vanille?\n")
    return smaakaantal

def bon(aantalbol, bakhoorn):
    bon = input("""hoeveel bolletjes heb je, en wat voor verpakking heb je gekozen
                    antwoord de vraag net zoals het volgende
                    bijvoorbeeld 3 en bakje of 2 en hoorntje
                    als je niks hebt besteld, typ dan 0\n""")
    if bon == "0":
        start()
    elif bon == "1 en hoorntje":
        print(bonh1)
    elif bon == "2 en hoorntje":
        print(bonh2)
    elif bon == "3 en hoorntje":
        print(bonh3)
    elif bon == "4 en hoorntje":
        print(bonh4)
    elif bon == "5 en hoorntje":
        print(bonh5)
    elif bon == "1 en bakje":
        print(bonb1)
    elif bon == "2 en bakje":
        print(bonb2)
    elif bon == "3 en bakje":
        print(bonb3)
    elif bon == "4 en bakje":
        print(bonb4)
    elif bon == "5 en bakje":
        print(bonb5)
        




def einde(bakhoorn, aantalbol):
    einde = print("hier is uw " +  ( bakhoorn ) + "met " + str (aantalbol ) + " bolletjes" )
    nogmeer = input("wil je nog meer bestellen. ja/nee\n")
    return einde, nogmeer
    

while True:
    begin = start()
    if begin <= 4:
        verpakking(begin)
        
    elif begin > 4:
        einde(begin)
        verpakking(begin)
        
    elif begin < 8:
        einde(begin)
        verpakking(begin)
        
    elif begin > 8:
        print("Sorry, zulke grote bakken hebben we niet")
        start()   
    else:
        invalid

    tweede = smaak1(begin)
    if tweede in smaakaantal:
        smaak2()
    else:
        invalid   

    derde = smaak2(tweede)
    if derde in smaakaantal:
        smaak3(derde)
    
    else:
        invalid

    vierde = smaak3(derde)
    if smaak3 in smaakaantal:
        smaak4(vierde)
    else:
        invalid

    vijfde = smaak4(vierde)
    if vijfde in smaakaantal:
        verpakking(vijfde)
    else:
        invalid


    tweede = verpakking(begin)
    if tweede == "a":
        einde('hoorn',  begin)
        break
    elif tweede == "b":
        einde('bakje', begin)
        break
    else:
        invalid
        

    
    zesde = einde("hoorn", begin)
    if zesde == "":
        einde(zesde)


    


        




start()
verpakking()
smaak1()
smaak2()
smaak3()
smaak4()
bon()
einde()

