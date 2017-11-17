from DataSet import DataSet

class DataParser(object):
    def __init__(self, MyFile):
        super(DataParser, self).__init__()
        self.File = MyFile
        self.NumberOfAttributes = []
        self.dataTable = []
