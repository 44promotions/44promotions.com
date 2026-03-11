with open(r'D:\Openclaw-Local\44promotions.com\products.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update footer links in products.html
content = content.replace("alert('About Us\\n\\nComing soon!')", "window.location.href='about.html'")
content = content.replace("alert('FAQ\\n\\nComing soon!')", "window.location.href='faq.html'")
content = content.replace("alert('Shipping Info\\n\\nComing soon!')", "window.location.href='shipping.html'")
content = content.replace("alert('Returns\\n\\nComing soon!')", "window.location.href='returns.html'")

with open(r'D:\Openclaw-Local\44promotions.com\products.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('products.html footer links updated!')
