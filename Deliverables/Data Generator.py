import random

# Set the range for random integers
lower_limit = 1
upper_limit = 10000

# Generate 100 unique random integers and store them in a list
random_integers = random.sample(range(lower_limit, upper_limit + 1), 10000)

# Print the generated random integers
print(random_integers)