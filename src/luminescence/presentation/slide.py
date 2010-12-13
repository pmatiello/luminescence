from markdown2 import markdown

class slide(object):
    
    def __init__(self, data):
        self.data = data
        self.contents_html = markdown(self.data['contents'])
        self._load_properties_names()
    
    def _load_properties_names(self):
        self.property_names = self.data.keys()
        self.property_names.remove('contents')
        
    def contents(self):
        return self.contents_html

    def properties(self):
        return self.property_names
    
    def property(self, name):
        return self.data[name]