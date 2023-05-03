def romanToInt(s: str) -> int:
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500,'M': 1000}

    result: int = 0

    for i in range(len(s)):
        if i + 1 < len(s) and roman_numerals[s[i]] < roman_numerals[s[i+1]]:
            result -= roman_numerals[s[i]]
        else:
            result += roman_numerals[s[i]]
    print(result)

romanToInt('MCMXCVIII')


"""
To solve this problem, we will first create a hash map for the keys and values of the roman numerals
Then, initialise a result variable to 0.
loop through the input string to get the index of each element
make sure the the loop doesnt go out of bounds and check if the element at 'i' is less than the element at 'i+1'
if yes then minus element at index 'i' from result
if no then add element at index 'i' to result
return result.
"""