from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.core.database import Base


class BlackListTokenModel(Base):
    __tablename__ = 'black_list_token'
    
    expire: Mapped[datetime]
    

class UserModel(Base):
    __tablename__ = 'user'
    
    username: Mapped[str] = mapped_column(unique=True, index=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    hashed_password: Mapped[str]
    
    articles = relationship('ArticleModel', back_populates='author', lazy='selectin', passive_deletes=True)
