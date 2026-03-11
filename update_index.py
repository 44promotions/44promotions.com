with open(r'D:\Openclaw-Local\44promotions.com\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add functions before </script>
functions = '''

// Button Functions
function toggleCategories() {
    alert('Categories dropdown - use category cards below to filter');
}

function filterByCategory(category) {
    window.location.href = 'products.html?category=' + encodeURIComponent(category);
}

function viewProduct(id) {
    window.location.href = 'product-detail.html?id=' + id;
}

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

function searchProducts() {
    const query = document.getElementById('searchInput').value;
    if (query) {
        window.location.href = 'products.html?search=' + encodeURIComponent(query);
    }
}

function signIn() {
    alert('Sign In\\n\\nThis feature is coming soon!');
}

function register() {
    alert('Register\\n\\nThis feature is coming soon!');
}

function addToCart() {
    alert('Add to Cart\\n\\nThis feature is coming soon!');
}

function goToWishlist() {
    alert('Wishlist\\n\\nThis feature is coming soon!');
}

// Update header buttons
document.getElementById('searchInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        searchProducts();
    }
});
'''

# Find where to add functions
if '// Button Functions' not in content:
    content = content.replace('</script>', functions + '</script>')

# Update button onclick events
content = content.replace('<a href="#">Track Order</a>', '<a href="#" onclick="trackOrder()">Track Order</a>')
content = content.replace('<a href="#">Contact Us</a>', '<a href="#" onclick="contactUs()">Contact Us</a>')
content = content.replace('<a href="#"><i class="far fa-heart"></i></a>', '<a href="#" onclick="goToWishlist()"><i class="far fa-heart"></i></a>')
content = content.replace('<a href="#"><i class="far fa-user"></i></a>', '<a href="#" onclick="signIn()"><i class="far fa-user"></i></a>')
content = content.replace('<a href="#"><i class="fas fa-shopping-cart"></i></a>', '<a href="#" onclick="addToCart()"><i class="fas fa-shopping-cart"></i></a>')

with open(r'D:\Openclaw-Local\44promotions.com\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('index.html updated!')
