with open(r'D:\Openclaw-Local\44promotions.com\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and keep only the LAST set of function definitions (after "// Button Functions" comment)
# Split by the comment and keep only the last part

# Remove the first set of duplicate functions (keep the second)
# Looking for the pattern between two "// Additional Functions" or similar

# Simply remove duplicates by keeping only the last occurrence of each function
import re

# Find all function blocks
functions = re.findall(r'function \w+\(\) \{[^}]+\}', content)

# Create a set of unique functions (keeping last occurrence)
seen = {}
for func in reversed(functions):
    name = re.search(r'function (\w+)', func).group(1)
    if name not in seen:
        seen[name] = func

# Now rebuild the content - this is complex, so let's just remove duplicates manually
# by removing the first block

# Find the pattern between two "function toggleCategories"
pattern = r'(// Button Functions.*?)function toggleCategories'
matches = re.findall(pattern, content, re.DOTALL)
if len(matches) > 1:
    # Remove the first occurrence (the duplicate)
    content = content.replace(matches[0], '', 1)

with open(r'D:\Openclaw-Local\44promotions.com\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Removed duplicate functions!')

# Now verify
functions_after = re.findall(r'function \w+\(\)', content)
print(f'Functions now: {len(set(functions_after))} unique functions')
