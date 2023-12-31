"""new engine"""
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
import os
from models.city import City



user = os.environ.get('HBNB_MYSQL_USER')
pswd = os.environ.get('HBNB_MYSQL_PWD')
host = os.environ.get('HBNB_MYSQL_HOST')
database = os.environ.get('HBNB_MYSQL_DB')
envir = os.environ.get('HBNB_ENV')

class DBStorage:
    """implement database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """instantiating db storage"""
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(user, pswd, host, database),
                            pool_pre_ping=True,
        )
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

        if envir == "test":
            metadata = MetaData()
            metadata.drop_all(self.__engine, checkfirst=False)

    def all(self, cls=None):
        """public inst method query all class from db"""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        if cls is None:
            cls = [User, State, City, Amenity, Place, Review]
            query = []
            for cl in cls:
                query.extend(self.__session.query(cl).all())
        else:
            query = self.__session.query(cls).all()    
        
        cls_objs = {}
        for itm in query:
            cls_objs[itm.to_dict()["__class__"] + "." + itm.id] = itm
        return cls_objs

    def new(self, obj):
        """add objt to current db session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes to current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delet from current db session"""
        if obj:
            self.__session.delete(obj)
    
    def reload(self):
        """method creates all tables in db"""
        from models.user import User
        from models.state import State, Base
        from models.city import City, Base
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        Base.metadata.create_all(self.__engine)

        DBStorage.Session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )
        self.__session = DBStorage,Session()

    def search(self, cls=None, **kwargs):
        """ search method """
        objs = self.all(cls)
        for key, obj in objs.items():
            flag = 0
            for attr, value in kwargs.items():
                if getattr(obj, attr) != value:
                    flag = 1
                    break
            if flag == 0:
                return obj
        return None

    def close(self):
        """ calls remove() method on the private session attribute """
        self.__session.close()
