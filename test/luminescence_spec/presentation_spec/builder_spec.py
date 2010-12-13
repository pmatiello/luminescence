from mockito import mock, when
from luminescence.presentation.builder import builder
from luminescence.filesystem.file import file

class builder_spec():
    
    def setup(self):
        slide1 = mock()
        slide2 = mock()
        slide3 = mock()
        
        when(slide1).contents().thenReturn("contents: Square stuff")
        when(slide2).contents().thenReturn("contents: Circle stuff")
        when(slide3).contents().thenReturn("contents: Triangle stuff")
        
        template = file("src/luminescence/resource/template.html")
        
        self.slide_set = [slide1, slide2, slide3]
        bldr = builder(self.slide_set, template)
        self.presentation = bldr.render()
    
    def should_render_presentations_from_slides(self):
        assert "Square stuff" in self.presentation
        assert "Circle stuff" in self.presentation
        assert "Triangle stuff" in self.presentation
    
    def should_render_slide_inside_div_block(self):
        before, after = self.presentation.split("Square stuff")
        assert "<div class='slide' id='1'>" in before
        assert "</div>" in after
    
    def should_render_slide_set_inside_html_skeleton(self):
        before, after = self.presentation.split("Square stuff")
        assert "<html>" in before
        assert "<body>" in before
        assert "</body>" in after
        assert "</html>" in after

    def should_have_a_default_template(self):
        builder(self.slide_set)
    
    def should_include_the_number_of_slides_in_output(self):
        assert "< 3)" in self.presentation
    
    def should_render_properties_in_output(self):
        assert "background-color" in self.presentation