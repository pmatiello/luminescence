from os import listdir
from os.path import isfile
from luminescence.filesystem.file import file

class crawler(object):
    
    def __init__(self, directory):
        self.directory = directory
    
    def files(self):
        filesystem_objects = listdir(self.directory)
        filesystem_objects.sort()
        files = self._retrieve_files(filesystem_objects)
        return files
        
    def _retrieve_files(self, filesystem_objects):
        files = []
        for fsobj in filesystem_objects:
            filepath = self.directory + "/" + fsobj
            if isfile(filepath):
                files.append(file(filepath))
        return files