# Given secret message
secret_message = "The SecRet MessaGe HoLds The Key."

# Convert the message to lowercase
lowercase_message = secret_message.lower()

# Replace spaces with a special character
modified_message = lowercase_message.replace(" ", "-")

# Extract a portion of the message using slicing
extracted_portion = modified_message[4:31]  # Example slicing range

# Find a specific word within the modified message
word_to_find = 'secret'
word_index = modified_message.find(word_to_find)

# Count the occurrences of a particular character
char_to_count = 'e'
char_count = modified_message.count(char_to_count)

# Displaying the results
print("Original message:", secret_message)
print("Lowercase message:", lowercase_message)
print("Modified message:", modified_message)
print("Extracted portion:", extracted_portion)
print(f"Location of '{word_to_find}': Found at index {word_index}.")
print(f"Character '{char_to_count}' count:", char_count)
