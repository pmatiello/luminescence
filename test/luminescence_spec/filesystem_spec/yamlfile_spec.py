from luminescence.filesystem.yamlfile import yamlfile

class file_spec():
    
    def should_open_files(self):
        yamlfile("test/fixtures/presentation.yaml")
    
    def should_raise_exception_if_file_does_not_exists(self):
        try:
            yamlfile("test/fixtures/invalid.yaml")
            raise AssertionError("Opened non-existing file")
        except IOError:
            pass
    
    def should_read_file_contents(self):
        f = yamlfile("test/fixtures/presentation.yaml")
        contents = f.contents()
        assert type(contents) == list
        assert len(contents) == 4
        assert "Square" in contents[0]['contents']