import random
import math

def random_lista():
    random_lista = []
    lista_string = ""

    for i in range(0,12,1):
        szam = math.floor(random.random()*1011-10)
        if i < 11:
            lista_string += str(szam) +"$"
        else:
            lista_string += str(szam)

    random_lista.append(lista_string) 
    return random_lista

def paratlanok_szama(paratlan_lista):
    paratlan_lista = paratlan_lista[0].split("$")
    paratlan_sum = 0

    for i in range(0,len(paratlan_lista),1):
        if int(paratlan_lista[i]) % 2 != 0:
            paratlan_sum += 1

    return paratlan_sum

def konzol_kiir():
    paratlan_kiiras = paratlanok_szama()
    kiiras =f"A páratlanok száma: {paratlan_kiiras}"
    
    return kiiras

def fajlba_kiir():
    kiirando = konzol_kiir()

    fajl = open("kimutatas.txt","w",encoding="utf-8")
    fajl.write(kiirando)
    fajl.close

    