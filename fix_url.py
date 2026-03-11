import re

with open(r'D:\Openclaw-Local\44promotions.com\products_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix to correct format: gh/44promotions/44promotions-images@master/L-首图/
old = 'gh/44promotions/44promotions-images/'
new = 'gh/44promotions/44promotions-images@master/L-%E9%A6%96%E5%9B%BE/'

content = content.replace(old, new)

with open(r'D:\Openclaw-Local\44promotions.com\products_data.js', 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
match = re.search(r'images1.*?cdn\.jsdelivr\.net[^\"]+', content)
print('Updated URL:', match.group()[:80] if match else 'Not found')
