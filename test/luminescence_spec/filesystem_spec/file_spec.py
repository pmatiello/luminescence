from luminescence.filesystem.file import file

class file_spec():
    
    def should_open_files(self):
        file("test/fixtures/presentation.yaml")
    
    def should_raise_exception_if_file_does_not_exists(self):
        try:
            file("test/fixtures/invalid.yaml")
            raise AssertionError("Opened non-existing file")
        except IOError:
            pass
    
    def should_read_file_contents(self):
        f = file("test/fixtures/presentation.yaml")
        contents = f.contents()
        assert type(contents) == list
        assert len(contents) == 4
        assert "Square" in contents[0]['contents']