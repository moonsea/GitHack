#!/usr/bin/env python

from lib.datatype import AttribDict
# from lib.core.log import LOGGER

# sqlmap paths
paths = AttribDict()

# object to store original command line options
# cmdLineOptions = AttribDict()

# object to store merged options (command line, configuration file and default options)
# mergedOptions = AttribDict()

# object to share within function and classes command
# line options and settings
conf = AttribDict()

# object to share within function and classes results
kb = AttribDict()

# ignore Directory
conf.ignore_dir = ['.git']

# ignore file type
ignore_img = ['ico', 'bmp', 'jpg', 'tiff', 'gif', 'pcx', 'tga', 'exif', 'fpx', 'svg', 'psd', 'cdr', 'pcd', 'dxf', 'ufo', 'eps', 'ai', 'raw']
ignore_exec = ['exe', 'dll', 'com']
ignore_style = ['css']
conf.ignore_type = ignore_img + ignore_exec + ignore_style

# sensitive ip address
# conf.sense_ip = r'\d+\.\d+\.\d+\.\d+'
# conf.sense_ip = r'\d{1,2}|1\d\d|2[0-4]\d|25[0-5]((\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])){3}|(\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])){5})'
# conf.sense_ip = r'((25[0-5]|2[0-4]\d|[01]?\d\d?)($|(?!\.$)\.)){4}'
conf.sense_ip = r'(\d{1,3}\.){3}(\d{1,3})'

# sense_conf = ['conf', 'properity', 'setting', 'admin', 'manage', 'root']
# conf.sense_string = sense_conf


# object with each database management system specific queries
# queries = {}

# logger
# logger = LOGGER
