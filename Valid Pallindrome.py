# Valid Pallindrome

def valid_pallindrome(string_test):
    clean_string = ''.join(char.lower() for char in string_test if char.isalnum())

    left = 0
    right = len(clean_string) - 1   

    while left < right:
        if clean_string[left] != clean_string[right]:
            return False
        
        left += 1
        right -= 1
    
    return True

if __name__ == "__main__":
    print(valid_pallindrome("racecare"))