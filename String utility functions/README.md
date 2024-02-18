# Session 2: Strings
This session will be focusing on basic string handling.  

For example, slicing strings, stripe, find etc.  
You can check this Python official documentation link for more string methods：  
https://docs.python.org/3/library/stdtypes.html#string-methods

# Excercise

Create a Python program that decodes a secret message by performing various string manipulations.

Hints:
1. Provide a secret message (a string) that includes hidden information, such as a sentence or phrase with different cases and characters.
2. Perform the following operations on the given secret message:
    a) Convert the entire message to lowercase.  
    b) Replace all spaces with a special character (e.g., "-").  
    c) Use slicing to extract a portion of the message.  
    d) Find a specific word or phrase within the modified message.  
    e) Count the occurrences of a particular character within the modified message.  
    f) Display the modified message, the extracted portion, the location of the specific word/phrase, and the count of a chosen character.

------------------------------------------------------------------------
Sample Output:  
(Let's assume the secret message is: "The SecRet MessaGe HoLds The Key.")  

Original message: The SecRet MessaGe HoLds The Key.  
Lowercase message: the secret message holds the key.  
Modified message: the-secret-message-holds-the-key.  
Extracted portion: secret-message-holds-the  
Location of 'secret': Found at index 4.  
Character 'e' count: 8  
