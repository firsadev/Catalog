import re

with open('write_catalog.py', 'r', encoding='utf-8') as f:
    txt = f.read()

pattern = r'<span class="page-num">\d+</span>'
count = len(re.findall(pattern, txt))
txt = re.sub(pattern, '', txt)

with open('write_catalog.py', 'w', encoding='utf-8') as f:
    f.write(txt)

print(f'Removed {count} page-num spans from write_catalog.py')
