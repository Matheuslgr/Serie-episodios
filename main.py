from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
Base = declarative_base()

class Serie(Base):
    __tablename__ = "series"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(100), nullable=False)
    data = Column(Integer, nullable=False)
    genero = Column(String(100), nullable=False)
    nota = Column(Float)

    #relações
    episodios = relationship("Episodio", back_populates="series")

    def __init__ (self, titulo, data, genero, nota ):
        self.titulo = titulo
        self.data = data
        self.genero = genero
        self.nota = nota

    def __repr__(self):
        return (f"series: {self.id} - titulo {self.titulo} - data: {self.data} - genero: {self.genero} - nota: {self.nota}")
    

class Episodio(Base):
    __tablename__ = "episodios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150), nullable=False )
    duracao = Column(String(200), nullable=False)
    avaliacao = Column(Float)
    serie_id = Column(Integer, ForeignKey("series.id"))

    #relacionamento
    series = relationship("Serie", back_populates="episodios")

    
    


    
    def __repr__(self):
        return (f"series: {self.id} - nome {self.nome} - duracao: {self.duracao} - avaliacao: {self.avaliacao}")
    


engine = create_engine("sqlite:///Netflix.db")

Base.metadata.create_all(engine)

Session= sessionmaker (bind= engine)


def cadastrar_serie():
    with Session() as session:
        try:
            titulo_serie = input("Digite o nome da serie: ").capitalize()
            data_serie = input("Digite a data da serie: ")
            genero_serie = input("Digite o genero da serie: ").capitalize()
            nota_serie = float(input("Digite a nota da serie: "))


            serie1 = Serie(titulo=titulo_serie, data=data_serie, genero=genero_serie, nota=nota_serie)
            session.add(serie1)
            session.commit()
            print(f"Serie {titulo_serie} cadastrado com sucesso!")
        except Exception as erro:
            session.rollback()
            print(f"Ocorreu um erro ao cadastrar a serie {erro}")


def cadastrar_ep():
    with Session() as session:
        try:
            nome_serie = input("Digite o nome da serie para cadastrar os episodios:  ").capitalize()
            serie = session.query(Serie).filter_by(titulo = nome_serie ).first()

            if serie == None:
                print(f"Nenhuma serie encontrada com esse nome: {nome_serie} ")
                return
            else:
                nome_ep = input("Digite o nome do episodio: ").capitalize()
                duracao_ep = input(f" Digite a duração do ep  {nome_ep}: ")
                avaliacao_ep = float(input(f" Digite a avaliação do ep {nome_ep}: "))


                ep = Episodio(nome = nome_ep, duracao= duracao_ep, avaliacao=avaliacao_ep,  series = serie)
                #ep.series.append(ep)

                session.add(ep)
                session.commit()
                print(f"episodio {nome_ep} adicionado com sucesso")

        except Exception as erro:
            session.rollback()
            print(f"Ocorreu um erro ao cadastrar a serie {erro}")

cadastrar_ep()