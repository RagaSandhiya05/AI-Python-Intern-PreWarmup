# T05 - Python Data Structures


#1. Read a Paragraph
paragraph = input("Enter a paragraph: ")


#2. Convert Words to Lowercase and Clean Punctuation
import string

cleaned_paragraph = paragraph.lower().translate(
    str.maketrans("", "", string.punctuation)
)

words = cleaned_paragraph.split()


#3. Store Words in a List
word_list = list(words)

print("\nTotal words:", len(word_list))


#4. Use a Set to Find Unique Words
unique_words = set(word_list)

print("Unique words:", len(unique_words))


#5. Use a Dictionary to Count Word Frequencies
word_frequency = {}

for word in word_list:
    word_frequency[word] = word_frequency.get(word, 0) + 1


#6. Use a Tuple to Store Word-Frequency Pairs
frequency_items = list(word_frequency.items())


#7. Sort Words by Frequency
sorted_words = sorted(
    frequency_items,
    key=lambda item: item[1],
    reverse=True
)


#8. Display the Top 5 Most Frequent Words
top_five = sorted_words[:5]

print("\nTop 5 Most Frequent Words:")

for word, frequency in top_five:
    print(f"{word}: {frequency}")


#9. Dictionary Comprehension
top_five_dict = {
    word: frequency
    for word, frequency in top_five
}

print("\nTop 5 Words Dictionary:", top_five_dict)


#10. List Comprehension
long_words = [word for word in word_list if len(word) > 5]

print("\nWords longer than 5 characters:", long_words)
