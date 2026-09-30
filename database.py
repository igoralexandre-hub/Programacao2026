import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()


class Database:
    def __init__(self):
        self.engine = None
        self.Session = None
        self.tipo = None

    def conectar_sqlite(self):
        try:
            self.engine = create_engine(
                "sqlite:///av5.db",
                echo=False
            )

            self.Session = sessionmaker(bind=self.engine)
            self.tipo = "SQLite"

            print("\nConectado ao SQLite com sucesso!")
            return True

        except Exception as erro:
            print("\nErro ao conectar ao SQLite:")
            print(erro)
            return False

    def conectar_mysql(self):
        print("\n===== CONECTANDO AO MYSQL =====")

        usuario = os.getenv("MYSQL_USER")
        senha = os.getenv("MYSQL_PASSWORD")
        host = os.getenv("MYSQL_HOST")
        porta = os.getenv("MYSQL_PORT", "3306")

        if not usuario or not senha or not host:
            print("\nErro: configure o arquivo .env.")
            return False

        try:
            # Banco padrão do Aiven
            banco = "defaultdb"

            url = (
                f"mysql+pymysql://{usuario}:{senha}"
                f"@{host}:{porta}/{banco}"
            )

            self.engine = create_engine(
                url,
                echo=False
            )

            # Testa a conexão
            with self.engine.connect():
                pass

            self.Session = sessionmaker(bind=self.engine)
            self.tipo = "MySQL"

            print("\nConectado ao MySQL com sucesso!")
            return True

        except Exception as erro:
            print("\nErro ao conectar ao MySQL:")
            print(erro)

            self.engine = None
            self.Session = None
            self.tipo = None

            return False

    def conectar(self):
        while True:
            print("\n===== ESCOLHA O BANCO =====")
            print("1 - SQLite")
            print("2 - MySQL")
            print("0 - Cancelar")

            opcao = input("Opção: ")

            if opcao == "1":
                if self.conectar_sqlite():
                    return True

            elif opcao == "2":
                if self.conectar_mysql():
                    return True

            elif opcao == "0":
                return False

            else:
                print("Opção inválida!")

    def criar_tabelas(self, Base):
        if self.engine is not None:
            Base.metadata.create_all(self.engine)
            print("Tabelas verificadas/criadas com sucesso!")

    def obter_sessao(self):
        if self.Session is None:
            return None

        return self.Session()
