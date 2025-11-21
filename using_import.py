# -----------------------------
# Imports (always at the top)
# -----------------------------

import random               # Provides random number functions
import os                   # Allows interaction with the operating system (paths, dirs, etc.)
import sys                  # Gives access to system-related info (Python version, argv, etc.)
import math                 # Includes mathematical functions like sqrt, pi, etc.
import matplotlib.pyplot as plt   # Used for plotting graphs and visualizations
import pyfiglet             # Generates ASCII art from text


# -----------------------------
# 1. Using the random library
# -----------------------------

# Generate a random integer between 0 and 10
number = random.randint(0, 10)

# Print the randomly generated number
print("Random number:", number)


# -----------------------------
# 2. Using the os library
# -----------------------------

# Get the current working directory (folder where this file is running)
current_dir = os.getcwd()

# Print the working directory path
print("Current working directory:", current_dir)


# -----------------------------
# 3. Using the sys library
# -----------------------------

# Print the version of Python currently running this script
print("Python version:", sys.version)


# -----------------------------
# 4. Using the math library
# -----------------------------

# Calculate and print the square root of 16
sqrt_value = math.sqrt(16)
print("Square root of 16:", sqrt_value)

# Calculate area of a circle with radius 5 using pi * r^2
circle_area = math.pi * (5 ** 2)
print("Area of a circle with radius 5:", circle_area)


# -----------------------------
# 5. Using matplotlib (simple plot)
# -----------------------------

# Define x and y values for the graph
x = [0, 1, 2, 3]
y = [0, 2, 4, 6]

# Plot a simple line graph using x and y
plt.plot(x, y)

# Add a title and axis labels
plt.title("Simple Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# Display the graph window
plt.show()


# -----------------------------
# 6. Using pyfiglet (ASCII art)
# -----------------------------

# Create ASCII art text from the word "Python!"
ascii_banner = pyfiglet.figlet_format("Python!")

# Print the ASCII art to the terminal
print(ascii_banner)


# -----------------------------
# 7. String manipulation examples
# -----------------------------

# Example string with extra spaces
text = " Python is FUN! "

# Remove leading and trailing whitespace
print("Stripped:", text.strip())

# Convert the string to lowercase
print("Lowercase:", text.lower())

# Convert the string to uppercase
print("Uppercase:", text.upper())

# Replace a word inside the string
print("Replace FUN → AWESOME:", text.replace("FUN", "AWESOME"))

# Split string into a list of words based on spaces
split_text = text.split()
print("Split into words:", split_text)

# Join a list of words back into a single string
print("Join:", " ".join(split_text))

# Show only the first 5 characters of the string
print("Subset:", text[:5])
