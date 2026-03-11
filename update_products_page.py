with open(r'D:\Openclaw-Local\44promotions.com\products.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add more functions
functions = '''

// Additional Functions
function goHome() {
    window.location.href = 'index.html';
}

function goProducts() {
    window.location.href = 'products.html';
}

function trackOrder() {
    const orderId = prompt('Please enter your order number:');
    if (orderId) {
        alert('Order tracking for: ' + orderId + '\\n\\nThis feature is coming soon!');
    }
}

function contactUs() {
    window.location.href = 'mailto:info@44promotions.com?subject=Contact Us';
}

function signIn() {
    alert('Sign In\\n\\nThis feature is coming soon!');
}

function addToCart() {
    alert('Add to Cart\\n\\nThis feature is coming soon!');
}

function goToWishlist() {
    alert('Wishlist\\n\\nThis feature is coming soon!');
}

function searchProducts() {
    const query = document.getElementById('searchInput').value;
    if (query) {
        window.location.href = 'products.html?search=' + encodeURIComponent(query);
    }
}

// Update header buttons
document.getElementById('searchInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        searchProducts();
    }
});
'''

# Add functions before </script>
if '// Additional Functions' not in content:
    content = content.replace('</script>', functions + '</script>')

# Update header buttons
content = content.replace('<a href="index.html"><i class="fas fa-home"></i></a>', '<a href="#" onclick="goHome()"><i class="fas fa-home"></i></a>')

with open(r'D:\Openclaw-Local\44promotions.com\products.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('products.html updated!')
