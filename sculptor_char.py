""" create a function that receives a string. 
It returns a new string changing the odd letters to lower case and pair 
to uppercase. It does not change any other chars. """

def transform_alpha_only(text):
    result = []
    alpha_count = 0  # This counter only tracks letters
    
    for char in text:
        if char.isalpha():
            # Check the counter we're managing manually
            if alpha_count % 2 == 0:
                result.append(char.upper())
            else:
                result.append(char.lower())
            
            # Increment only after processing a letter
            alpha_count += 1
        else:
            # For non-alpha chars, just append and DON'T increment alpha_count
            result.append(char)
            
    return "".join(result)