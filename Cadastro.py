def cadastrar_dados():
    nome = input("Digite o nome: ")
    endereço = input("Digite o endereço: "),
    with open("dados.txt", "a") as arquivo:
        arquivo.write(f"{nome};{endereço}\n")
    print("Dados cadastrados com sucesso!")


def ler_dados():
    try:
        with open("dados.txt", "r") as arquivo:
            print("Lista de dados cadastrados :")
            for linha in arquivo:
                dados = linha.strip().split(';')
                if len(dados) == 2:
                    nome, endereco = dados
                    print(f"Nome: {nome}, Endereço: {endereco}")
                else:
                    print("Erro ao ler linha do arquivo:", linha)
    except FileNotFoundError:
        print("Nenhum dado cadastrado ainda.")


def main():
    while True:
        print("\n===== Menu de Opções =====")
        print("1. Cadastrar dados")
        print("2. Ler dados cadastrados")
        print("3. Sair")

        opcao = input("Escolha uma opção:")

        if opcao == "1":
            cadastrar_dados()
        elif opcao == "2":
            ler_dados()
        elif opcao == "3":
            print("Saindo. . .")
            break
        else:
            print("Opção invalida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
