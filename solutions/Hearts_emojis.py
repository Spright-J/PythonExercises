import unicodedata

heart_list = []

for unicode in range(230000):
    try:
        char_name = unicodedata.name(chr(unicode))
        if 'HEART' in char_name:
            heart_list.append(chr(unicode))
    except ValueError:
        continue

print(''.join(heart_list))