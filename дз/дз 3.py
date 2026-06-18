import re
from collections import Counter

# --- Наборы букв (только RU и EN) ---
RU_ALPHABET = set("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
EN_ALPHABET = set("abcdefghijklmnopqrstuvwxyz")

RU_VOWELS = set("аеёиоуыэюя")
EN_VOWELS = set("aeiou")


def count_vowels_consonants(text: str):

    vowels = 0
    consonants = 0

    for ch in text.lower():
        if ch in RU_VOWELS or ch in EN_VOWELS:
            vowels += 1
        elif ch in RU_ALPHABET or ch in EN_ALPHABET:
            consonants += 1

    total_letters = vowels + consonants
    vowel_percent = (vowels / total_letters * 100) if total_letters else 0.0
    return vowels, consonants, vowel_percent




def text_analyzer():
    text = input("Введите текст: ")
    cleaned_text = re.sub(r'\s+', ' ', text).strip()

    chars_with_spaces = len(text)
    chars_without_spaces = len(text.replace(" ", ""))

    words = cleaned_text.split() if cleaned_text else []
    word_count = len(words)

    sentences = re.split(r'[.!?]+', cleaned_text)
    sentences = [s.strip() for s in sentences if s.strip()]
    sentence_count = len(sentences)

    words_lower = []
    for w in words:
        clean_word = re.sub(r'^[^\w\s]+|[^\w\s]+$', '', w.lower())
        if clean_word:
            words_lower.append(clean_word)

    word_freq = Counter(words_lower)
    most_common_words = word_freq.most_common(5)

    vowels, consonants, vowel_percent = count_vowels_consonants(text)

    print("\n" + "=" * 50)
    print("СТАТИСТИКА ТЕКСТА:")
    print("=" * 50)

    print(f"-- Символов (с пробелами): {chars_with_spaces}")
    print(f"-- Символов (без пробелов): {chars_without_spaces}")
    print(f"-- Слов: {word_count}")
    print(f"-- Предложений: {sentence_count}")

    print(f"-- Гласных букв: {vowels}")
    print(f"-- Согласных букв: {consonants}")
    print(f"-- Процент гласных: {vowel_percent:.1f}%")

    print(f"\n-- Самые частые слова:")
    if most_common_words:
        for i, (w, f) in enumerate(most_common_words, 1):
            print(f"  {i}. '{w}' — {f} раз(а)")
    else:
        print("  (нет слов для анализа)")

    print("\n" + "-" * 50)
    print("ОЧИЩЕННЫЙ ТЕКСТ:")
    print("-" * 50)
    print(cleaned_text)
    print("=" * 50)


def enhanced_text_analyzer():
    text = input("Введите текст: ")

    cleaned_text = re.sub(r'\s+', ' ', text).strip()
    words = cleaned_text.split() if cleaned_text else []

    print("\n" + "=" * 50)
    print("РАСШИРЕННАЯ СТАТИСТИКА:")
    print("=" * 50)

    unique_words = set(w.lower().strip(".,!?;:\"'()[]{}") for w in words if w.strip(".,!?;:\"'()[]{}"))
    print(f"-- Уникальных слов: {len(unique_words)}")

    if words:
        lens = [len(w.strip(".,!?;:\"'()[]{}")) for w in words if w.strip(".,!?;:\"'()[]{}")]
        avg_word_length = (sum(lens) / len(lens)) if lens else 0
        print(f"-- Средняя длина слова: {avg_word_length:.1f} символов")
    else:
        print(f"-- Средняя длина слова: 0.0 символов")

    if words:
        density = len(cleaned_text.replace(" ", "")) / len(words)
        print(f"-- Плотность текста: {density:.1f} символов/слово")
    else:
        print(f"-- Плотность текста: 0.0 символов/слово")

    uppercase_count = sum(1 for ch in text if ch.isupper())
    uppercase_percent = (uppercase_count / len(text) * 100) if text else 0.0
    print(f"-- Заглавных букв: {uppercase_count} ({uppercase_percent:.1f}%)")

    if words:
        longest_word = max(words, key=lambda w: len(w.strip(".,!?;:\"'()[]{}")))
        lw_len = len(longest_word.strip(".,!?;:\"'()[]{}"))
        print(f"-- Самое длинное слово: '{longest_word}' ({lw_len} символов)")
    else:
        print("-- Самое длинное слово: (нет слов)")

    vowels, consonants, vowel_percent = count_vowels_consonants(text)
    print(f"-- Гласных букв: {vowels}")
    print(f"-- Согласных букв: {consonants}")
    print(f"-- Процент гласных: {vowel_percent:.1f}%")

    print("=" * 50)


if __name__ == "__main__":
    print("=== ПРОСТОЙ АНАЛИЗАТОР ===")
    text_analyzer()

    print("\n=== РАСШИРЕННЫЙ АНАЛИЗАТОР ===")
    enhanced_text_analyzer()
