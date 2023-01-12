from abc import *
class Myclass(ABC):
    @abstractmethod
    def connectingtodatabase(self):
        pass

    @abstractmethod
    def disconnectingtodatabase(self):
        pass

class Oracle(Myclass):
    def connectingtodatabase(self):
        print("Connecting to Oracle Datbase")

    def disconnectingtodatabase(self):
        #return super().disconnectingtodatabase()
        print("Disconnecting to Oracle Database")


class Sybase(Myclass):
    def connectingtodatabase(self):
        print("Connecting to Sybase Database")

    def disconnectingtodatabase(self):
        print("Disconnecting to Sybase datbase")


class Database:
    string = input("Enter the datbase: ")

    classname = globals()[string]

    x=classname()

    x.connectingtodatabase()
    x.disconnectingtodatabase()