a = 5+3
b = 5-3
c = 5*3
d = 5/3
print(f"{a}\n{b}\n{c}\n{d}")

"""---------------------------"""

new_bicycle = []

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-2:4])
for cycle in bicycles:
    new_bicycle.append(cycle.title())

print(new_bicycle)
print("-----------------------------------------")

# The English alphabet has 26 lowercase letters.
letters_in_alphabet = 26

# The desired length of the password.
password_length = 3

# For each position in the password, there are 26 independent choices.
# So, the total number of combinations is 26 * 26 * 26.
# This can be calculated as 26 to the power of 3.
total_combinations = letters_in_alphabet ** password_length

print(f"For a password with {password_length} lowercase English letters, there are {total_combinations} possible combinations.")


