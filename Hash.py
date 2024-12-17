def rabin_karp(pattern, text):
    d = 256  # Количество символов в алфавите (ASCII)
    q = 101  # Простое число для модулярного хеширования

    M = len(pattern)
    N = len(text)
    p = 0  # Хэш-код образца
    t = 0  # Хэш-код текста
    h = 1
    result = []

    for i in range(M - 1):
        h = (h * d) % q

    for i in range(M):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(N - M + 1):
        if p == t:
            if text[i:i + M] == pattern:
                result.append(i)

        if i < N - M:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + M])) % q
            if t < 0:
                t += q

    return result

pattern = input().strip()
text = input().strip()

indices = rabin_karp(pattern, text)

print(" ".join(map(str, indices)))
