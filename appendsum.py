#! /usr/bin/python

def appendsum(lst):

	for c in range(25):
		last3 = lst[-3:]
		print last3
		lst.append(sum(last3))
	return lst


mylist = [0,1,2]

x = appendsum(mylist)

print x[10], x[20]