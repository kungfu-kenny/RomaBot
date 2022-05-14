import os
# import sqlalchemy
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine,
                        Table,
                        Column,
                        Integer,
                        String,
                        ForeignKey,
                        PrimaryKeyConstraint)
# from sqlalchemy.orm.session import Session
from utilities.work_files import check_folder
from config import Folders, DbCredentials


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
    text_user = relationship("User",
        secondary=association_text_user,
        back_populates="text_user")
    text_group = relationship("Group",
        secondary=association_text_group,
        back_populates="text_group")
    text_channel = relationship("Channel",
        secondary=association_text_channel,
        back_populates="text_channel")

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, default='')
    last_name = Column(String, default='')
    user_name = Column(String, default='')
    text_user = relationship("Text",
        secondary=association_text_user,
        back_populates="text_user")
    user_group = relationship("Group",
        secondary=association_user_group,
        back_populates="user_group")
    user_channel = relationship("Channel",
        secondary=association_user_channel,
        back_populates="user_channel")

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    group_name = Column(String, default='')
    text_group = relationship("Text",
        secondary=association_text_group,
        back_populates="text_group")
    user_group = relationship("User",
        secondary=association_user_group,
        back_populates="user_group")

class Channel(Base):
    __tablename__ = 'channels'
    id = Column(Integer, primary_key=True)
    channel_name = Column(String, default='')
    text_channel = relationship("Text",
        secondary=association_text_channel,
        back_populates="text_channel")
    user_channel = relationship("Channel",
        secondary=association_user_channel,
        back_populates="user_channel")

class DbCreate:
    """
    class which is dedicated to create from the users necessary connections
    It would use the previous value to create connection
    """
    def __init__(self, create_conn:bool=False) -> None:
        self._host = DbCredentials.host
        self._name = DbCredentials.name
        self._database = DbCredentials.database
        self._password = DbCredentials.password
        self.engine = self.produce_engine(create_conn)
        self.session = self.produce_session()
        self.connection = self.create_connection()

    def produce_engine(self, create_conn:bool=False) -> object:
        """
        Method which is dedicated to create engine from the sql 
        Input:  All values for the PostgeSQL
        Output: object of the session
        """
        try:
            if create_conn:
                return create_engine(f'postgresql://{self._database}:{self._password}@{self._host}/{self._name}')
            return create_engine(f"sqlite:///{DbCredentials.db_path}")
        except Exception as e:
            print(f"We faced problems with values: {e}")
            check_folder(Folders.folder_storage_full)
            return create_engine(f"sqlite:///{DbCredentials.db_path}")

    def produce_session(self) -> object:
        """
        Method which is dedicated to create the session values for the database
        Input:  None
        Output: we create session for creation
        """
        Session = sessionmaker(bind=self.engine)
        return Session()

    def create_db(self):
        """
        Method which is dedicated to create databse values of this
        Input:  None
        Output: we created the selected values for the database values
        """
        try:
            Base.metadata.create_all(self.engine)
        except Exception as e:
            print(f"We faced problems with Base: {e}")

    def create_connection(self) -> object:
        """
        Method which is dedicated to create the connection values of this
        Input:  None
        Output: we created connection for selected values
        """
        return self.engine.connect()

    def close_connection(self) -> None:
        """
        Method which is dedicated to develop the 
        """
        if self.connection:
            self.connection.close()