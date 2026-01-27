# Author: jhonatanmickael
# Description: ISBN-10 Validator (Validador de ISBN-10)
# Challenge by: 'Labs One Bit Code'
# Date: 2026-01-27

def verificar_isbn(entrada):

    if len(entrada) != 10:
        return False
    
    if not entrada[:9].isdigit():
        return False

    if not (entrada[-1].isdigit() or entrada[-1] == 'X'):
        return False
   
    list1 = [int(item) if item.isdigit() else 10 for item in entrada]
    multiplica_itens = [item*(indice+1) for indice, item in enumerate(list1)]

    soma_total = sum(multiplica_itens)         
    if soma_total % 11 == 0:
        return True
    else:
        return False       
