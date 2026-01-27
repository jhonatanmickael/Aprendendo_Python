# Author: jhonatanmickael
# Description: Find the First Unique Character (Primeiro Caractere Único)
# Challenge by: 'Labs One Bit Code'
# Date: 2026-01-27

def Encontrar_Caracter_Unico(string):

    for caracter in string:

        if string.find(caracter) == string.rfind(caracter):
            return caracter
        
    return ""