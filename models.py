from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Autor(Base):
    __tablename__ = "autores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False)
    idade = Column(Integer, nullable=False)
    nacionalidade = Column(String(50), nullable=False)

    livros = relationship(
        "Livro",
        back_populates="autor",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return (
            f"Autor(id={self.id}, nome='{self.nome}', "
            f"email='{self.email}', idade={self.idade}, "
            f"nacionalidade='{self.nacionalidade}')"
        )


class Livro(Base):
    __tablename__ = "livros"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(150), nullable=False)
    ano = Column(Integer, nullable=False)
    genero = Column(String(50), nullable=False)
    preco = Column(Float, nullable=False)

    autor_id = Column(Integer, ForeignKey("autores.id"), nullable=False)

    autor = relationship("Autor", back_populates="livros")

    def __repr__(self):
        return (
            f"Livro(id={self.id}, titulo='{self.titulo}', "
            f"ano={self.ano}, genero='{self.genero}', "
            f"preco={self.preco}, autor_id={self.autor_id})"
        )
