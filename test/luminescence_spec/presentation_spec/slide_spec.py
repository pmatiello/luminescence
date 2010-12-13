from luminescence.presentation.slide import slide
from mockito import mock, when

class slide_spec():
    
    def setup(self):
        fl = mock()
        content_fixture = file("test/_test_set/01 square.yaml").read()
        when(fl).contents().thenReturn(content_fixture)
        
        self.slide = slide(fl)
        
    def should_have_contents(self):
        assert "Square" in self.slide.contents()
        assert "In geometry" in self.slide.contents()
    
    def should_present_contents_in_html_format(self):
        assert "<h1>Square</h1>" in self.slide.contents()
        assert "<p>In geometry, a <em>square</em> is a regular quadrilateral.</p>" in self.slide.contents()
    
    def should_have_properties(self):
        assert self.slide.properties() == ['background-color']
        assert self.slide.property('background-color') == '#d2d9e5'