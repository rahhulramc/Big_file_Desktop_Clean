import os
import shutil
from os.path import join
pathname="/home/ram/Desktop/"
createpath="/home/ram/Documents/"

def arrange(pathname,createpath):
	for root,dirs,files in os.walk(pathname):
		for name in files:
			src=join(root,name)
			ext=name.split(".")
			xf=ext[-1] #simply gives me the last string in name of file after .
			if not os.path.exists(createpath + xf):
        			os.mkdir( createpath+xf)
			dest=createpath+xf
			try:
				shutil.move(src,dest)
			except shutil.Error:
				continue
	print "Successfully Moved"
