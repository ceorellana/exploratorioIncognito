# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import operator

def rankingXcontinente(archivo, continenteName):
    archivo_continente = open(continenteName.strip() + ".csv", "w")
    archivo_continente.write("pais,no.universidades,continente\n")
    continente = dict()
    orden_paises = []
    with open(archivo) as html_file:
        soup = BeautifulSoup(html_file,'html.parser')
    table_rows = soup.find_all("tr")
    for tr in table_rows:
        print(tr)
        td = tr.find_all('td')
        row = [i.text for i in td]
        if row[2] not in continente.keys():
            continente[row[2]] = 1
        else:
            continente[row[2]] += 1
        orden_paises.append(row[2])
    sorted_x = sorted(continente.items(), key=operator.itemgetter(1),reverse=True)
    for pais in sorted_x:
        print (pais[0],pais[1])
        archivo_continente.write(",".join([pais[0],str(pais[1]),continenteName]) )
        archivo_continente.write("\n")
    archivo_continente.close()

    input("Presione enter para continuar")
    return orden_paises

def overallRankingXcontinente(continenteName,orden_paises):
    archivo = continenteName + "OverallScore.html"
    archivo_continente = open(continenteName.strip() + "_Overall.csv", "w")
    archivo_continente.write("pais,overall,continente\n")
    overalls = []
    with open(archivo) as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')
    table_rows = soup.find_all("tr")
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        if (len(row) == 7):
            overall = (float(row[3]) * .4) + (float(row[4]) * .3) + (float(row[5]) * .15) + (float(row[6]) * .15)
        else:
            overall = (float(row[2]) * .4) + (float(row[3] * .3)) + (float(row[4]) * .15) + (float(row[5]) * .15)
        overalls.append(overall)
    i = 0
    for pais in orden_paises:
        archivo_continente.write(",".join([pais, str(overalls[i]), continenteName]))
        archivo_continente.write("\n")
        i+=1
    archivo_continente.close()

def troubleShooting(numero):
    if numero.isdigit():
        numero = int(numero)
        if (numero>0 and numero<8):
            return True
        else:
            print ("Numero fuera de rango. Escoja una opcion valida")
    else:
        print("Ingrese un numero")
    return False

def imprimirMenu():
    print("---Ranking Paises por Continente---\n"
          "1. Africa\n"
          "2. Asia\n"
          "3. Europa\n"
          "4. Latinoamerica\n"
          "5. Norteamerica\n"
          "6. Oceania\n"
          "7. Salir")
    n = input("Escoja una opcion: ")
    while(troubleShooting(n)!=True):
        n = input("Escoja una opcion: ")
    return n

continentes = ['Africa', 'Asia', 'Europa', 'Latinoamerica', 'Norteamerica', 'Oceania']
opcion = imprimirMenu()
while (opcion != "7"):
    archivo_continente = continentes[int(opcion) - 1] + ".html"
    orden_paises = rankingXcontinente(archivo_continente, continentes[int(opcion)-1])
    overallRankingXcontinente(continentes[int(opcion)-1],orden_paises)
    opcion = imprimirMenu()
print("Cerrando...")