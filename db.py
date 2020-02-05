from sqlalchemy import MetaData, create_engine, Table, Column, select, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from flask_serialize import FlaskSerializeMixin


from sqlalchemy.orm import relationship, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lnet_db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# metadata = MetaData()
# # ToDo: do not use check_same_thread
# engine = create_engine('sqlite:///lnet_db', connect_args={'check_same_thread': False}, echo=False)  # echo=False
# Base = declarative_base()
# db_session = sessionmaker(bind=engine)()

def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]

# Table city
class BookDetails(db.Model, FlaskSerializeMixin):
    __tablename__ = 'BookDetails'

    id = Column(Integer, primary_key=True)
    title = Column(String)


class UserRequest(db.Model, FlaskSerializeMixin):

    __tablename__ = 'UserRequest'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer)
    book_title = Column(String)
    email = Column(String)
    timestamp = Column(DateTime)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'book_id': self.book_id,
            'book_title': self.book_title,
            'email': self.email,
            'timestamp': dump_datetime(self.timestamp)
        }

    # @property
    # def serialize_many2many(self):
    #     """
    #     Return object's relations in easily serializable format.
    #     NB! Calls many2many's serialize property.
    #     """
    #     return [item.serialize for item in self.many2many]

# Retrieving data from the database
def get_book_data(book_title="abc"):
    # data = db_session.query(BookDetails)
    return True



data = get_book_data()

