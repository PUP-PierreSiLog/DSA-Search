import random

# Set the range for random integers
lower_limit = 1
upper_limit = 100

# Generate 100 random integers and store them in a list
random_integers = [random.randint(lower_limit, upper_limit) for _ in range(100)]

# Print the generated random integers
print(random_integers)