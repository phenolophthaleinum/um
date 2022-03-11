import regex as re


while True:
    name = input("your name: ")
    cmp = re.match(r"^\p{Lu}", name)  # match also polish letters and in upper
    if cmp:
        break
    else:
        print("Must start with capital letter")
        continue

while True:
    fullname = input("your surname: ")
    cmp = re.match(r'^\p{Lu}', fullname)
    if cmp:
        break
    else:
        print("Must start with capital letter")
        continue

while True:
    tel = input("your phone number: ")
    cmp = re.match(r'\(\d{2}\) \d{3}-\d{2}-\d{2}$', tel, flags=re.M)
    if cmp:
        break
    else:
        print("Must be in following format, e.g. (61) 222-45-56")
        continue

while True:
    code = input("your postal code: ")
    cmp = re.match(r'\d{2}-\d{3}$', code)
    if cmp:
        break
    else:
        print("Must be in following format, e.g. 11-111")
        continue

while True:
    city = input("your city: ")
    cmp = re.match(r'^\p{Lu}', city)
    if cmp:
        break
    else:
        print("Must start with capital letter")
        continue
