import json
import re

# Read current products
with open(r'D:\Openclaw-Local\44promotions.com\products_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Old pattern: gh/44promotions/44promotions-images/FFSAT40041_L.jpg
# New pattern: gh/44promotions/44promotions-images/L-首图/FFSAT40041_L.jpg

# Use raw string replacement
old_pattern = 'gh/44promotions/44promotions-images/'
new_pattern = 'gh/44promotions/44promotions-images/L-%E9%A6%96%E5%9B%BE/'

content = content.replace(old_pattern, new_pattern)

with open(r'D:\Openclaw-Local\44promotions.com\products_data.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed image URLs!')

# Verify first URL
match = re.search(r'images1.*?cdn\.jsdelivr\.net[^\"]+', content)
if match:
    print('New URL example:', match.group()[:120])
