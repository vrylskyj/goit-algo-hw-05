import timeit

# Алгоритм Боєра-Мура
def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return []

    last_occurrence = {}
    for i in range(m - 1):
        last_occurrence[pattern[i]] = i

    result = []
    i = m - 1
    while i < n:
        j = m - 1
        k = i
        while j >= 0 and text[k] == pattern[j]:
            j -= 1
            k -= 1
        if j == -1:
            result.append(i - m + 1)
            i += m
        else:
            last_occ = last_occurrence.get(text[i], -1)
            i += m - min(j, 1 + last_occ)
    return result

# Алгоритм Кнута-Морріса-Пратта
def knuth_morris_pratt(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return []

    lps = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[j] != pattern[i]:
            j = lps[j - 1]
        if pattern[j] == pattern[i]:
            j += 1
        lps[i] = j

    result = []
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
        if text[i] == pattern[j]:
            j += 1
            if j == m:
                result.append(i - m + 1)
                j = lps[j - 1]
    return result

# Алгоритм Рабіна-Карпа
def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return []

    p = 31  # просте число
    d = 256  # кількість символів ASCII
    q = 997  # просте число

    result = []
    h_pattern = 0
    h_text = 0
    h = 1

    for i in range(m - 1):
        h = (h * d) % q
    for i in range(m):
        h_pattern = (d * h_pattern + ord(pattern[i])) % q
        h_text = (d * h_text + ord(text[i])) % q

    for i in range(n - m + 1):
        if h_pattern == h_text:
            if text[i:i + m] == pattern:
                result.append(i)
        if i < n - m:
            h_text = (d * (h_text - ord(text[i]) * h) + ord(text[i + m])) % q
            if h_text < 0:
                h_text += q
    return result

# Функція для вимірювання часу виконання алгоритму для підрядка
def measure_time(algorithm, text, pattern):
    start_time = timeit.default_timer()
    algorithm(text, pattern)
    return timeit.default_timer() - start_time

# Зчитуємо дані з файлів
with open("text1.txt", "r") as file1, open("text2.txt", "r") as file2:
    text1 = file1.read()
    text2 = file2.read()

# Вибираємо підрядки для пошуку
existing_pattern = "example"  # підрядок, який дійсно існує у тексті
fake_pattern = "xyzz"         # вигаданий підрядок

# Створюємо словник для зберігання результатів
results = {}

# Виконуємо алгоритми пошуку підрядка та вимірюємо час для обох текстів та обох підрядків
for algorithm in [boyer_moore, knuth_morris_pratt, rabin_karp]:
    for text_name, text in [("Text 1", text1), ("Text 2", text2)]:
        for pattern_name, pattern in [("Existing pattern", existing_pattern), ("Fake pattern", fake_pattern)]:
            key = f"{algorithm.__name__} - {text_name} - {pattern_name}"
            result = measure_time(algorithm, text, pattern)
            results[key] = result

# Виводимо результати
for key, result in results.items():
    print(key + ":", result)
