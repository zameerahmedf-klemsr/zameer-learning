with open("sample.txt", "r") as file:
    text = file.read()
lines = text.split("\n")
total_lines = len(lines)
words = text.split()
total_words = len(words)

total_characters = len(text)

word_count = {}

for word in words:
    word = word.lower().strip(".,!?\"'()")
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

top_5 = sorted_words[:5]

print("=== Text Analysis Report ===")
print("File: sample.txt")
print("Total Words:", total_words)
print("Total Lines:", total_lines)
print("Total Characters:", total_characters)

print("\nTop 5 Most Used Words:")
for i, (word, count) in enumerate(top_5, start=1):
    print(f"{i}. {word} - {count} times")