import gdown
import timeit

# Завантаження файлів
url1 = 'https://drive.google.com/file/d/18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh/view?usp=sharing'
output1 = 'article_1.txt'
gdown.download(url1, output1, quiet=False)

url2 = 'https://drive.google.com/file/d/13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ/view?usp=sharing'
output2 = 'article_2.txt'
gdown.download(url2, output2, quiet=False)

# Функція для пошуку підрядка за допомогою алгоритму Боєра-Мура
def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    last = {}  # Зберігає останні входження символів з підрядка
    for i in range(m):
        last[pattern[i]] = i
    i = m - 1  # індекс в тексті
    k = m - 1  # індекс в підрядку
    while i < n:
        if text[i] == pattern[k]:
            if k == 0:
                return i  # Знайдено збіг
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(text[i], -1)  # Останнє входження символу в підрядку
            i += m - min(k, j + 1)
            k = m - 1  # Почати співпадіння знову
    return -1  # Збіг не знайдено

# Функція для пошуку підрядка за допомогою алгоритму Кнута-Морріса-Пратта
def knuth_morris_pratt(text, pattern):
    def compute_prefix_function(pattern):
        m = len(pattern)
        pi = [0] * m
        k = 0
        for q in range(1, m):
            while k > 0 and pattern[k] != pattern[q]:
                k = pi[k - 1]
            if pattern[k] == pattern[q]:
                k += 1
            pi[q] = k
        return pi

    n = len(text)
    m = len(pattern)
    pi = compute_prefix_function(pattern)
    q = 0
    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q - 1]
        if pattern[q] == text[i]:
            q += 1
        if q == m:
            return i - m + 1
    return -1

# Функція для пошуку підрядка за допомогою алгоритму Рабіна-Карпа
def rabin_karp(text, pattern):
    def hash_func(s):
        return sum(ord(s[i]) * 256 ** (len(s) - i - 1) for i in range(len(s)))

    n = len(text)
    m = len(pattern)
    pattern_hash = hash_func(pattern)
    text_hash = hash_func(text[:m])
    for i in range(n - m + 1):
        if text_hash == pattern_hash:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            text_hash = hash_func(text[i + 1:i + m + 1])
    return -1

# Підрядки для пошуку
existing_pattern = "існуючий_підрядок"
non_existing_pattern = "неіснуючий_підрядок"

# Читаємо файли з кодуванням CP1251
with open(output1, 'r', encoding='cp1251') as file:
    article1 = file.read()

with open(output2, 'r', encoding='cp1251') as file:
    article2 = file.read()

# Виконання пошуку підрядка у першому файлі для кожного алгоритму
time_boyer_moore_existing = timeit.timeit(lambda: boyer_moore(article1, existing_pattern), number=1)
time_knuth_morris_pratt_existing = timeit.timeit(lambda: knuth_morris_pratt(article1, existing_pattern), number=1)
time_rabin_karp_existing = timeit.timeit(lambda: rabin_karp(article1, existing_pattern), number=1)

time_boyer_moore_non_existing = timeit.timeit(lambda: boyer_moore(article1, non_existing_pattern), number=1)
time_knuth_morris_pratt_non_existing = timeit.timeit(lambda: knuth_morris_pratt(article1, non_existing_pattern), number=1)
time_rabin_karp_non_existing = timeit.timeit(lambda: rabin_karp(article1, non_existing_pattern), number=1)

# Виконання пошуку підрядка у другому файлі для кожного алгоритму
time_boyer_moore_existing_2 = timeit.timeit(lambda: boyer_moore(article2, existing_pattern), number=1)
time_knuth_morris_pratt_existing_2 = timeit.timeit(lambda: knuth_morris_pratt(article2, existing_pattern), number=1)
time_rabin_karp_existing_2 = timeit.timeit(lambda: rabin_karp(article2, existing_pattern), number=1)

time_boyer_moore_non_existing_2 = timeit.timeit(lambda: boyer_moore(article2, non_existing_pattern), number=1)
time_knuth_morris_pratt_non_existing_2 = timeit.timeit(lambda: knuth_morris_pratt(article2, non_existing_pattern), number=1)
time_rabin_karp_non_existing_2 = timeit.timeit(lambda: rabin_karp(article2, non_existing_pattern), number=1)

# Вивід результатів
print("Час виконання для першого файлу:")
print(f"Boyer-Moore (існуючий підрядок): {time_boyer_moore_existing}")
print(f"Knuth-Morris-Pratt (існуючий підрядок): {time_knuth_morris_pratt_existing}")
print(f"Rabin-Karp (існуючий підрядок): {time_rabin_karp_existing}")
print()
print(f"Boyer-Moore (неіснуючий підрядок): {time_boyer_moore_non_existing}")
print(f"Knuth-Morris-Pratt (неіснуючий підрядок): {time_knuth_morris_pratt_non_existing}")
print(f"Rabin-Karp (неіснуючий підрядок): {time_rabin_karp_non_existing}")
print()
print("Час виконання для другого файлу:")
print(f"Boyer-Moore (існуючий підрядок): {time_boyer_moore_existing_2}")
print(f"Knuth-Morris-Pratt (існуючий підрядок): {time_knuth_morris_pratt_existing_2}")
print(f"Rabin-Karp (існуючий підрядок): {time_rabin_karp_existing_2}")
print()
print(f"Boyer-Moore (неіснуючий підрядок): {time_boyer_moore_non_existing_2}")
print(f"Knuth-Morris-Pratt (неіснуючий підрядок): {time_knuth_morris_pratt_non_existing_2}")
print(f"Rabin-Karp (неіснуючий підрядок): {time_rabin_karp_non_existing_2}")
