from luminescence.presentation.builder import builder
from luminescence.filesystem.file import file
from __builtin__ import file as sys_file

class builder_spec():
    
    def setup(self):
        self.presentation_fixture = file("test/fixtures/presentation.yaml")

        template = sys_file("src/luminescence/resource/template.html").read()
        
        bldr = builder(self.presentation_fixture.contents(), template)
        self.presentation = bldr.render()
    
    def should_render_presentations_from_slides(self):
        assert "Square" in self.presentation
        assert "Circle" in self.presentation
        assert "Triangle" in self.presentation
    
    def should_render_slide_inside_div_block(self):
        before, after = self.presentation.split("Square")
        assert "<div class='slide' id='1'>" in before
        assert "</div>" in after
    
    def should_render_slide_set_inside_html_skeleton(self):
        before, after = self.presentation.split("Square")
        assert "<html>" in before
        assert "<body>" in before
        assert "</body>" in after
        assert "</html>" in after

    def should_have_a_default_template(self):
        builder(self.presentation_fixture.contents())
    
    def should_include_the_number_of_slides_in_output(self):
        assert "LAST_SLIDE = 4" in self.presentation
    
    def should_render_properties_in_output(self):
        assert "background-color" in self.presentation