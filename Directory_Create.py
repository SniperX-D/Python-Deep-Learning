import os
from pathlib import Path
import matplotlib.pyplot as plt
import shutil

#gets the project path, creates the project folder name
#and then creates test and training folders for later use...
def create_base_dir(base_path, library_name):
	
	#check if directory is ok
	if (not os.path.exists(base_path)):
		print("no such directory as %s!" % base_path)
		exit(1)
	
	#create project directory
	new_path = os.path.join(base_path, library_name)
	if (not os.path.exists(new_path)): #already exists?
		os.mkdir(new_path)
		
	#create the test
	test_path = os.path.join(new_path,"test")
	if (not os.path.exists(test_path)): #already exists?
		os.mkdir(test_path)
		
	#create the test
	train_path = os.path.join(new_path,"train")
	if (not os.path.exists(train_path)): #already exists?
		os.mkdir(train_path)
		
	return new_path #the project directory
	
#gets the project path with test or train sub directory and the 
#path where the images are located and then moves the images from 
#the images path to parent path by this context:
#all if train \ 70% if testing
def move_images(path, images_path):
	
	#check if directory is ok
	if (not os.path.exists(path)):
		print("no such directory as %s!" % base_path)
		exit(1)
	
	#testing?
	if 'test' in path[-6:]:
		images = os.listdir(images_path) #images in the dir...
		count = 0.7 * len(images) #count how much is 70%
		i = 0
		#move the images
		for img in images:
			if str(img).split(".")[-1:][0] in {"jpg","png","jpeg"}: #its an image?
				shutil.move(os.path.join(images_path,img), os.path.join(path,img)) #lets move the image!
				i+=1
				if i > count: #enogh images?
					break
					
	#training!
	else:
		for img in os.listdir(images_path):
			print("img:",img, str(img).split(".")[-1:][0])
			if str(img).split(".")[-1:][0] in {"jpg","png","jpeg"}: #its an image?
				shutil.move(os.path.join(images_path,img), os.path.join(path,img)) #lets move the image!

#gets the project directory with the images and show our
#beautiful images!
def show_images(path):
	print('The names of the files in ', path, ' :')
	for img in os.listdir(path):
		if img.split(".")[-1:][0] in {"jpg","png","jpeg"}:
			plt.imshow(plt.imread(os.path.join(path, img))) 
			plt.show()


def main():
	#parent path for project:
	parent_path = input("enter path>>")
	if (parent_path == ''): #default directory to home
		parent_path = str(Path.home()) 
	new_path = create_base_dir(parent_path, "proj1") #set up the directory
	
	#testing or training?
	con = input("are you training or testing? >>") 
	if ("test" in con):
		new_path = os.path.join(new_path,"test")
	elif ("train" in con):
		new_path = os.path.join(new_path,"train")
	else:
		print("what?")
		exit() 
	
	#move the images
	move_images(new_path, input("enter images path>>"))
	
	#show our beautiful images with plt!
	show_images(new_path)
	
main()
