essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# 1. Remove leading and trailing whitespace from the essay
cleaned_essay = essay.strip()
print("1. Cleaned Essay:")
print(cleaned_essay)
print("\n")

# 2. Convert the essay to title case (capitalize the first letter of each word)
title_case_essay = cleaned_essay.title()
print("2. Title Case Essay:")
print(title_case_essay)
print("\n")

# 3. Count the number of "python" words in the essay
python_count = cleaned_essay.lower().count("python")
print(f"3. Number of 'python' words in the essay: {python_count}")
print("\n")

# 4. Replace all occurrences of "python" with "Python 🐍"
modified_essay = cleaned_essay.replace("python", "Python 🐍")
print("4. Modified Essay:")
print(modified_essay)
print("\n")

# 5. Split the essay into sentences to produce a list of sentenses.
sentences = cleaned_essay.split(". ")
print("5. Sentences List:") 
print(sentences)
print("\n")

# 6. Print each sentence in a new line.
print("6. Sentences in New Lines:")
for i, sentence in enumerate(sentences, 1):     # add "." at the end of each sentence if it doesn't already end with it
    if not sentence.endswith("."):
        sentence += "."
        
    print(f"Sentence {i}: {sentence}")