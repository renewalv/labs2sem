def compute_lps_array(needle: str) -> list[int]:
    """Обчихлює масив LPS"""
    m = len(needle)
    lps = [0] * m
    length = 0 
    i = 1

    while i < m:
        if needle[i] == needle[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(haystack: str, needle: str) -> list[int]:
    """Шукає всі індекси входжень стрічки needle в стрічку haystack за допомогою КМП
    """
    if not needle:
        return []

    n = len(haystack)
    m = len(needle)
    lps = compute_lps_array(needle)
    indices = []  
    
    i = 0  
    j = 0 

    while i < n:
        if needle[j] == haystack[i]:
            i += 1
            j += 1

        if j == m:
            indices.append(i - j)
            j = lps[j - 1]
        
        elif i < n and needle[j] != haystack[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
                
    return indices

if __name__ == "__main__":
    text = "ABABDABACDABABCABAB"
    pattern = "ABAB"
    
    result = kmp_search(text, pattern)
    
    print(f"Текст:   {text}")
    print(f"Шаблон: {pattern}")
    print(f"Індекси всіх входжень: {result}")
    
    for index in result:
        print(f"Збіг на індексі {index}: '{text[index:index+len(pattern)]}'")