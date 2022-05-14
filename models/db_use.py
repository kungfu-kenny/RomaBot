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
    def __init__(self) -> None:
        self._produce_conn()

    def _produce_conn(self):
        """
        Method which is dedicated to produce the connection
        Input:  None
        Output: we created necessary connection
        """
        self.db = DbCreate(False)
        self.connection = DbCreate(False).connection
        print(self.connection)
        print('..................................................')

    
    