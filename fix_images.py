import re

with open('write_catalog.py', 'r', encoding='utf-8') as f:
    txt = f.read()

# Fix 404 image 1: Keyboard photo
txt = txt.replace(
    'https://images.unsplash.com/photo-1525994886773-0805aa7cc1a2?auto=format&fit=crop&w=600&q=80',
    'https://images.unsplash.com/photo-1462965326201-d02e4f455804?auto=format&fit=crop&w=600&q=80'
)

# Fix 404 image 2: Sound 3000W / speaker photo
txt = txt.replace(
    'https://images.unsplash.com/photo-1520523839896-5aa428633bc8?auto=format&fit=crop&w=800&q=80',
    'https://images.unsplash.com/photo-1598488035139-bdbb2231ce04?auto=format&fit=crop&w=800&q=80'
)

with open('write_catalog.py', 'w', encoding='utf-8') as f:
    f.write(txt)

print("Fixed 2 broken image URLs in write_catalog.py")
