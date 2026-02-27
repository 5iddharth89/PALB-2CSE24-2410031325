def isPalindrome(num):
    return str(num) == str(num)[::-1]


def allPalindrome(arr):
    for num in arr:
        if not isPalindrome(num):
            return False
    return True


print(allPalindrome([111,222,333]))
