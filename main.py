from database import Database
from models import Base
from crud import (
    inserir_autor,
    listar_autores,
    excluir_autor,
    inserir_livro,
    listar_livros,
    excluir_livro
)


def menu():
    print("1 - Inserir autor")
    print("2 - Listar autores")
    print("3 - Excluir autor")
    print("4 - Inserir livro")
    print("5 - Listar livros")
    print("6 - Excluir livro")
    print("7 - Alterar banco de dados")
    print("8 - Mostrar conexão atual")
    print("0 - Sair")



def main():
    database = Database()


    if not database.conectar():
        print("Programa encerrado.")
        return

    database.criar_tabelas(Base)

    while True:
        menu()

        opcao = input("Escolha uma opção: ")

        session = database.obter_sessao()

        if session is None:
            print("Nenhum banco conectado.")
            continue

        try:
            if opcao == "1":
                inserir_autor(session)

            elif opcao == "2":
                listar_autores(session)

            elif opcao == "3":
                excluir_autor(session)

            elif opcao == "4":
                inserir_livro(session)

            elif opcao == "5":
                listar_livros(session)

            elif opcao == "6":
                excluir_livro(session)

            elif opcao == "7":
                session.close()

                print("\nAlterando conexão...")

                if database.conectar():
                    database.criar_tabelas(Base)

            elif opcao == "8":
                print(
                    f"\nBanco conectado atualmente: "
                    f"{database.tipo}"
                )

            elif opcao == "0":
                print("\nPrograma encerrado.")
                session.close()
                break

            else:
                print("\nOpção inválida!")

        except ValueError:
            print("\nErro: digite um valor válido.")

        except Exception as erro:
            session.rollback()
            print("\nOcorreu um erro:")
            print(erro)

        finally:
            session.close()


if __name__ == "__main__":
    main()
