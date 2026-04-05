
def sort_text(words):
    ukrainian = [item for item in words if any('а' <= c.lower() <= 'я' or c.lower() in "єіїґ" for c in item)]
    latin = [item for item in words if item not in ukrainian]

    ukrainian.sort(key=str.lower)
    latin.sort(key=str.lower)

    return ukrainian + latin

with open('prog1.txt', 'r', encoding='utf-8') as f:
    text = f.read()

print("\nВхідний текст:\n")
print(text)

words = [w.strip(".,") for w in text.split()]

sorted_words = sort_text(words)

print("\nВідсортований список слів:\n")
print(sorted_words)
