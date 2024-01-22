def is_palindrome(number):
    """ Check if a number is a palindrome. """
    return str(number) == str(number)[::-1]

def find_palindrome_divisible_by_95():
    palindromes = []
    for b in range(10):
        for c in range(10):
            # Constructing the palindrome number of the form 5bccb5
            num = 500000 + b * 10000 + c * 1000 + c * 100 + b * 10 + 5
            
            # Check if the number is divisible by 95 and the quotient is a palindrome
            if num % 95 == 0 and is_palindrome(num // 95):
                palindromes.append(num)
    
    return palindromes

# Find the palindromes
palindrome_numbers = find_palindrome_divisible_by_95()
print(palindrome_numbers)


