import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import Table, MetaData, select, and_, or_
from sqlalchemy.orm import sessionmaker

# engine = create_engine('sqlite:///homework_sql.db', echo=True)
# Base = declarative_base()


# class Books(Base):
#     __tablename__ = 'Books'
#     title = Column(String, nullable=False)
#     author = Column(String)
#     publisher = Column(String)
#     description = Column(String, nullable=False)
#     edition = Column(Integer)
#     year = Column(Integer, nullable=False)
#     quantity = Column(Integer, nullable=False)
#     price = Column(Float)

#     def __repr__(self) -> str:
#         return f'Books {self.name}'

# Books.__table__.create(engine)

engine = create_engine('sqlite:///' + 'C:\Workspace\dbs' +
                       '\Homework_9_db.sqlite', echo=True)
Base = declarative_base()


class Books(Base):
    __tablename__ = 'Books'
    # Books_Id = Column(Integer, primary_key=True)
    Title = Column(String)
    Author = Column(String)
    Publisher = Column(String)
    Description = Column(String)
    Edition = Column(Integer)
    Year = Column(Integer)
    Quantity = Column(Integer)
    Price = Column(Float, primary_key=True)  # wrong :D


def select_author(connection, books_table):
    '''
    1. Title and Description of all books written by “J.K. Rowling”
    '''
    select_books = select(
        [books_table.columns.Title, books_table.columns.Description])
    result = select_books.where(
        books_table.columns.Author == "J.K. Rowling")
    results = connection.execute(result).fetchall()
    return results


def select_books(connection, books_table):
    '''
    2. Title, Publisher and Edition of all books printed last decade (in the 2010s)
    '''
    select_books = select(
        [books_table.columns.Title, books_table.columns.Publisher, books_table.columns.Publisher])
    result = select_books.where(books_table.columns.Year >= 2010)
    results = connection.execute(result).fetchall()
    return results


def select_quantity(connection, books_table):
    '''
    3. All information about books that are not in stock
    '''
    select_books = select([books_table])
    result = select_books.where(books_table.columns.Quantity == 0)
    results = connection.execute(result).fetchall()
    return results


def select_price(connection, books_table):
    '''
    4. All books in stock without a price
    '''
    select_books = select(
        [books_table.columns.Title, books_table.columns.Price])
    result = select_books.where(books_table.columns.Price == '')
    results = connection.execute(result).fetchall()
    return results


def select_word(results):
    '''
    5. All books containing the word “Cooking” or “Food”, in stock that were written by either “Gordon Ramsay” or “Jamie Oliver”
    '''
    list_of_books = []
    for result in results:
        if (result.Author == "Gordon Ramsay") or (result.Author == "Gordon Ramsay") and (result.Quantity != 0) and (("Food" in result.Title) or ("Cooking" in result.Title)):
            list_of_books.append((result.Author, result.Title))
    return list_of_books


def select_vowel(results):
    '''
    6. All authors whose name starts with a vowel
    '''
    list_of_books = ([(result.Author, result.Title)
                      for result in results if result.Author[0].lower() in 'aeiou'])
    return list_of_books


if __name__ == "__main__":
    engine = create_engine(
        'sqlite:///' + 'C:\Workspace\dbs' + '\Homework_9_db.sqlite')
    connection = engine.connect()
    metadata = MetaData()
    books_table = Table('Books', metadata, autoload=True, autoload_with=engine)
    # print(books_table.columns.keys())

    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(Books).all()

    # 1. Title and Description of all books written by “J.K. Rowling”
    # results = select_author(connection, books_table)
    # print(results)

    # 2. Title, Publisher and Edition of all books printed last decade (in the 2010s)
    # results = select_books(connection, books_table)
    # print(results)

    # 3. All information about books that are not in stock
    # results = select_quantity(connection, books_table)
    # print(results)

    # 4. All books in stock without a price
    # results = select_price(connection, books_table)
    # print(results)

    # 5. All books containing the word “Cooking” or “Food”, in stock that were written by either “Gordon Ramsay” or “Jamie Oliver”
    # result = select_word(results)
    # print(result)

    # 6. All authors whose name starts with a vowel
    result = select_vowel(results)
    print(result)

    # 7. All book titles that have the letter “a” at least 3 times in.
