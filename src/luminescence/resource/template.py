from pkg_resources import resource_string #@UnresolvedImport

def default_template():
    return resource_string(__name__, 'template.html')