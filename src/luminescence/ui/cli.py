from sys import argv, exit
from luminescence.presentation.builder import builder
from luminescence.filesystem.yamlfile import yamlfile
from yaml.parser import MarkedYAMLError

def luminescence():
    try:
        source_path, output_path, template_path = _parse_arguments()
    
        source = yamlfile(source_path)
        template = _define_template(template_path)
        
        presentation_builder = builder(source.contents(), template)
        html = presentation_builder.render()
        
        _write_output(output_path, html)
        
    except IOError as e:
        print e
    except MarkedYAMLError as e:
        print e

def _define_template(template_path):
    if (template_path):
        template = file(template_path).read()
    else:
        template = None
    return template

def _write_output(output_path, html):
    output = file(output_path, 'w')
    output.write(html)
    output.close()

def _parse_arguments():
    if (len(argv) == 4):
        command, source_path, output_path, template_path = argv               #@UnusedVariable
    elif (len(argv) == 3):
        command, source_path, output_path, template_path = argv + [None]      #@UnusedVariable
    else:
        print "Syntax: %s <source directory> <output file> [<template file>]" % argv[0]
        exit(1)
    return source_path, output_path, template_path

