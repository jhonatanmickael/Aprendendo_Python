while True:
    input_user = input("""Digite um número para verificar se é primo:\n Digite Break para fechar o progama\n >>> """).strip().lower()

    if input_user == "break":
        print("Fechando progama")
        break
    else:
      input_user = int(input_user)

    list_division = [str(division) for division in range(1, (input_user+1)) if input_user % division == 0]

    if input_user == 1:
        print("O número 1 não é primo porque não é maior que 1.")
    elif len(list_division) == 2:
        print(f"O número {input_user} é primo porque só é divisível por {",".join(list_division[:-1])} e {list_division[-1]}.")
    else:
        print(f"O número {input_user} não é primo porque é divisível por {",".join(list_division[:-1])} e {list_division[-1]}.")
