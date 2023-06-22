from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_utils import PasswordType, force_auto_coercion
from sqlalchemy.dialects.mysql import INTEGER

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'

    idpessoa = Column(Integer, primary_key=True)
    registration = Column(String(100, collation='big5'))
    hash_passw = Column(String(1000))
    name = Column(String(200))
    hash_email = Column(String(1000))

class Category(Base):
    __tablename__ = 'category'

    idcategory = Column(Integer, primary_key=True)

    name = Column(String(450))
    desc = Column(String(100))



class Item(Base):
    __tablename__ = 'item'

    idobject = Column(Integer, primary_key=True)
    name = Column(String(45))
    model_color = Column(String(45))
    brand_species = Column(String(45))
    year_acquired = Column(String(45))
    desc = Column(String(45))
    category_idcategory = Column(Integer, ForeignKey('category.idcategory'))
    condition = Column(String(450))
    vaccines = Column(String(450))
    likes = Column(String(450))
    dislikes = Column(String(450))
    
    category = relationship('Category')


class PersonAdvExchItem(Base):
    __tablename__ = 'person_adv_exch_item'

    person_idpessoa = Column(Integer, ForeignKey('person.idpessoa'), primary_key=True)
    item_idobject = Column(Integer, ForeignKey('item.idobject'), primary_key=True)
    item_category_idcategory = Column(Integer, ForeignKey('category.idcategory'), primary_key=True)
    desc = Column(String(45))
    exch_for = Column(String(45))
    delivery = Column(String(45))
    reason = Column(String(45))
    market_price = Column(String(45))
    listed = Column(String(45))
    
    person = relationship('Person')
    item = relationship('Item', primaryjoin='')
    desc = Column(String(45))
    desc = Column(String(45))


class PersonAdvDonateItem(Base):
    __tablename__ = 'person_adv_donate_item'

    idperson_adv_donate_item = Column(Integer, primary_key=True)


class Country(Base):
    __tablename__ = 'country'

    idcountry = Column(Integer, primary_key=True)


class FU(Base):
    __tablename__ = 'fu'

    idfu = Column(Integer, primary_key=True)


class City(Base):
    __tablename__ = 'city'

    idcity = Column(Integer, primary_key=True)

class (Base):
class (Base):
class (Base):
class (Base):
class (Base):
class (Base):
