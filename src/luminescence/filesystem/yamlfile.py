from __builtin__ import file as sys_file
from os.path import isfile
from yaml import load

class yamlfile(object):
    
    def __init__(self, filename):
        self.filename = filename
        self.file_contents = None
        self._require_existing_file(filename)
    
    def _require_existing_file(self, filename):
        if (not isfile(filename)):
            raise IOError("File does not exist: %s" % filename)
    
    def contents(self):
        self._load_contents()
        return self.file_contents

    def _load_contents(self):
        if (self.file_contents == None):
            self.file_contents = load(sys_file(self.filename, 'r').read())
    
    def __repr__(self):
        return "<file :: %s>" % self.filename