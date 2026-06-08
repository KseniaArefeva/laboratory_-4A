from collections import Counter
import string

def word_frequency(text: str) -> dict:
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    text_cleaned = text.translate(translator)
    
    words = text_cleaned.lower().split()
    return dict(Counter(words))

text = input("Введите текст: ")

freq = word_frequency(text)

print("\nРЕЗУЛЬТАТ (знаки препинания удалены):")
print("-" * 35)
for word, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
    print(f"  '{word}': {count}")
print(f"\nВсего уникальных слов: {len(freq)}")
