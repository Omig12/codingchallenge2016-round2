#
# Israel O. Dilan-Pantojas
# israelodilan@gmail.com
#


# To run program you may pass a file through cli standard input
# with an array or a list of numbers separated by commas as input.
# You may also input an Array directly from cli standard input.
# And finally you might want to enter it manually when you run 
# the program, remember to use ("") quotations marks when doing so. 

# Ex.
# python greatest.py arrays.txt
# python greatest.py "[ 50, 9, 17, 0 ]"
# python greatest.py

import sys
from itertools import permutations

# Parse array from all input sources
def parse(a):
	array = a.replace(" ", "").strip().lstrip("[(\"").rstrip("])\"").strip("[]]()\"").split(",")
	return array

# Determine max number from possible permutations of array
def greatest(x):
	lst = []
	x = parse(x)
	perms = list(permutations(x, len(x)))
	for i in perms:
		w = ""
		for h in i:
			w += h
		lst.append(w)
	print max(lst)
	
# Try different input sources
try:  
	arg = sys.argv[1]

	try: 
		with open(arg, 'r') as f:
			for line in f:
				greatest(line)

	except:
		greatest(arg)

except:
	arr = raw_input("Please input an array of valid natural integers separated by a comma: ")
	greatest(arr)

	