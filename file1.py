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