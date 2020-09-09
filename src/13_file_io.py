"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
import os
print(os.getcwd())

with open('/Users/petejames/lambda-cs/Intro-Python-I/src/foo.txt','r') as f:
    read_data = f.read()

print(read_data)
print(f.closed) #file closed if true

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
f = open('/Users/petejames/lambda-cs/Intro-Python-I/src/bar.txt','w') #creates if doesn't exist yet
f.write('first line\nsecond line\nthird line')
f.close()

