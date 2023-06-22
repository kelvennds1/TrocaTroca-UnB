from sqlalchemy import Column, ForeignKey, Integer, String, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    idperson = Column(Integer, primary_key=True)
    registration = Column(String(100))
    passw = Column(String(1000))
    name = Column(String(1000))
    email = Column(String(1000))

class Category(Base):
    __tablename__ = 'category'
    idcategory = Column(Integer, primary_key=True)
    name = Column(String(450) )
    desc = Column(String(100) )

class Item(Base):
    __tablename__ = 'item'
    iditem = Column(Integer, primary_key=True)
    name = Column(String(450) )
    image_path = Column(String(450) )
    image_blob = Column(LargeBinary(length=(2**32)-1) )
    model_color = Column(String(450) )
    brand_species = Column(String(450) )
    year_acquired = Column(String(45) )
    desc = Column(String(1000) )
    condition = Column(String(450) )
    vaccines = Column(String(1000) )
    likes = Column(String(1000) )
    dislikes = Column(String(1000) )
    category_idcategory = Column(Integer, ForeignKey('category.idcategory'), primary_key=True)
    category = relationship('Category', foreign_keys=[category_idcategory], lazy='joined')


class Person_adv_exch_item(Base):
    __tablename__ = 'person_adv_exch_item'
    idpersonAdvExchItem = Column(Integer, primary_key=True)
    desc = Column(String(1000) )
    delivers = Column(String(45) )
    reason = Column(String(450) )
    listed = Column(String(15) )
    market_price = Column(String(45) )
    person_idperson = Column(Integer, ForeignKey('person.idperson'), primary_key=True)
    item_iditem = Column(Integer, ForeignKey('item.iditem'), primary_key=True)
    category_idcategory = Column(Integer, ForeignKey('category.idcategory'), primary_key=True)
    person = relationship('Person', foreign_keys=[person_idperson], lazy='joined')
    item = relationship('Item', foreign_keys=[item_iditem], lazy='joined')
    category = relationship('Category', foreign_keys=[category_idcategory], lazy='joined')

class Person_adv_donate_item(Base):
    __tablename__ = 'person_adv_donate_item'
    idpersonAdvDonateItem = Column(Integer, primary_key=True)
    desc = Column(String(1000) )
    delivers = Column(String(45) )
    reason = Column(String(450) )
    listed = Column(String(15) )
    person_idperson = Column(Integer, ForeignKey('person.idperson'), primary_key=True)
    item_iditem = Column(Integer, ForeignKey('item.iditem'), primary_key=True)
    category_idcategory = Column(Integer, ForeignKey('category.idcategory'), primary_key=True)
    person = relationship('Person', foreign_keys=[person_idperson], lazy='joined')
    item = relationship('Item', foreign_keys=[item_iditem], lazy='joined')
    category = relationship('Category', foreign_keys=[category_idcategory], lazy='joined')

class Country(Base):
    __tablename__ = 'country'
    idcountry = Column(Integer, primary_key=True)
    name = Column(String(60) )

class FUnit(Base):
    __tablename__ = 'FU'
    idFU = Column(Integer, primary_key=True)
    name = Column(String(45) )
    country_idcountry = Column(Integer, ForeignKey('country.idcountry'))
    country = relationship('Country', foreign_keys=[country_idcountry])

class City(Base):
    __tablename__ = 'city'
    idcity = Column(Integer, primary_key=True)
    name = Column(String(200) )
    FUnit_idFU = Column(Integer,ForeignKey('FU.idFU'), primary_key=True)
    FUnit_country_idcountry = Column(Integer,ForeignKey('country.idcountry'), primary_key=True)
    FUnit = relationship('FUnit', foreign_keys=[FUnit_idFU])
    country = relationship('Country', foreign_keys=[FUnit_country_idcountry])

class Street(Base):
    __tablename__ = 'street'
    idstreet = Column(Integer, primary_key=True)
    name = Column(String(200) )
    city_idcity = Column(Integer,ForeignKey('city.idcity'), primary_key=True)
    city_FUnit_idFU = Column(Integer,ForeignKey('FU.idFU'), primary_key=True)
    city_FUnit_country_idcountry = Column(Integer,ForeignKey('country.idcountry'), primary_key=True)
    city = relationship('City', foreign_keys=[city_idcity])
    FUnit = relationship('FUnit', foreign_keys=[city_FUnit_idFU])
    country = relationship('Country', foreign_keys=[city_FUnit_country_idcountry])

class Address(Base):
    __tablename__ = 'address'
    idaddress = Column(Integer, primary_key=True)
    desc = Column(String(1000) )
    street_idstreet = Column(Integer,ForeignKey('street.idstreet'), primary_key=True)
    street_city_idcity = Column(Integer,ForeignKey('city.idcity'), primary_key=True)
    street_city_FUnit_idFU = Column(Integer,ForeignKey('FU.idFU'), primary_key=True)
    street_city_FUnit_country_idcountry = Column(Integer,ForeignKey('country.idcountry'), primary_key=True)
    city = relationship('City', foreign_keys=[street_city_idcity])
    FUnit = relationship('FUnit', foreign_keys=[street_city_FUnit_idFU])
    country = relationship('Country', foreign_keys=[street_city_FUnit_country_idcountry])
