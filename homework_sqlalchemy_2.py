from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, or_, and_
from sqlalchemy.orm import sessionmaker
import requests

"""ACCESSING A TABLE"""
engine = create_engine('sqlite:///homework_sql.db', echo=True)
Base = declarative_base()


class Books(Base):
    """TURNING A DATABASE INTO AN OBJECT"""
    __tablename__ = 'Books'
    books_id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String)
    publisher = Column(String)
    description = Column(String, nullable=False)
    edition = Column(Integer)
    year = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float)

    def __repr__(self) -> str:
        # return f'{self.books_id}, {self.title}, {self.author}, {self.publisher}, {self.description}, {self.edition}, {self.year}, {self.quantity}, {self.price}' # list
        return f'({self.books_id}, {self.title}, {self.author}, {self.publisher}, {self.description}, {self.edition}, {self.year}, {self.quantity}, {self.price})'  # tuple list


"""CREATING A TABLE"""
# Books.__table__.create(engine)

""" FILTERING A COLUMN """


def one(session):
    """ 1. Title and Description of all books written by “J.K. Rowling” """
    results = session.query(Books.title, Books.author).filter_by(
        author='J.K. Rowling').all()
    print(results)


def two(session):
    """ 2. Title, Publisher and Edition of all books printed last decade (in the 2010s) """
    results = session.query(Books.title, Books.publisher,
                            Books.edition, Books.year).filter(Books.year >= 2010).all()
    print(results)


def three(session):
    """ 3. All information about books that are not in stock """
    results = session.query(Books).filter_by(quantity=0).all()
    print(results)


def four(session):
    """ 4. All books in stock without a price """
    results = session.query(Books).filter(Books.price == 0).all()
    print(results)


def five(session):
    """ 5. All books containing the word “Cooking” or “Food”, in stock that were written by either “Gordon Ramsay” or “Jamie Oliver” """
    results = session.query(Books.title, Books.author).filter(and_(Books.quantity != 0, or_(Books.title.like(
        '%Cooking%'), Books.title.like('%Food%'), (Books.author == 'Gordon Ramsay'), (Books.author == 'Jamie Oliver')))).all()
    print(results)


def six(session):
    """ 6. All authors whose name starts with a vowel """
    results = session.query(Books.author).filter(or_(
        Books.author.like('a%'), Books.author.like('e%'), Books.author.like('i%'), Books.author.like('o%'), Books.author.like('u%'))).all()
    print(results)


def seven(session):
    """ 7. All book titles that have the letter “a” at least 3 times in. """
    results = session.query(Books.title).filter(
        Books.title.like('%a%a%a%')).all()
    print(results)


def eight(session):
    """ 8. Book titles composed of exactly 4 characters. """
    results = session.query(Books.title).filter(
        Books.title.like('____')).all()
    print(results)


def nine(session):
    """ 9. Books with the title same as the name of the author """
    results = session.query(Books.title, Books.author).filter(
        Books.title == Books.author).all()
    print(results)


def ten(session):
    """ 10. Books in stock, written by an author whose name does not end with the letter a, with a description that is either empty or has at least 5 characters """
    results = session.query(Books).filter(Books.author.notlike(
        '%a') & (Books.quantity > 0) & ((Books.description == "") | (Books.description.like('_____%')))).all()  # can also use '&' as AND (and_) OPERATOR and '|' as OR (or_) OPERATOR
    for result in results:
        print(result)


def inserting_books(session):
    requested_books = requests.get(
        "https://www.googleapis.com/books/v1/volumes?q=+inauthor:rowling&printType=books")
    books = requested_books.json()
    book_id = int(session.query(Books.books_id).order_by(
        Books.books_id.desc()).first()[0]) + 1
    for each in books['items']:
        """INSERTING INTO TABLE"""
        books = Books(books_id=book_id, title=each['volumeInfo']['title'], author=each['volumeInfo']['authors'][0], publisher="Penguin House", description=str(each['volumeInfo']['description']), edition=1,
                      year=int(each['volumeInfo']['publishedDate'][0:4]), quantity=10, price=(each['saleInfo'].get('retailPrice', {})).get('amount', 0.0))
        book_id += 1
        session.add(books)
        session.commit()


if __name__ == "__main__":
    """STARTING A SESSION"""
    Session = sessionmaker(bind=engine)
    session = Session()

    # one(session)
    # two(session)
    # three(session)
    # four(session)
    # five(session)
    # six(session)
    # seven(session)
    # eight(session)
    # nine(session)
    # ten(session)

    book_id = list(session.query(Books.books_id).order_by(
        Books.books_id.desc()).limit(1)[0])
    print(book_id)
