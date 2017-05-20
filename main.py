# The script should handle the kaggle files and sort them on folders as Keras wants them
import os
import shutil

# open directory
workingDir = raw_input('Which directory should be processed: ') # if using python 3, use input instead of raw_input
samples = int(raw_input('How many samples: '))
processPath = os.path.join(workingDir)
sortedPath = os.path.join(workingDir)
files = os.listdir(processPath)

# split the files on category in order to create folders
categories = {}
for item in files:
	# get the category until the first dot
	splitName = item.split('.', 1)
	categ = splitName[0]
	fileName = splitName[1]
	trainFolder = os.path.join(sortedPath,'train',categ)
	sampleFolder = os.path.join(sortedPath,'sample',categ)

	if categ in categories:
		categories[categ]['train'] += 1
	else:
		categories[categ] = {}
		categories[categ]['train'] = 1
		categories[categ]['samples'] = 1

	# make folder if does not exist already
	if not os.path.exists(trainFolder):		
		os.makedirs(trainFolder)
		os.makedirs(sampleFolder)

	# copy to samples
	if categories[categ]['samples'] < samples:
		shutil.copyfile(os.path.join(processPath, item), os.path.join(sampleFolder, fileName))
		categories[categ]['samples'] += 1

	# move to folder
	shutil.move(os.path.join(processPath, item), os.path.join(trainFolder, fileName))

print categories
print 'All sorted!'
