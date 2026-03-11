import re
import os

files = ['index.html', 'products.html', 'product-detail.html', 'login.html', 'register.html', 'track-order.html', 'about.html', 'faq.html', 'shipping.html', 'returns.html', 'wishlist.html', 'cart.html']

# Find all .html links
all_links = set()
for f in files:
    with open(f'D:\\Openclaw-Local\\44promotions.com\\{f}', 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        # Simple regex
        links = re.findall(r'href="([^"]+\.html)', content)
        for link in links:
            all_links.add(link)

print('All HTML links found:')
for link in sorted(all_links):
    print(f'  {link}')

print(f'\nTotal: {len(all_links)} links')

# Check which files exist
existing_files = set(os.listdir('D:\\Openclaw-Local\\44promotions.com\\'))
existing_files = {f for f in existing_files if f.endswith('.html')}

print('\n--- Checking if all links point to existing files ---')
broken = []
for link in all_links:
    if link not in existing_files:
        broken.append(link)
        print(f'BROKEN: {link}')

if broken:
    print(f'\n{len(broken)} BROKEN links found!')
else:
    print('\nAll links are valid!')
