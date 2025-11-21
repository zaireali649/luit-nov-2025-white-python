# -----------------------------
# Imports (always at the top)
# -----------------------------
import random
import os
import sys
import math
import matplotlib.pyplot as plt
import pyfiglet


# -----------------------------
# 1. Using the random library
# -----------------------------
number = random.randint(0, 10)
print("Random number:", number)


# -----------------------------
# 2. Using the os library
# -----------------------------
current_dir = os.getcwd()
print("Current working directory:", current_dir)


# -----------------------------
# 3. Using the sys library
# -----------------------------
print("Python version:", sys.version)


# -----------------------------
# 4. Using the math library
# -----------------------------
sqrt_value = math.sqrt(16)
print("Square root of 16:", sqrt_value)

circle_area = math.pi * (5 ** 2)
print("Area of a circle with radius 5:", circle_area)


# -----------------------------
# 5. Using matplotlib (simple plot)
# -----------------------------
x = [0, 1, 2, 3]
y = [0, 2, 4, 6]

plt.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()


# -----------------------------
# 6. Using pyfiglet (ASCII art)
# -----------------------------
ascii_banner = pyfiglet.figlet_format("Python!")
print(ascii_banner)


# -----------------------------
# 7. String manipulation examples
# -----------------------------
text = " Python is FUN! "

print("Stripped:", text.strip())
print("Lowercase:", text.lower())
print("Uppercase:", text.upper())
print("Replace FUN → AWESOME:", text.replace("FUN", "AWESOME"))

split_text = text.split()
print("Split into words:", split_text)

print("Join:", " ".join(split_text))

print("Subset:", text[:5])