with open(r'D:\Openclaw-Local\44promotions.com\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update links in index.html
content = content.replace("alert('Sign In\\n\\nThis feature is coming soon!')", "window.location.href='login.html'")
content = content.replace("alert('Register\\n\\nThis feature is coming soon!')", "window.location.href='register.html'")
content = content.replace("alert('Wishlist\\n\\nThis feature is coming soon!')", "window.location.href='wishlist.html'")
content = content.replace("alert('About Us\\n\\nThis feature is coming soon!')", "window.location.href='about.html'")
content = content.replace("alert('Add to Cart\\n\\nThis feature is coming soon!')", "window.location.href='cart.html'")

with open(r'D:\Openclaw-Local\44promotions.com\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('index.html links updated!')
