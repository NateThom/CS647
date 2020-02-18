#!/usr/bin/python3

import tarfile # Used to manipulate tarfiles
import sys # Used for writing to stdout
import io # Used for in memory files like StringIO or ByteIO
import tempfile # Used to create temporary files and directories
import os # Used to list files in a directory
import subprocess # Used to run other applications with Popen
import logging # Used for logging

from systemd.journal import JournaldLogHandler

##### BEGIN LOGGING SETUP #####

# get an instance of the logger object this module will use
logger = logging.getLogger("tarecho")

# instantiate the JournaldLogHandler to hook into systemd
journald_handler = JournaldLogHandler()

# set a formatter to include the level name
journald_handler.setFormatter(logging.Formatter(
'[%(levelname)s] %(message)s'
))

# add the journald handler to the current logger
logger.addHandler(journald_handler)

# optionally set the logging level
logger.setLevel(logging.DEBUG)

##### END OF LOGGING SETUP #####

#Read the binary data from stdin buffer.read()
data = sys.stdin.buffer.read()

#Store it in a ByteIO 'file'

#Open the tar

#Create a temporary directory

#iterate over the TarInfo objects in the tar and print their
#names to the journald log

#Extract the archive into the temporary directory

#Get a list of the files

#Create a list of absolute paths by joining the temp directory path and the filename

#Iterate over all the paths and test file type with 'file -b' command

#Compile only the troff files and output the html to stdout
