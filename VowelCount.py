def count_vowels(txt):
    vowels = ["a","e","i","o","u"]
    total = 0
    for x in txt:
        if x in vowels:
            total += 1
    print(total)

count_vowels("Mississippi")
