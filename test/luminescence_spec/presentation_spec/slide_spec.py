from luminescence.presentation.slide import slide
from yaml import load

class slide_spec():
    
    def setup(self):
        slide_fixture = load(file("test/fixtures/presentation.yaml").read())[0]
        
        self.slide = slide(slide_fixture)
        
    def should_have_contents(self):
        assert "Square" in self.slide.contents()
        assert "In geometry" in self.slide.contents()
    
    def should_present_contents_in_html_format(self):
        assert "<h1>Square</h1>" in self.slide.contents()
        assert "<p>In geometry, a <em>square</em> is a regular quadrilateral.</p>" in self.slide.contents()
    
    def should_have_properties(self):
        print self.slide.properties()
        assert self.slide.properties() == ['background-color']
        assert self.slide.property('background-color') == '#d2d9e5'