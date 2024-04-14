my_string = "Forty" + str(2)
print(my_string)

my_name = "Kay"
print(f"Hello, {my_name}!")

#Exercise one

print("")
print("Function: greet")

def greet(name):
	return f"Hello, {name}!"

check_that_these_are_equal( # type: ignore
	greet("Chuang-tzu"),
	"Hello, Chuang-tzu!"
)

check_that_these_are_equal( # type: ignore
	greet("Crab"),
	"Hello, Crab!"
)