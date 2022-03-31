from luhn import verify
from random import randint

def gen(bin="4", month="#", year="#", cvv="#"): #Eso de igual quiere decir que si no se proporciona un valor tiene ese por defecto
    i = 0 
    ccs = []
    genMonth = (month == "#") #Si devuelve true será true sino será false
    genYear = (year == "#")
    genCvv = (cvv == "#")

    while(i < 10): #Itero 10 veces el siguiente bucle
        if(genMonth == True): month = str(randint(1, 12)) #Si un if es corto lo puedes reducir a una linea: if(...): orden1; orden2; orden3...
        if(genYear == True): year = str(randint(2022, 2032))
        if(genCvv == True and bin[0] != '3'): cvv = str(randint(111, 999))
        if(genCvv == True and bin[0] == '3'): cvv = str(randint(1111, 9999))

        if(len(month) == 1):
            month = "0" + month

        passed = False #Lo usaré para ver si pasó luhn
        cc = ""

        while(passed == False):
            cc = ccGen(bin) #Uso esta función para separar código
            passed = verify(cc)

        ccs.append(f"{cc}|{month}|{year}|{cvv}")

        i += 1 #Sumo 1 al iterador al final del bucle

    return ccs


def ccGen(bin):
    final_cc = ""
    i = 0

    if(bin[0] != '3'):
        while(i < 16): #La longitud de la cc
            try:
                if(bin[i] == "x"): #Reemplaza las x que encuentre con un número random
                    final_cc += str(randint(0, 9))
                else: #Si no es x se suma el caracter del bin
                    final_cc += bin[i]

            except: #Si trato de buscar 12 y la longitud del bin es de 7 dará un error
                final_cc += str(randint(0, 9)) #Si el caracter no existe solo tengo que sumar un número random

            i += 1
    else:
        while(i < 15): #Mismo proceso para amex
            try:
                if(bin[i] == "x"):
                    final_cc += str(randint(0, 9))
                else: 
                    final_cc += bin[i]

            except:
                final_cc += str(randint(0, 9)) 

            i += 1

    return final_cc

def validateCard(cc):
    try:
        data = cc.split('|')
        if(len(data) < 4):
            return [False, "Bad format in the input"]
        
        cc = int(data[0])
        month = int(data[1])
        year = int(data[2])
        cvv = int(data[3])

        if(verify(str(cc)) == False):
            return [False, "Failed luhn check"]

        if(month < 1 or month > 12):
            return [False, "Invalid month: " + str(month)]
        elif(month < 10):
            month = "0" + str(month)

        if(len(str(year)) == 2):
            year = "20" + str(year)
        elif(len(str(year)) != 4):
            return [False, "Invalid year: " + str(year)]

        if(len(str(cvv)) != 3):
            return [False, "Invalid cvv: " + str(cvv)]

        return [True, str(cc), str(month), str(year), str(cvv)]

    except ValueError:
        return [False, "Some of the data isn´t a number"]   
