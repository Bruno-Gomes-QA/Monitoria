import mysql.connector
from mysql.connector import Error

# Função para conectar ao banco
def conectar():
    try:
        return mysql.connector.connect(
            host='localhost',
            user='brunomgomes',
            password='Monitoria123@',
            database='game_db'
        )
    except Error as e:
        print(f"Erro ao conectar: {e}")
        return None

# Inserir novo personagem
def inserir_personagem(conn):
    print("\n--- Inserir Personagem ---")
    nome = input("Nome do personagem: ").strip()
    classe = input("Classe do personagem: ").strip()
    try:
        nivel = int(input("Nível do personagem: "))
    except ValueError:
        print("❌ Nível deve ser um número inteiro.\n")
        return

    try:
        cursor = conn.cursor()
        sql = "INSERT INTO personagens (nome, classe, nivel) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nome, classe, nivel))
        conn.commit()
        print("\n✅ Personagem inserido com sucesso!\n")
    except Error as e:
        print(f"Erro ao inserir: {e}\n")

# Listar personagens
def listar_personagens(conn):
    print("\n--- Lista de Personagens ---")
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM personagens")
        resultados = cursor.fetchall()

        if not resultados:
            print("📭 Nenhum personagem encontrado.\n")
            return

        for id, nome, classe, nivel in resultados:
            print(f"ID {id} | {nome} ({classe}) - Nível {nivel}")
        print()
    except Error as e:
        print(f"Erro ao listar: {e}\n")

# Atualizar personagem
def atualizar_personagem(conn):
    print("\n--- Atualizar Personagem ---")
    try:
        id = int(input("ID do personagem a atualizar: "))
    except ValueError:
        print("❌ ID inválido.\n")
        return

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM personagens WHERE id = %s", (id,))
        if not cursor.fetchone():
            print("⚠️ Nenhum personagem encontrado com esse ID.\n")
            return

        nome = input("Novo nome: ").strip()
        classe = input("Nova classe: ").strip()
        try:
            nivel = int(input("Novo nível: "))
        except ValueError:
            print("❌ Nível inválido.\n")
            return

        sql = "UPDATE personagens SET nome=%s, classe=%s, nivel=%s WHERE id=%s"
        cursor.execute(sql, (nome, classe, nivel, id))
        conn.commit()
        print("\n🛠️ Personagem atualizado com sucesso!\n")
    except Error as e:
        print(f"Erro ao atualizar: {e}\n")

# Remover personagem
def remover_personagem(conn):
    print("\n--- Remover Personagem ---")
    try:
        id = int(input("ID do personagem a remover: "))
    except ValueError:
        print("❌ ID inválido.\n")
        return

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM personagens WHERE id = %s", (id,))
        if not cursor.fetchone():
            print("⚠️ Nenhum personagem encontrado com esse ID.\n")
            return

        sql = "DELETE FROM personagens WHERE id=%s"
        cursor.execute(sql, (id,))
        conn.commit()
        print("\n❌ Personagem removido com sucesso!\n")
    except Error as e:
        print(f"Erro ao remover: {e}\n")

# Menu principal com conexão reaproveitada
def menu():
    conn = conectar()
    if not conn:
        print("Não foi possível iniciar o sistema.\n")
        return

    try:
        while True:
            print("\n🎮 MENU DO GAME\n")
            print("1 - Inserir personagem")
            print("2 - Listar personagens")
            print("3 - Atualizar personagem")
            print("4 - Remover personagem")
            print("5 - Sair")
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                inserir_personagem(conn)
            elif opcao == "2":
                listar_personagens(conn)
            elif opcao == "3":
                atualizar_personagem(conn)
            elif opcao == "4":
                remover_personagem(conn)
            elif opcao == "5":
                print("\n👋 Até a próxima!\n")
                break
            else:
                print("\n❗ Opção inválida. Tente novamente.\n")
    finally:
        conn.close()

# Iniciar o sistema
if __name__ == "__main__":
    menu()
