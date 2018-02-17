# -*- coding: utf-8 -*-

# ! /usr/local/Cellar/python3/3.6.1

# backupToZip_021718_1.py - copies an entire folder and files within into a ZIP archive file, which adds an increment to the name each time it's done (i.e. creates a new numbered back up)

import zipfile, os

def backupToZip(folder):
	# back up the entire contents of `folder` into a zip file
	
	folder = os.path.abspath(folder) # make sure the folder is an absolute path string

	# figure what filename this code should use based on what files there are
	
	number = 1

	while True:
		zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
		if not os.path.exists(zipFilename):
			break
		number = number + 1

	# TODO:  create the zip file
	# TODO:  cycle through entire folder tree and compress the files in each folder
	print('Done.')

backupToZip('../docs/') # for testing