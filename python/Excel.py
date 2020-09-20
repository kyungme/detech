from abc import *

class ExcelData(metaclass=ABCMeta):

    @abstractmethod
    def create_table(self, raw_data):
        pass

    @abstractmethod
    def range(self, sheet):
        pass
