def most_frequent(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq
user_input = input("Enter a string: ")
freq_dict = most_frequent(user_input)
print(freq_dict)
