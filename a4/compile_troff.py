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
data = sys.stdin.read()

#Store it in a ByteIO 'file'
bytIO = io.BytesIO(data.encode('utf-8'))
#Open the tar
tin = tarfile.open(fileobj=bytIO)

#Create a temporary directory
temp_dirpath = tempfile.mkdtemp()

#iterate over the TarInfo objects in the tar and print their
#names to the journald log
files_in_tar = tin.getnames()
for name in files_in_tar:
	logger.info(name)

#Extract the archive into the temporary directory
tin.extractall(temp_dirpath)

#Create a list of absolute paths by joining the temp directory path and the filename
abs_path_list = []
for name in files_in_tar:
	abs_path_list.append(temp_dirpath + '/'  + name)

#Iterate over all the paths and test file type with 'file -b' command
for path in abs_path_list:
	proc = subprocess.Popen(f"file -b {path}", shell=True, stdout=subprocess.PIPE)
	out = proc.stdout.read().decode('utf-8')
	print(out)

#Compile only the troff files and output the html to stdout
	proc = subprocess.Popen(f"file -b {path}", shell=True, stdout=subprocess.PIPE)
	out = proc.stdout.read().decode('utf-8')
	if out[0:5] == "troff":
		groff_proc = subprocess.Popen(f"groff -Thtml {path}", shell=True, stdout=subprocess.PIPE)
		groff_out = groff_proc.stdout.read().decode('utf-8')
		print(groff_out)
