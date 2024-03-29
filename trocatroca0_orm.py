from sqlalchemy import Column, ForeignKey, Integer, String, LargeBinary, DATETIME
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
    image_blob = Column(LargeBinary(length=(2**32)-1) )
    model_color = Column(String(450) )
    brand_species = Column(String(450) )
    year_acquired = Column(String(45) )
    desc = Column(String(1000) )
    condition = Column(String(450) )
    vaccines = Column(String(1000) )
    likes = Column(String(1000) )
    dislikes = Column(String(1000) )
    item_type = Column(String(10) )
    time_created = Column(DATETIME, server_default="CONVERT_TZ(NOW(),'UTC','America/Sao_Paulo')")
    category_idcategory = Column(Integer, ForeignKey('category.idcategory'))
    person_idperson = Column(Integer, ForeignKey('person.idperson'))
    category = relationship('Category', foreign_keys=[category_idcategory], lazy='joined')
    person = relationship('Person', foreign_keys=[person_idperson], lazy='joined')


class Swap(Base):
    __tablename__ = 'swap'
    idswap = Column(Integer, primary_key=True)
    p1Key = Column(Integer, ForeignKey('person.idperson'))
    p1kGive = Column(Integer, ForeignKey('item.iditem'))
    p1kReceive = Column(Integer, ForeignKey('item.iditem'))
    p2kGive = Column(Integer, ForeignKey('item.iditem'))
    p2kReceive = Column(Integer, ForeignKey('item.iditem'))
    p2Key = Column(Integer, ForeignKey('person.idperson'))
    time_created = Column(DATETIME, server_default="CONVERT_TZ(NOW(),'UTC','America/Sao_Paulo')")
    person1 = relationship('Person', foreign_keys=[p1Key])
    p1_k_give = relationship('Item', foreign_keys=[p1kGive])
    p1_k_receive = relationship('Item', foreign_keys=[p1kReceive])
    person2 = relationship('Person', foreign_keys=[p2Key])
    p2_k_give = relationship('Item', foreign_keys=[p2kGive])
    p2_k_receive = relationship('Item', foreign_keys=[p2kReceive])
