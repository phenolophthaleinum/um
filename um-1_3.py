import regex as re


# example sites read from files
with open("site-github.txt", 'r', encoding='utf-8') as f_big, open("site-gmail.txt", 'r') as f_sm:
    text_big = f_big.read()
    text_small = f_sm.read()
    # print(re.findall(r'.*@.*\.\w+', text))
    output = [re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', text) for text in [text_big, text_small]]
    print(f"site-github: {output[0]},\nsite-gmail: {output[1]}")
