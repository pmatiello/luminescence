from sys import argv, exit
from luminescence.filesystem.crawler import crawler
from luminescence.presentation.builder import builder
from luminescence.filesystem.file import file
from __builtin__ import file as sys_file

def luminescence():
    source_path, output_path, template_path = _parse_arguments()
    
    file_set = crawler(source_path).files()    
    template = _define_template(template_path)
        
    presentation_builder = builder(file_set, template)
    html = presentation_builder.render()
    
    _write_output(output_path, html)

def _define_template(template_path):
    if (template_path):
        template = file(template_path)
    else:
        template = None
    return template

def _write_output(output_path, html):
    output = sys_file(output_path, 'w')
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

