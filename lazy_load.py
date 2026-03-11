import os

os.chdir(r'D:\Openclaw-Local\44promotions.com')

files = ['index.html', 'products.html', 'product-detail.html']

for f in files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()

        # Add lazy loading
        content = content.replace('<img src=', '<img loading="lazy" src=')

        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'{f} updated')
