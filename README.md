# Nome Dupla - Matheus/Paulo
# Série - Episodios 

# 📺 Sistema de Gerenciamento de Séries e Episódios

## 📖 1. Descrição do Tema

Este projeto consiste em um sistema simples de gerenciamento de **séries e episódios**, desenvolvido em Python utilizando **SQLAlchemy** como ORM e **SQLite** como banco de dados.

O objetivo é permitir que o usuário cadastre séries, adicione episódios vinculados a essas séries e realize operações de consulta, atualização e remoção de dados, simulando um pequeno catálogo no estilo de plataformas de streaming.

---

## 🔗 2. Explicação do Relacionamento 1:N

O sistema utiliza um relacionamento do tipo **um-para-muitos (1:N)** entre as entidades:

* Uma **série** pode possuir vários episódios
* Um **episódio** pertence a apenas uma série

### Como isso foi implementado:

* Na classe `Serie`:

```python
episodios = relationship("Episodio", back_populates="series")
```

* Na classe `Episodio`:

```python
serie_id = Column(Integer, ForeignKey("series.id"))
series = relationship("Serie", back_populates="episodios")
```

### Funcionamento:

* A chave estrangeira (`serie_id`) conecta cada episódio a uma série
* O SQLAlchemy gerencia automaticamente a navegação entre os objetos:

  * `serie.episodios` → lista de episódios da série
  * `episodio.series` → série associada ao episódio

---

## 🔍 3. Explicação das Consultas

O sistema utiliza consultas com o SQLAlchemy através de sessões (`Session`).

### 🔎 Buscar série pelo nome:

```python
session.query(Serie).filter_by(titulo=nome_serie).first()
```

Retorna a primeira série encontrada com o título informado.

---

### 📋 Listar todas as séries:

```python
session.query(Serie).all()
```

Retorna todas as séries cadastradas no banco.

---

### 🔗 Acessar episódios de uma série:

```python
for episodio in serie.episodios:
```

Utiliza o relacionamento 1:N para acessar os episódios vinculados.

---

### ❌ Deletar registros:

```python
session.delete(objeto)
session.commit()
```

Remove uma série ou episódio do banco.

---

### ✏️ Atualizar dados:

Os dados são modificados diretamente no objeto:

```python
serie.titulo = "Novo Nome"
session.commit()
```

---

## ⚙️ 4. Como Executar o Projeto

### 1. Instale o SQLAlchemy:

```bash
pip install sqlalchemy
```

### 2. Execute o arquivo Python:

```bash
python seu_arquivo.py
```

### 3. O banco será criado automaticamente:

* `Netflix.db`

### 4. Utilize as funções disponíveis no código:

* `cadastrar_serie()`
* `cadastrar_ep()`
* `listar_series()`
* `atualizar_serie()`
* `atulizar_episodio()`
* `deletar_serie()`
* `deletar_episodio()`

---

