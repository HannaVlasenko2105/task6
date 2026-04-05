from urllib.parse import unquote
import pyperclip

encoded = input("Введіть закодоване посилання: ")

decoded = unquote(encoded)

print(f"\nЗакодоване посилання:  {encoded}")
print(f"Розкодоване посилання:  {decoded}")

pyperclip.copy(decoded)

print("\nПосилання скопійовано в буфер обміну!")