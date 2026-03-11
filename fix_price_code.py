import re
with open(r'D:\Openclaw-Local\44promotions.com\product-detail.html', 'r', encoding='utf-8') as f:
    content = f.read()

old = '<!-- Price Code -->\n<p style="margin-bottom:15px;font-size:13px;"><strong>Price Code:</strong> <span id="priceCode" style="color:#666;"></span></p>\n\n<!-- Price Grid -->'

new = '<!-- Price Code - above price table, right aligned -->\n<div style="text-align:right;margin-bottom:8px;"><span id="priceCode" style="color:#666;font-size:13px;"></span></div>\n\n<!-- Price Grid -->'

content = content.replace(old, new)

with open(r'D:\Openclaw-Local\44promotions.com\product-detail.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')
