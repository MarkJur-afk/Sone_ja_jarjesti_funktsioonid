import random

while True:
    print("Valige funktsioon 1-10")
    print("1. Vaheta suurtähed väikesteks ja vastupidi")
    print("2. Pööra string ümber")
    print("3. Leia stringi pikkus")
    print("4. Vali juhuslik element")
    print("5. Muuda kõik tähed väikesteks")
    print("6. Kontrolli, kas string koosneb ainult numbritest")
    print("7. Kontrolli, kas string koosneb ainult tähtedest")
    print("8. Kontrolli, kas string on palindroom")
    print("9. Muuda string sõnade loendiks")
    print("10. Muuda esimene täht suureks ja ülejäänud väikesteks")
    print("11. Looge list, kus on stringi iga elemendi ruudud")
    print("12. Segage stringi elemendid")
    print("0. Välju programmist")

    answer = input("Sisestage number: ")

    if answer == "1":
        s = input("Sisestage string: ")
        print(s.swapcase())
        print("Funktsioon .swapcase muudab väiketähed suurtähtedeks ja vastupidi.")

    elif answer == "2":
        s = input("Sisestage string: ")
        print(s[::-1])
        print("Funktsioon pöörab stringi ümber.")

    elif answer == "3":
        s = input("Sisestage string: ")
        print(len(s))
        print("Funktsioon tagastab stringi pikkuse.")

    elif answer == "4":
        s = input("Sisestage string: ")
        print(random.choice(s))
        print("Juhusliku elemendi valik.")

    elif answer == "5":
        s = input("Sisestage string: ")
        print(s.lower())
        print("Funktsioon muudab stringi kõik tähed väikesteks.")

    elif answer == "6":
        s = input("Sisestage string: ")
        if s.isdigit():
            print("String koosneb ainult numbritest.")
        else:
            print("String sisaldab muid sümboleid peale numbrite.")

    elif answer == "7":
        s = input("Sisestage string: ")
        if s.isalpha():
            print("String koosneb ainult tähtedest.")
        else:
            print("String sisaldab muid sümboleid peale tähtede.")

    elif answer == "8":
        s = input("Sisestage string: ")
        if s == s[::-1]:
            print("String on palindroom.")
        else:
            print("String ei ole palindroom.")

    elif answer == "9":
        s = input("Sisestage string: ")
        word_list = s.split()
        print(f"String on muudetud sõnade loendiks: {word_list}")

    elif answer == "10":
        s = input("Sisestage string: ")
        print(s.capitalize())
        print("Muudab esimese tähe suureks ja kõik ülejäänud väikesteks.")

    elif answer == "11":
        s = input("Sisestage string: ")
        squares = [x**2 for x in s]
        print(squares)
        print("Funktsioon loob listi, kus on stringi iga elemendi ruudud.")

    elif answer == "12":
        s = input("Sisestage string: ")
        random.shuffle(s)
        print(s)
        print("Funktsioon segab stringi elemendid.")
        
    elif answer == "0":
        print("Väljumine programmist.")
        break

    else:
        print("Vale valik, proovige uuesti.")
