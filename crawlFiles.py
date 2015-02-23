#!/usr/bin/python
# -*- coding : utf-8 -*-

import commands as c

# info about execution
user = c.getoutput('whoami')
groups = c.getoutput('groups').split(' ')
start = c.getoutput('pwd')

ignore = ('.git')

# helper function
def ls( directory='.'):
	l = c.getoutput('ls -la '+directory).split('\n')
	return l[1:]

def fileName(lsEntry):
	return lsEntry.split(' ')[-1]

def is_directory(lsEntry):
	if 'd' in lsEntry.split(' ')[0]:
		return True
	else :
		return False

def is_readable(lsEntry):
	pass

def log(message, tag='log'):
	print "[%s] %r"%(tag, message)

def crawl(start, depth = 0, max_depth = 5, parent = 0):

	result = {}
	result[start]={}
	
	if parent == 0:
		base_path = start.split('/')
		log('Initial path %r'%base_path)
	else :
		pass


	if max_depth < 0 :
		return False
	else:

		log("%s %s  max_depth is %i so depth is %i"%( "    " * depth, start, max_depth, depth), 'Path crawled')

		for f in ls(start):
			
			if is_directory(f):

				if fileName(f) in ignore:
					pass
				else:
					m = max_depth - 1
					d = depth + 1
					result[str(start)] = {}
					result[str(start)] = crawl(fileName(f),d ,m, start, base_path)
			else :
				result[fileName(f)] = fileName(f)

	return result


print 'result : %r'% crawl(start)



