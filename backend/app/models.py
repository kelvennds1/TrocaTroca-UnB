from sqlalchemy import Column, ForeignKey, Integer, String, LargeBinary, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.database import Base 

from passlib.context import CryptContext  # Certifique-se de instalar passlib

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Pessoa/Usuário do sistema
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    registration = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(1000), nullable=False)
    name = Column(String(255), nullable=False)
    user_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    profile_picture = Column(LargeBinary, nullable=True)  # foto de perfil opcional
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    items = relationship('Item', back_populates='owner')
    swaps_initiated = relationship('Swap', foreign_keys='Swap.initiator_id', back_populates='initiator')
    swaps_received = relationship('Swap', foreign_keys='Swap.receiver_id', back_populates='receiver')

    def verify_password(self, password: str):
        return pwd_context.verify(password, self.password_hash)

    @classmethod
    def hash_password(cls, password: str):
        return pwd_context.hash(password)

# Categoria de um item
class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(String(500), nullable=True)
    
    items = relationship('Item', back_populates='category')

# Item a ser trocado
class Item(Base):
    __tablename__ = 'items'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    image = Column(LargeBinary, nullable=True)  # imagem opcional
    model = Column(String(100), nullable=True)
    brand = Column(String(100), nullable=True)
    year_acquired = Column(String(45), nullable=True)
    description = Column(String(1000), nullable=True)
    condition = Column(String(100), nullable=True)
    vaccines = Column(String(500), nullable=True)  # campo opcional para itens como animais
    likes = Column(String(500), nullable=True)
    dislikes = Column(String(500), nullable=True)
    item_type = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    category = relationship('Category', back_populates='items')
    owner = relationship('User', back_populates='items')

# Troca entre usuários
class Swap(Base):
    __tablename__ = 'swaps'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    initiator_id = Column(Integer, ForeignKey('users.id'), nullable=False)  # pessoa que inicia a troca
    receiver_id = Column(Integer, ForeignKey('users.id'), nullable=False)  # pessoa que recebe a oferta

    item_offered_id = Column(Integer, ForeignKey('items.id'), nullable=False)  # item oferecido
    item_requested_id = Column(Integer, ForeignKey('items.id'), nullable=False)  # item pedido

    status = Column(String(50), nullable=False, default='pending')  # 'pending', 'accepted', 'rejected'
    created_at = Column(DateTime, default=func.now(), nullable=False)

    initiator = relationship('User', foreign_keys=[initiator_id], back_populates='swaps_initiated')
    receiver = relationship('User', foreign_keys=[receiver_id], back_populates='swaps_received')
    item_offered = relationship('Item', foreign_keys=[item_offered_id])
    item_requested = relationship('Item', foreign_keys=[item_requested_id])
