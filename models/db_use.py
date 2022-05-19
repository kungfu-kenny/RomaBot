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
from utilities.work_files import make_sublists


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
            value_used = [
                f for f, *_ in 
                self.session.query(Text.id).filter(
                    association_text_user.c.id_text == Text.id
                ).filter(
                    association_text_user.c.id_user == id_sent
                    ).all()
            ]
        elif id_type == 2:
            value_used = [
                f for f, *_ in
                self.session.query(Text.id).filter(
                    association_text_group.c.id_text == Text.id
                ).filter(
                    association_text_group.c.id_group == id_sent
                ).all()
            ]
        elif id_type == 3:
            value_used = [
                f for f, *_ in
                self.session.query(Text.id).filter(
                    association_text_channel.c.id_text == Text.id
                ).filter(
                    association_text_channel.c.id_channel == id_sent
                ).all()
            ]
        if len(value_used) != self.session.query(Text.id).count():
            id_new = random.choice(
                [f.id for f in self.session.query(Text).filter(~Text.id.in_(value_used)).all()]
            )
            return self.session.query(Text).with_entities(Text.id, Text.text).filter_by(id=id_new).one() 
        else:
            return self.session.query(Text).with_entities(Text.id, Text.text).filter_by(id=random.randint(1, len(value_used))).one()  

    def insert_user_joke(self, id_sent:int, id_type:int, id_joke:int) -> None:
        """
        Method which is dedicated to insert the users joke to the record
        Input:  id_sent = id for who is sent
                id_type = id of the type of the joke
                id_joke = id of the joke to send
        Output: we created the
        """
        if id_type == 1:
            statement = association_text_user.insert().values(id_text=id_joke, id_user=id_sent)
        elif id_type == 2:
            statement = association_text_group.insert().values(id_text=id_joke, id_group=id_sent)
        elif id_type == 3:
            statement = association_text_channel.insert().values(id_text=id_joke, id_channel=id_sent)
        self.session.execute(statement)
        self.session.commit()

    def return_user_history(self, id_sent:int, id_type:int, index:int=0) -> set:
        """
        Method which is dedicated to return list of the user history
        Input:  id_sent = id of those who sent values
                id_type = id of the selected type to search
                index = index value for given values
        Output: length of the values, list of the user history
        """
        if id_type == 1:
            value_used = [
                f for f, *_ in 
                self.session.query(Text.id).filter(
                    association_text_user.c.id_text == Text.id
                ).filter(
                    association_text_user.c.id_user == id_sent
                    ).all()
            ]
        elif id_type == 2:
            value_used = [
                f for f, *_ in
                self.session.query(Text.id).filter(
                    association_text_group.c.id_text == Text.id
                ).filter(
                    association_text_group.c.id_group == id_sent
                ).all()
            ]
        elif id_type == 3:
            value_used = [
                f for f, *_ in
                self.session.query(Text.id).filter(
                    association_text_channel.c.id_text == Text.id
                ).filter(
                    association_text_channel.c.id_channel == id_sent
                ).all()
            ]
        length = len(value_used)
        value_list = make_sublists(value_used)
        tmp_bool = len(value_list)
        index = index % len(value_list) if value_list else 0
        value_list = value_list[index] if value_list else []
        return length, value_list, tmp_bool, id_type

    def return_text_joke(self, id_text:int) -> str:
        """
        Method which is dedicated to return text of the selected joke
        Input:  id_text = id of the selected text
        Output: string from the selected id
        """
        return self.session.query(Text.text).filter_by(id=id_text).one()[0]
        
    def insert_user(self, id:int, name:str, surname:str, username:str) -> None:
        """
        Method which is dedicated to insert selected user for the db
        Input:  id = id of the selected user
                name = first name of the telegram user
                surname = last name of the telegram user
                user_name = username selected
        Output: we created the insertion
        """
        if self.session.query(User).filter_by(id=id):
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

    def insert_group(self, id:int, name:str) -> None:
        """
        Method which is dedicated to insert selected group for the db
        Input:  id = id of the selected group
                name = name of the selected group
        Output: we inserted the 
        """
        if self.session.query(Group).filter_by(id=id):
            return
        self.session.add(
            Group(
                id=id,
                group_name=name
            )
        )
        self.session.commit()

    def insert_channel(self, id:int, name:str, username:str) -> None:
        """
        Method which is dedicated to insert selected channel for the db
        Input:  id = id of the selected channel
                name = name of the selected channel
                username = username of the selected 
        Output: we inserted the channel for the selected database 
        """
        if self.session.query(Channel).filter_by(id=id):
            return
        self.session.add(
            Channel(
                id=id,
                channel_name=name,
                channel_username=username
            )
        )
        self.session.commit()