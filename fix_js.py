with open(r'D:\Openclaw-Local\44promotions.com\product-detail.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update JS to show price_code value directly
old = "document.getElementById('priceCode').textContent = product.price_code || 'N/A';"
new = "document.getElementById('priceCode').textContent = product.price_code || '';"

content = content.replace(old, new)

with open(r'D:\Openclaw-Local\44promotions.com\product-detail.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('JS updated!')
