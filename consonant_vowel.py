vowel_count=0
consonant_count=0
def count_vowels_and_consonants(input_string):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    for i in input_string:
        for j in vowels:
            if (i in input_string == j in vowels):
                vowel_count+=1
        for k in consonants:
            if(i in input_string == k in consonants):
                consonant_count+=1
        
    return vowel_count, consonant_count


input_string = input("Enter a string: ")

vowel_count, consonant_count = count_vowels_and_consonants(input_string)

print(f"\nAnalysis for the string: {input_string}")
print(f"Vowel count: {vowel_count}")
print(f"Consonant count: {consonant_count}")
    
