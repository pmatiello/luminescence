from luminescence.filesystem.file import file

class file_spec():
    
    def should_open_files(self):
        file("test/_test_set/01 square.yaml")
    
    def should_raise_exception_if_file_does_not_exists(self):
        try:
            file("test/_test_set/99 does not exists")
            raise AssertionError("Opened non-existing file")
        except IOError:
            pass
    
    def should_read_file_contents(self):
        f = file("test/_test_set/01 square.yaml")
        contents = f.contents()
        assert type(contents) == str
        assert "contents: |" in contents
        assert "Square" in contents
        assert "In geometry, a _square_ is a regular quadrilateral." in contents