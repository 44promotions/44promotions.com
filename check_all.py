import re
import os

files = ['index.html', 'products.html', 'product-detail.html', 'login.html', 'register.html', 'track-order.html', 'about.html', 'faq.html', 'shipping.html', 'returns.html', 'wishlist.html', 'cart.html']

all_refs = set()

for f in files:
    with open(f'D:\\Openclaw-Local\\44promotions.com\\{f}', 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        
        # href links
        links = re.findall(r'href="([^"]+\.html)', content)
        for link in links:
            all_refs.add(('href', link))
        
        # onclick page redirects
        onclicks = re.findall(r"onclick=[\"'](?:window\.location\.href\s*=\s*|location\s*=\s*)['\"]([^'\"]+\.html)['\"]", content)
        for link in onclicks:
            all_refs.add(('onclick', link))

print('All page references:')
for ref_type, link in sorted(all_refs):
    print(f'  [{ref_type}] {link}')

# Check which files exist
folder = 'D:\\Openclaw-Local\\44promotions.com\\'
existing = set(f for f in os.listdir(folder) if f.endswith('.html'))

print('\n--- Checking validity ---')
broken = []
for ref_type, link in all_refs:
    if link not in existing:
        broken.append((ref_type, link))
        print(f'BROKEN: [{ref_type}] {link}')

if broken:
    print(f'\n{len(broken)} BROKEN links!')
else:
    print('\nAll page references are valid!')

# Check what files exist
print(f'\nExisting HTML files ({len(existing)}):')
for f in sorted(existing):
    print(f'  {f}')
