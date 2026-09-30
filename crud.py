from models import Autor, Livro


# ==========================
# AUTORES
# ==========================

def inserir_autor(session):
    print("\n===== CADASTRAR AUTOR =====")

    nome = input("Nome: ")
    email = input("E-mail: ")
    idade = int(input("Idade: "))
    nacionalidade = input("Nacionalidade: ")

    autor = Autor(
        nome=nome,
        email=email,
        idade=idade,
        nacionalidade=nacionalidade
    )

    session.add(autor)
    session.commit()

    print(f"\nAutor cadastrado com ID {autor.id}!")


def listar_autores(session):
    print("\n===== LISTA DE AUTORES =====")

    autores = session.query(Autor).all()

    if not autores:
        print("Nenhum autor cadastrado.")
        return

    for autor in autores:
        print(
            f"\nID: {autor.id}"
            f"\nNome: {autor.nome}"
            f"\nE-mail: {autor.email}"
            f"\nIdade: {autor.idade}"
            f"\nNacionalidade: {autor.nacionalidade}"
            f"\nQuantidade de livros: {len(autor.livros)}"
        )


def excluir_autor(session):
    print("\n===== EXCLUIR AUTOR =====")

    try:
        id_autor = int(input("ID do autor: "))
    except ValueError:
        print("ID inválido.")
        return

    autor = session.get(Autor, id_autor)

    if autor is None:
        print("Autor não encontrado.")
        return

    session.delete(autor)
    session.commit()

    print("Autor excluído com sucesso!")


# ==========================
# LIVROS
# ==========================

def inserir_livro(session):
    print("\n===== CADASTRAR LIVRO =====")

    titulo = input("Título: ")
    ano = int(input("Ano: "))
    genero = input("Gênero: ")
    preco = float(input("Preço: "))

    autores = session.query(Autor).all()

    if not autores:
        print("\nNão existem autores cadastrados.")
        print("Cadastre um autor antes de cadastrar um livro.")
        return

    print("\nAutores disponíveis:")

    for autor in autores:
        print(f"{autor.id} - {autor.nome}")

    try:
        autor_id = int(input("ID do autor: "))
    except ValueError:
        print("ID inválido.")
        return

    autor = session.get(Autor, autor_id)

    if autor is None:
        print("Autor não encontrado.")
        return

    livro = Livro(
        titulo=titulo,
        ano=ano,
        genero=genero,
        preco=preco,
        autor=autor
    )

    session.add(livro)
    session.commit()

    print(f"\nLivro cadastrado com ID {livro.id}!")


def listar_livros(session):
    print("\n===== LISTA DE LIVROS =====")

    livros = session.query(Livro).all()

    if not livros:
        print("Nenhum livro cadastrado.")
        return

    for livro in livros:
        print(
            f"\nID: {livro.id}"
            f"\nTítulo: {livro.titulo}"
            f"\nAno: {livro.ano}"
            f"\nGênero: {livro.genero}"
            f"\nPreço: R$ {livro.preco:.2f}"
            f"\nAutor: {livro.autor.nome}"
        )


def excluir_livro(session):
    print("\n===== EXCLUIR LIVRO =====")

    try:
        id_livro = int(input("ID do livro: "))
    except ValueError:
        print("ID inválido.")
        return

    livro = session.get(Livro, id_livro)

    if livro is None:
        print("Livro não encontrado.")
        return

    session.delete(livro)
    session.commit()

    print("Livro excluído com sucesso!")
