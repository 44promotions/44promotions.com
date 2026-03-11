with open(r'D:\Openclaw-Local\44promotions.com\product-detail.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update Sign In
content = content.replace('<li><a href="#"><i class="fas fa-user"></i> Sign In</a></li>', '<li><a href="#" onclick="signIn()"><i class="fas fa-user"></i> Sign In</a></li>')

# Update Register
content = content.replace('<li><a href="#">Register</a></li>', '<li><a href="#" onclick="register()">Register</a></li>')

# Update Track Order
content = content.replace('<li><a href="#">Track Order</a></li>', '<li><a href="#" onclick="trackOrder()">Track Order</a></li>')

# Update Share
content = content.replace('<li><a href="#"><i class="fas fa-share-alt"></i> Share</a></li>', '<li><a href="#" onclick="shareProduct()"><i class="fas fa-share-alt"></i> Share</a></li>')

# Update Email
content = content.replace('<li><a href="#"><i class="far fa-envelope"></i> Email</a></li>', '<li><a href="#" onclick="emailProduct()"><i class="far fa-envelope"></i> Email</a></li>')

# Update Add to Cart
content = content.replace('<button type="button" class="btn btn-add-cart">Add to Cart</button>', '<button type="button" class="btn btn-add-cart" onclick="addToCart()">Add to Cart</button>')

# Update Request Quote
content = content.replace('<button type="button" class="btn btn-request-quote">Request Quote</button>', '<button type="button" class="btn btn-request-quote" onclick="requestQuote()">Request Quote</button>')

# Update Request Info
content = content.replace('<button type="button" class="btn btn-request-info">Request Info</button>', '<button type="button" class="btn btn-request-info" onclick="requestInfo()">Request Info</button>')

with open(r'D:\Openclaw-Local\44promotions.com\product-detail.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Buttons updated!')
