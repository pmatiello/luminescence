from luminescence.filesystem.yamlfile import yamlfile
from yaml.error import MarkedYAMLError

class file_spec():
    
    def should_open_files(self):
        yamlfile("test/fixtures/presentation.yaml")
    
    def should_raise_exception_if_file_does_not_exists(self):
        try:
            yamlfile("test/fixtures/filedoesnotexist.yaml")
            raise AssertionError("Opened non-existing file")
        except IOError:
            pass
    
    def should_read_file_contents(self):
        f = yamlfile("test/fixtures/presentation.yaml")
        contents = f.contents()
        assert type(contents) == list
        assert len(contents) == 4
        assert "Square" in contents[0]['contents']
        assert "Circle" in contents[1]['contents']
        assert "Triangle" in contents[2]['contents']
        assert "Pentagon" in contents[3]['contents']
    
    def should_raise_exception_if_file_contents_is_invalid_yaml(self):
        f = yamlfile("test/fixtures/invalid.yaml")
        try:
            f.contents()
            raise AssertionError("Returned contents of invalid YAML file")
        except MarkedYAMLError:
            pass
