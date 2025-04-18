# Coding starts here...
# Define a function to display the string as it is
def display_regular(text):
    print(text)

# Define a function to display the string in uppercase
def display_uppercase(text):
    print(text.upper())

# Define a function to display the string in lowercase
def display_lowercase(text):
    print(text.lower())

# Ask the user for input
message = input("What is your message? ")

# Call each function with the message
display_regular(message)
display_uppercase(message)
display_lowercase(message)
