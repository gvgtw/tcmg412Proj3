FILE_NAME = 'path/to/file'

# Use open() to get a filehandle that can access the file
fh = open(FILE_NAME)

# Loop through the file 
for line in fh:
  print(line)

# The filehandle object provides many basic file operations:
fh.read(64)     # read the specified bytes from the file (if no byte size is specified, then the entire file is read)
fh.readline()   # read a single line from the file (up to a newline character - \n)
fh.write('some data here')  # write a string to the file (make sure the file was open()'ed for writing!)
fh.close()      # close the file when you're finished with it

  
# Alternately, skip the assignment to the filehandle altogether:
for line in open(FILE_NAME):
  print(line)

# The loop example above is memory-efficient, and also easy to read
