Word histogram

The histogram is a graphical representation drawn based on the frequency of occurrence of things. Histogram for a word is drawn based on the number of occurrences of each character in the word. An inverted dictionary is used to maintain the list of characters that has same frequency. Design an algorithm and write the Python code to compute and print the frequency of occurrence of character as a dictionary (ch:count). Make the entire process to be case insensitive. For example, if the input word is ‘parrot’, then the dictionary with characters and frequency of occurrence is 
{'a': 1, 'o': 1, 'p': 1, 'r': 2, 't': 1}
and the inverted dictionary is 
{1: ['o', 'p', 'a', 't'], 2: ['r']}
Print dictionary in sorted order by key. 
[Hint: use pprint function for printing dictionary in sorted order. 

Syntax for pprint is 
pprint(dictionary name)

Include the line “from pprint import pprint” in the top of your program]

Check for boundary conditions and print 'Invalid input' if conditions are not met. 
Input Format:
Input String
Output Format:
Dictionary of characters in the word as keys and count as values in sorted order by key
Inverted dictionary in sorted order by key
Boundary Conditions:
Given word should only contain alphabets

Example 

Input:
dictionary
$END
dairy1
Output:
{'a': 1, 'c': 1, 'd': 1, 'i': 2, 'n': 1, 'o': 1, 'r': 1, 't': 1, 'y': 1}
{1: ['r', 'd', 'c', 'o', 'n', 'y', 'a', 't'], 2: ['i']}
$END
Invalid input
Hidden case
Dinosaur
Output
{'a': 1, 'd': 1, 'i': 1, 'n': 1, 'o': 1, 'r': 1, 's': 1, 'u': 1}
{1: ['n', 's', 'a', 'd', 'u', 'r', 'o', 'i']}


SOLUTION:

from pprint import pprint
import sys
def invert_dict(d):
	inverse = dict()
	for key in d:
		val=d[key]
		if val not in inverse:
			inverse[val]=key
		else:
			inverse[val].append(key)
		inverse[val]=sorted(inverse[val])				
	return(inverse)
s=input()
if not s.isalpha():
	print("Invalid input")
	sys.exit()
d1={}
for i in s:
	if i not in d1.keys():
		d1[i]=1
	else:
		d1[i]=d1[i]+1
pprint(d1)		
pprint(invert_dict(d1))
