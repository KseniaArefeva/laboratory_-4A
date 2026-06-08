"""
WORD FREQUENCY - ВАРИАТИВНАЯ ЧАСТЬ №2
Убирает знаки препинания перед подсчётом частоты слов
"""

from collections import Counter
import string

def word_frequency(text: str) -> dict:
    """Подсчитывает частоту слов, удаляя знаки препинания"""
    # Заменяем знаки препинания на пробелы
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    text_cleaned = text.translate(translator)
    
    # Разбиваем на слова, приводим к нижнему регистру и считаем
    words = text_cleaned.lower().split()
    return dict(Counter(words))

# Ввод текста
text = input("Введите текст: ")

# Подсчёт и вывод
freq = word_frequency(text)

print("\nРЕЗУЛЬТАТ (знаки препинания удалены):")
print("-" * 35)
for word, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
    print(f"  '{word}': {count}")
print(f"\nВсего уникальных слов: {len(freq)}")

# ============================================
# README (сохранится в файл)
# ============================================

readme_content = """# Word Frequency - Вариативная часть №2

## Описание
Программа подсчитывает частоту слов в тексте с **удалением знаков препинания** (вариативная часть №2).

## Функциональность
- Удаляет все знаки препинания (., ! ? ; : " ' ( ) [ ] { } < > @ # $ % ^ & * - + = | \\ / ~)
- Приводит слова к нижнему регистру
- Подсчитывает количество вхождений каждого слова
- Выводит слова, отсортированные по убыванию частоты

## Как использовать
1. Запустите программу
2. Введите текст
3. Получите результат подсчёта

## Пример

**Ввод:**
Hello, world! Hello, world. World is wonderful!

**Вывод:**
РЕЗУЛЬТАТ (знаки препинания удалены):
-----------------------------------
  'world': 3
  'hello': 2
  'is': 1
  'wonderful': 1

Всего уникальных слов: 4

## Требования
- Python 3.6 или выше
- Стандартные библиотеки: collections, string

## Запуск
```bash
python word_frequency.py
