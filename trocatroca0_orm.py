from sqlalchemy import Column, ForeignKey, Integer, String, LargeBinary, TIMESTAMP
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
    pfp_blob = Column(LargeBinary(length=(2**32)-1) )

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
    category_idcategory = Column(Integer, ForeignKey('category.idcategory'))
    person_idperson = Column(Integer, ForeignKey('person.idperson'))
    category = relationship('Category', foreign_keys=[category_idcategory], lazy='joined')
    person = relationship('Person', foreign_keys=[person_idperson], lazy='joined')

class Person_adv_exch_item(Base):
    __tablename__ = 'person_adv_exch_item'
    idpersonAdvExchItem = Column(Integer, primary_key=True)
    name = Column(String(75) )
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
    name = Column(String(75) )
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


class Swap(Base):
    __tablename__ = 'swap'
    idswap = Column(Integer, primary_key=True)
    p1Key = Column(Integer, ForeignKey('person.idperson'))
    p1kGive = Column(Integer, ForeignKey('item.iditem'))
    p1kReceive = Column(Integer, ForeignKey('item.iditem'))
    p2kGive = Column(Integer, ForeignKey('item.iditem'))
    p2kReceive = Column(Integer, ForeignKey('item.iditem'))
    p2Key = Column(Integer, ForeignKey('person.idperson'))
    time_created = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')
    person1 = relationship('Person', foreign_keys=[p1Key])
    p1_k_give = relationship('Item', foreign_keys=[p1kGive])
    p1_k_receive = relationship('Item', foreign_keys=[p1kReceive])
    person2 = relationship('Person', foreign_keys=[p2Key])
    p2_k_give = relationship('Item', foreign_keys=[p2kGive])
    p2_k_receive = relationship('Item', foreign_keys=[p2kReceive])
