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
    episodios = relationship("Episodio", back_populates="serie")

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
    serie = relationship("Serie", back_populates="episodios")

    
    def __init__ (self, nome, duracao, avaliacao ):
        self.nome = nome
        self.duracao = duracao
        self.avaliacao = avaliacao


    
    def __repr__(self):
        return (f"series: {self.id} - nome {self.nome} - duracao: {self.duracao} - avaliacao: {self.avaliacao}")
    


engine = create_engine("sqlite:///Netflix.db")

Base.metadata.create_all(engine)

Session= sessionmaker (bind= engine)


