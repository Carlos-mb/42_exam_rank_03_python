""" create a function that receives a string. 
It returns a new string changing the odd letters to lower case and pair 
to uppercase. It does not change any other chars. """


def sculptor_char(text):

    result = ""
    alpha_count = 0  # Only counts letters
    
    for char in text:
        if char.isalpha():
            # Check the counter we're managing
            if alpha_count % 2 == 0:
                # Even count -> Uppercase
                result += char.upper()
            else:
                # Odd count -> Lowercase
                result += char.lower()
            
            # Increment ONLY when we process a letter
            alpha_count += 1
        else:
            # Non-alpha chars (spaces, numbers) are added as-is
            # alpha_count does NOT increase here
            result += char
            
    return result
