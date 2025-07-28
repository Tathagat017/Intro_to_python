
#count the number of vowels in a string using a list comprehension
s = "A quick browbn fox jumps over the lazy dog"

vowel_count = len([f for f in s if f.lower() in 'aeiou'])

#reverse a string using a list comprehension
reversed_string = s[::-1]
print(f"Reversed string: {reversed_string}")

#unique characters in a string using a set comprehension
unique_chars = {c for c in s if c.isalpha()}
print(f"Unique characters: {unique_chars}")

#flatten a list of lists using a list comprehension
nested_list = [[1, 2, 3], [4, 5], [6]]
flattened_list = [item for sublist in nested_list for item in sublist]

#filter even numbers from a list using a list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]

