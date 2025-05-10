personagens = []

while True:
    nome = input("Nome do personagem: ")
    forca = int(input("Força [1-20]: "))
    agilidade = int(input("Agilidade [1-20]: "))
    inteligencia = int(input("Inteligência [1-20]: "))

    personagens.append({
        'nome': nome,
        'forca': forca,
        'agilidade': agilidade,
        'inteligencia': inteligencia
    })

    continuar = input("Deseja cadastrar outro personagem? (s/n): ")
    if continuar.lower() != 's':
        break