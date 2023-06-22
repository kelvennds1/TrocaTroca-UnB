from sqlalchemy import Column, ForeignKey, Integer, String
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
    model_color = Column(String(450) )
    brand_species = Column(String(450) )
    year_acquired = Column(String(45) )
    desc = Column(String(1000) )
    condition = Column(String(450) )
    vaccines = Column(String(1000) )
    likes = Column(String(1000) )
    dislikes = Column(String(1000) )
    
    category_idcategory = Column(Integer, ForeignKey(Category.idcategory), primary_key=True)
    category = relationship('Category', foreign_keys='Item.category_idcategory')


class Person_adv_exch_item(Base):
    __tablename__ = 'person_adv_exch_item'
    idperson_adv_exch_item = Column(Integer, primary_key=True)
    desc = Column(String(1000) )
    delivers = Column(String(45) )
    reason = Column(String(450) )

    person_idperson = Column(Integer, ForeignKey(Person.idperson), primary_key=True)
    item_iditem = Column(Integer, ForeignKey(Item.iditem, primary_key=True))
    item_category_idcategory = Column(Integer, ForeignKey(Item.iditem.Category.idcategory), primary_key=True)
    person = relationship('Person', foreign_keys='Person_adv_exch_item.person_idperson')
    item = relationship('Item', foreign_keys='Person_adv_exch_item.item_iditem')
    category = relationship('Category', foreign_keys='Person_adv_exch_item.item_category_idcategory')
