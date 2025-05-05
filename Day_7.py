s = "  hello  "
print(s.strip())  # Output: "hello"
print(s)

text = "I love Java"
print(text.replace("love", "hate"))  # Output: I love Python

data = "apple,banana,mango"
text = "i am a human + who is + trying + to + learn + python"
life = print(text.strip("+"))  # Output: ['i am a human ', ' who is ', ' trying ', ' to ', ' learn ', ' python']
print(text.split("+"))  # Output: ['apple', 'banana', 'mango']

fruits = ['apple', 'banana', 'mango']
print(", ".join(fruits))  # Output: "apple, banana, mango"

def clean_text(blog):
    blog = blog.strip()
    blog = blog.replace("teh", "the")
    words = blog.split()
    cleaned = " ".join(words)
    return cleaned

text = input("Enter your blog post: ")
print("Cleaned Blog:", clean_text(text))


spells = ["  FireBall ", "ICE blast", "dark_VEIL"]

# Clean spell names
cleaned_spells = []
for spell in spells:
    spell = spell.strip().replace("_", " ").title()
    cleaned_spells.append(spell)

print("Your Spellbook:")
for s in cleaned_spells:
    print("-", s)
