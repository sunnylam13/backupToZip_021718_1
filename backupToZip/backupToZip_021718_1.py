# -*- coding: utf-8 -*-

# ! /usr/local/Cellar/python3/3.6.1

# backupToZip_021718_1.py - copies an entire folder and files within into a ZIP archive file, which adds an increment to the name each time it's done (i.e. creates a new numbered back up)

import zipfile, os

def backupToZip(folder):
	# back up the entire contents of `folder` into a zip file
	# `folder` is a string path to a folder to be backed up
	
	folder = os.path.abspath(folder) # make sure the folder is an absolute path string

	# figure what filename this code should use based on what files there are
	
	number = 1

	while True:
		zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip' # store new zip file name
		if not os.path.exists(zipFilename): # check whether the file exists
			break
		number = number + 1

	# TODO:  create the zip file
	
	print('Creating %s...' % (zipFilename))
	backupZip = zipfile.ZipFile(zipFilename,'w')

	# TODO:  cycle through entire folder tree and compress the files in each folder
	# use `os.walk()`
	
	for foldername,subfolders,filenames in os.walk(folder):
		# each iteration of os.walk(folder) returns current folder name, subfolders in that folder and filenames in that folder
		print('Adding files in %s...' % (foldername))

		# add the current folder to the zip file
		backupZip.write(foldername)

		# add all files in folder to zip file
		for filename in filenames:
			newBase = os.path.basename(folder) + '_'
			if filename.startswith(newBase) and filename.endswith('.zip'):
				continue # don't backup the backup ZIP files
			backupZip.write(os.path.join(foldername,filename))

		backupZip.close()

	print('Done.')

backupToZip('../docs/') # for testing