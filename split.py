# Let's say you have a string like this

my_string = "apple banana peach pear orange"

# You want to split it apart based on words (using the spaces as delimiters)
#   FYI: splitting apart a larger string into smaller ones (especially by 
#        spaces) is called 'tokenizing' a string

items = my_string.split() # by default, split uses spaces

# Now, items looks like this:

items == ['apple', 'banana', 'peach', 'pear', 'orange']

# split() always returns a list, so you can use the results of that function like any other list:

for item in my_string.split()
    print(item)
  
# If you need to use a different character (rather than a space) as the delimiter:

log_line = "localhost:2020-09-12:foo:404"
items = log_line.split(':') # i fyou pass an argument to split(), it uses that as the delimiter

# The result is still a list:

items == ['localhost', '2020-09-12', 'foo', '404']
