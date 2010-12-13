from luminescence.filesystem.crawler import crawler

class crawler_spec():
    
    def should_discover_in_directory(self):
        crw = crawler("test/_test_set")
        files = crw.files()
        assert len(files) == 4
        assert files[0].filename == "test/_test_set/01 square.yaml"
        assert files[1].filename == "test/_test_set/02 circle.yaml"
        assert files[2].filename == "test/_test_set/03 triangle.yaml"
        assert files[3].filename == "test/_test_set/04 pentagon.yaml"
    
    def should_not_discover_files_in_subdirectories(self):
        crw = crawler("test/_test_set")
        files = crw.files()
        for each in files:
            assert "trap" not in each.filename