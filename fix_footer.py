with open(r'D:\Openclaw-Local\44promotions.com\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix footer links in index.html
content = content.replace('<li><a href="#">About Us</a></li>', '<li><a href="#" onclick="alert(\'About Us\\n\\nThis feature is coming soon!\')">About Us</a></li>')
content = content.replace('<li><a href="#">Products</a></li>', '<li><a href="#" onclick="goProducts()">Products</a></li>')
content = content.replace('<li><a href="#">Contact</a></li>', '<li><a href="#" onclick="contactUs()">Contact</a></li>')

with open(r'D:\Openclaw-Local\44promotions.com\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('index.html footer fixed!')
