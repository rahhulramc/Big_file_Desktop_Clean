
import os
from os.path import join, getsize
i=0;
arr=[("?",-1.0)]

def myfn(a):
	return  a[1];
def gts(gpath):
	for root, dirs, files in os.walk(gpath):
		for name in files:
			try:
				temp = getsize(join(root,name))
			except OSError:
				continue
			path=join(root,name)
			arr.append((path,temp))
			arr.sort(key=myfn)
			if(len(arr)>11):
				arr.remove(arr[1])
	arr.remove(arr[0])
	return arr
	