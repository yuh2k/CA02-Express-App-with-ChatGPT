# print(ord('A'))

alphabet = [0] * 26

s = "abdjhska"

for c in s:
    alphabet[ord(c) - ord('a')] += 1

print(alphabet)