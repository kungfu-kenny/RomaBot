from email.policy import default
import sqlalchemy
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine,
                        Table,
                        Column,
                        Integer,
                        String,
                        ForeignKey,
                        PrimaryKeyConstraint)
from sqlalchemy.orm.session import Session


Base = declarative_base()

association_text_user = Table('text_user', Base.metadata,
    Column('id_text', ForeignKey(f'texts.id')),
    Column('id_user', ForeignKey(f'users.id')),
    PrimaryKeyConstraint('id_text', 'id_user'),    
)

association_text_group = Table('text_group', Base.metadata,
    Column('id_text', ForeignKey(f'texts.id')),
    Column('id_group', ForeignKey(f'groups.id')),
    PrimaryKeyConstraint('id_text', 'id_group'),    
)

association_text_channel = Table('text_user', Base.metadata,
    Column('id_text', ForeignKey(f'texts.id')),
    Column('id_channel', ForeignKey(f'channels.id')),
    PrimaryKeyConstraint('id_text', 'id_channel'),    
)

association_user_group = Table('user_group', Base.metadata,
    Column('id_user', ForeignKey(f'users.id')),
    Column('id_group', ForeignKey(f'groups.id')),
    PrimaryKeyConstraint('id_text', 'id_group'),    
)

association_user_channel = Table('user_channel', Base.metadata,
    Column('id_user', ForeignKey(f'users.id')),
    Column('id_channel', ForeignKey(f'channels.id')),
    PrimaryKeyConstraint('id_text', 'id_channel'),    
)

class Text(Base):
    __tablename__ = 'texts'
    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, default='')
    last_name = Column(String, default='')
    user_name = Column(String, default='')

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    group_name = Column(String, default='')

class Channel(Base):
    __tablename__ = 'channels'
    id = Column(Integer, primary_key=True)
    channel_name = Column(String, default='')

class SessionCreate:
    """
    class which is dedicated to create from the users necessary sessions
    It would use the previous value to create session
    """
    def __init__(self) -> None:
        pass

    def develop_session(self) -> object:
        """
        Method which is dedicated to create the session values for the database
        """
        pass