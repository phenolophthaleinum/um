import json
import regex as re

# wziete stad: https://github.com/coldner/wulgaryzmy/blob/master/wulgaryzmy.json
with open('wulgaryzmy.json', 'r', encoding='utf-8') as f:
    database = json.load(f)
# print(database)
text = "Ziombro, kurwo jebana przestań mi rodzinę prześladować, śmierdzielu"
print(text)
regex = re.compile('|'.join(re.escape(x) for x in database))
# print(re.findall(regex, text))
censored_text = re.sub(regex, '---', text)
print(censored_text)
final_censored = re.sub(r'[-]+\w', '---', censored_text)
print(final_censored)

