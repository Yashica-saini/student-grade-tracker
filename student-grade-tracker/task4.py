# essay given in the assignment

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "
# Step 1: remove extra spaces from beginning and end
clean_essay = essay.strip()
print("1. Essay after stripping whitespace:")
print(clean_essay)

# Step 2: convert to title case
title_version = clean_essay.title()
print("\n2. Essay in Title Case:")
print(title_version)

# Step 3: count how many times 'python' appears
python_count = clean_essay.count("python")
print("\n3. Number of times 'python' appears:", python_count)

# Step 4: replace 'python' with 'Python '
replaced_essay = clean_essay.replace("python", "Python ")

print("\n4. Essay after replacing 'python':")
print(replaced_essay)
# Step 5: split essay into sentences
sentences = clean_essay.split(". ")
print("\n5. Sentences as a list:")
print(sentences)

# Step 6: print each sentence with numbering
print("\n6. Numbered Sentences:")
for i in range(len(sentences)):
    sentence = sentences[i]
    if not sentence.endswith("."):
        sentence = sentence + "."
    print(f"{i+1}. {sentence}")