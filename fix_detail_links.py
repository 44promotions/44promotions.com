with open(r'D:\Openclaw-Local\44promotions.com\product-detail.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update footer links in product-detail.html
content = content.replace("alert('Sign In\\n\\nThis feature is coming soon!')", "window.location.href='login.html'")
content = content.replace("alert('Register\\n\\nThis feature is coming soon!')", "window.location.href='register.html'")

with open(r'D:\Openclaw-Local\44promotions.com\product-detail.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('product-detail.html footer links updated!')
