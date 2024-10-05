def custom_soundex(name):
    # Simple Soundex function
    if not name:  # Handle empty or None values
        return '0000'
    # Step 1: Keep the first letter of the string
    first_letter = name[0].upper()

    # Step 2: Remove all occurrences of a, e, i, o, u, y, h, w from the rest of the string
    name = name.lower()
    name = name[1:]  # Skip the first letter
    name = ''.join([char for char in name if char not in 'aeiouyhw'])

    # Step 3: Replace consonants from position 2 onwards with digits
    soundex_mapping = {
        'b': '1', 'f': '1', 'p': '1', 'v': '1',
        'c': '2', 'g': '2', 'j': '2', 'k': '2', 'q': '2', 's': '2', 'x': '2', 'z': '2',
        'd': '3', 't': '3',
        'l': '4',
        'm': '5', 'n': '5',
        'r': '6'
    }

    digits = [soundex_mapping.get(char, '') for char in name]

    # Step 4: Only keep unique adjacent digits
    unique_digits = []
    for i in range(len(digits)):
        if i == 0 or digits[i] != digits[i - 1]:
            unique_digits.append(digits[i])

    # Step 5: Construct the Soundex code (first letter + unique digits)
    soundex_code = first_letter + ''.join(unique_digits)

    # Step 6: Ensure the Soundex code is exactly 4 characters long
    return (soundex_code + '000')[:4]

# Example: Calculate Soundex for "Ashworth" based on the provided rules
 
# res= custom_soundex("Fan")
# print('\n'+res)
# res= custom_soundex("Yue")
# print('\n'+res)

def extract_characters(name, positions, fallback):
    extracted = ''
    for pos in positions:
        if len(name) >= pos:
            extracted += name[pos-1].upper()
        else:
            extracted += fallback  # Use fallback if the name is too short
    return extracted

def slk_581_from_record(rec_values, fam_name_attr_ind, giv_name_attr_ind, dob_attr_ind, gender_attr_ind):
    """Generate SLK-581 key for a given record based on family name, given name,
       date of birth, and gender.
    """
    # Extract family name, given name, date of birth, and gender from the record
    family_name = rec_values[fam_name_attr_ind]
    given_name = rec_values[giv_name_attr_ind]
    dob = rec_values[dob_attr_ind]
    gender = rec_values[gender_attr_ind]

    # Step 1: Take the 2nd, 3rd, and 5th letters of the family name (or use fallback '2')
    family_part = extract_characters(family_name, [2, 3, 5], '2')

    # Step 2: Take the 2nd and 3rd letters of the given name (or use fallback '2')
    given_part = extract_characters(given_name, [2, 3], '2')

    # Step 3: Take the date of birth in ddmmyyyy format
    dob_part = dob  # Should already be in the correct "DDMMYYYY" format

    # Step 4: Take the gender (1=male, 2=female, 9=unknown)
    if gender not in ['1', '2', '9']:
        gender = '9'  # Default to 'unknown' if invalid

    # Combine all parts to form the SLK-581 code
    slk_code = family_part + given_part + dob_part + gender

    return slk_code

 

def slk_581(family_name, given_name, dob, gender):
   
    # Step 1: Take the 2nd, 3rd, and 5th letters of the family name (or use fallback '2')
    family_part = extract_characters(family_name, [2, 3, 5], '2')

    # Step 2: Take the 2nd and 3rd letters of the given name (or use fallback '2')
    given_part = extract_characters(given_name, [2, 3], '2')

    # Step 3: Take the date of birth in ddmmyyyy format (assuming dob is provided as "DDMMYYYY")
    dob_part = dob  # Should be in the correct format "DDMMYYYY"

    # Step 4: Take the gender of the person (1=male, 2=female, 9=unknown)
    if gender not in [1, 2, 9]:
        gender = 9  # Default to 'unknown' if gender is invalid

    # Combine all parts to form the SLK-581 code
    slk_code = family_part + given_part + dob_part + str(gender)

    return slk_code

# Example usage:
given_name = "Fan"
family_name = "Yue"
dob = "05261995"
gender = 1  # Male

slk_code = slk_581(family_name, given_name, dob, gender)
print('\n'+slk_code)
