# You can get the length using a function pre-loaded into
# Python called `len`

# Here's an example:

length = len("Hello!")
print(f"The string is {length} characters long")


"Hello, YOUR_NAME!"

# Into this:

"Hello, Kay!"

# For this, you could use the `replace` function:

old_string = "Hello, YOUR_NAME!"
new_string = old_string.replace("YOUR_NAME", "Kay")

print (new_string)

my_string = "hello"

len(my_string)              # <-- Independent Function
my_string.replace("h", "w") # <-- Method Function


#Exercise one

print("")
print("Function: uppercase")

# Search for 'python make string uppercase'

def make_uppercase(string):
  return string.upper()

check_that_these_are_equal( # type: ignore
  make_uppercase("hello"), "HELLO")

check_that_these_are_equal( #type: ignore
  make_uppercase("World"), "WORLD")

#Exercise 2

print("")
print("Function: lowercase")

# Search for 'python make string lowercase'

def make_lowercase(string):
  return string.lower()

check_that_these_are_equal( #type: ignore
  make_lowercase("HELLO"), "hello")

check_that_these_are_equal( #type: ignore
  make_lowercase("World"), "world")

#Exercise 3

def strip_whitespace(string):
 return string.strip()

check_that_these_are_equal( #type: ignore
  strip_whitespace("hello "), "hello")

check_that_these_are_equal( #type: ignore
  strip_whitespace(" hello world "), "hello world")
