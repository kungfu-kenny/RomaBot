import random
import pandas as pd
from pprint import pprint
from sqlalchemy import (
    insert,
    delete,
    update,
)
from models.db_create import (
    DbCreate, 
    User,
    Text,
    Group,
    Channel,
    association_text_user,
    association_text_group,
    association_text_channel,
    association_user_group,
    association_user_channel,
)


class DataUsage:
    """
    class which is dedicated to operate values with the databases
    """
    def __init__(self, create_conn:bool=False, create_db:bool=False) -> None:
        self._produce_conn(create_conn, create_db)

    def _produce_conn(self, create_conn:bool=False, create_db:bool=False):
        """
        Method which is dedicated to produce the connection
        Input:  create_conn = bool value to create postgres connection
                create_db = bool value to create database
        Output: we created necessary connection
        """
        self.db = DbCreate(create_conn, create_db)
        self.session = self.db.session

    def _produce_close(self) -> None:
        """
        Method which is dedicated to produced closing of the dedicated session
        Input:  None
        Output: we closed our session
        """
        self.db.close_connection()

    def insert_jokes_database(self, df:pd.DataFrame) -> None:
        """
        Method which is dedicated to insert all new values for the selected users
        Input:  df = pandas dataframe of previously parsed
        Output: we created and inserted new values
        """
        df = df[~df.String.isin([f.text for f in self.session.query(Text).all()])]
        if not df.empty:
            self.session.add_all(
                [
                    Text(
                        text=elem.get('String', ''),
                        link=elem.get('Link', ''),
                        source=elem.get('Source', '')
                    ) 
                    for elem in df.to_dict('records')
                ]
            )
            self.session.commit()
    
    def return_random_joke(self, id_sent:int, id_type:int) -> set:
        """
        Method which is dedicated to return the random joke for the users
        Input:  id_sent = id which was previously sent
                id_type = id of the type which was previously used
        Output: set with id and the string message
        """
        if id_type == 1:
            print(1, id_sent)
            value_used = []
        elif id_type == 2:
            print(2, id_sent)
            value_used = []
        elif id_type == 3:
            print(3, id_sent)
            value_used = []
        #TODO add here the check
        #TODO add here insertion after
        length = self.session.query(Text.id).count()
        print(length)
        id_new = random.choice(
            [f.id for f in self.session.query(Text).filter(~Text.id.in_(value_used)).all()]
        )
        return self.session.query(Text).with_entities(Text.id, Text.text).filter_by(id=id_new).one()
        

    def insert_user(self, id:int, name:str, surname:str, username:str) -> None:
        """
        Method which is dedicated to insert selected user for the db
        Input:  id = id of the selected user
                name = first name of the telegram user
                surname = last name of the telegram user
                user_name = username selected
        Output: we created the insertion
        """
        if self.session.query(User).filter_by(id=id).one():
            return
        self.session.add(
            User(
                id=id,
                first_name=name,
                last_name=surname,
                user_name=username
            )
        )
        self.session.commit()