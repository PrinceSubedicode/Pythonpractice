name = "Prince"

print(len(name))
print(name.endswith("ince"))

s = "  Hello World  "

print(s.strip())         # "Hello World"
print(s.upper())         # "HELLO WORLD"
print(s.count("l"))      # 3
print(s.replace("World", "Python"))  # "  Hello Python  "
print("Python".zfill(10))  # "0000Python"
