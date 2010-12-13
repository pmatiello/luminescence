from luminescence.presentation.slide import slide
from luminescence.resource.template import default_template
from yaml import load

class builder(object):
    
    def __init__(self, presentation_file, template=None):
        self.data = load(presentation_file.contents())
        if (template == None):
            self.template = default_template()
        else:
            self.template = template.contents()

    def render(self):
        content_list = []
        slide_list = []
        for each in self.data:
            sld = slide(each)
            slide_list.append(sld)
            content_list.append(sld.contents())
        content_list = self._include_divs(content_list)
        html = self._make_string(content_list)
        html = self._include_properties(html, slide_list)
        return html
    
    def _make_string(self, source_list):
        string = "\n".join(source_list)
        string = self._include_in_template(string)
        return string
    
    def _include_divs(self, source_list):
        self._initialize_id_counter()
        return map(
            lambda text: "<div class='slide' id='%s'>\n%s\n</div>" % (self._get_id() ,text),
            source_list)
    
    def _initialize_id_counter(self):
        self._id_counter = 0
    
    def _get_id(self):
        self._id_counter = self._id_counter + 1
        return self._id_counter
    
    def _include_in_template(self, body):
        html = self.template
        html = html.replace("%INCLUDE: SLIDES%", body)
        html = html.replace("%INCLUDE: SLIDES_NUM%", str(len(self.data)))
        return html
    
    def _include_properties(self, html, slides):
        self._initialize_id_counter()
        properties_js = "properties = {\n"
        for slide in slides:
            id = self._get_id()
            for property in slide.properties():
                properties_js = properties_js + "'%s.%s': '%s',\n" %  (id, property, slide.property(property))
        properties_js = properties_js + "}\n"
        html = html.replace("%INCLUDE: PROPERTIES%", properties_js)
        return html