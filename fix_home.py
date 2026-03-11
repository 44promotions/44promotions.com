with open(r'D:\Openclaw-Local\44promotions.com\products.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<a href="index.html" class="btn btn-outline-secondary rounded-pill d-none d-md-block"><i class="fas fa-home"></i></a>', '<a href="#" onclick="goHome()" class="btn btn-outline-secondary rounded-pill d-none d-md-block"><i class="fas fa-home"></i></a>')

with open(r'D:\Openclaw-Local\44promotions.com\products.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated!')
