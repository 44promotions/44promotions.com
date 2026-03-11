import pandas as pd
import json

path = r'D:\Openclaw-Local\44promotions.com\新品资料 2026. 1. 6\新品资料 2026. 1. 6\44promotions260310日281新品调整格式.xlsx'
df = pd.read_excel(path)

# Category mapping (8 categories)
cat_map = {
    'COSMETIC BAGS': 'Bags & Travel', 'Bags-General': 'Bags & Travel', 'Backpacks-Laptop': 'Bags & Travel',
    'Backpacks-General': 'Bags & Travel', 'Duffel Bags': 'Bags & Travel', 'DUFFEL BAGS': 'Bags & Travel',
    'Bags-Leather': 'Bags & Travel', 'Tote Bags-Canvas': 'Bags & Travel', 'Tote Bags-Non Woven': 'Bags & Travel',
    'Tote Bags-Grocery': 'Bags & Travel', 'Bags-Shopping': 'Bags & Travel', 'LAPTOP SLEEVES/CASES': 'Bags & Travel',
    'PURSES': 'Bags & Travel', 'Portfolios-Zippered': 'Bags & Travel', 'Pouches-General': 'Bags & Travel',
    'CASES & HOLDERS': 'Bags & Travel', 'JEWELRY BOXES & ROLLS': 'Bags & Travel', 'Signs & Displays-Door Knob': 'Bags & Travel',
    'Carts': 'Bags & Travel', 'STOOLS': 'Bags & Travel', 'SLEEPING BAGS': 'Bags & Travel',
    'Bottles-Insulated': 'Drinkware', 'Bottles-Sport Type': 'Drinkware', 'Bottles-Collapsible': 'Drinkware',
    'TRAVEL MUGS/CUPS': 'Drinkware', 'Cups-General': 'Drinkware', 'Cups-Baby': 'Drinkware',
    'Beverage Holders-General': 'Drinkware', 'Bottles-Spray': 'Drinkware', 'STRAWS': 'Drinkware',
    'ICE BUCKETS': 'Drinkware', 'COOLERS': 'Drinkware', 'WINE ACCESSORIES': 'Drinkware', 'Openers-Bottle': 'Drinkware',
    'Pen & Pencil Holders-General': 'Office', 'BOXES & CASES-PEN & PENCIL': 'Office', 'PENS': 'Office',
    'Pens-General': 'Office', 'Pens-Ballpoint-Stylus': 'Office', 'HIGHLIGHTERS': 'Office', 'SHARPENERS': 'Office',
    'Office Supplies': 'Office', 'Organizers-Cord': 'Office', 'Badge Holders-Retractable': 'Office',
    'VALUABLE PAPER HOLDERS': 'Office', 'ERASERS': 'Office', 'ENVELOPES': 'Office', 'LANYARDS': 'Office',
    'Custom Lapel Pins': 'Office', 'Labels-Weather Resistant': 'Office',
    'Battery Rechargers & Adaptors-Power Banks': 'Tech', 'Battery Rechargers & Adaptors-Wireless QI Charger': 'Tech',
    'Battery Rechargers & Adaptors-General': 'Tech', 'Mobile Accessories-Cables & Cords': 'Tech',
    'Mobile Accessories-Cell Phone Wallets': 'Tech', 'MOUSE PADS': 'Tech', 'Speakers-Wireless': 'Tech',
    'Speakers-Wired': 'Tech', 'Fans-USB': 'Tech', 'Flashlights-Rechargeable': 'Tech',
    'Electronic Devices-General': 'Tech', 'Watches-Analog': 'Tech', 'Picture Frames-Digital': 'Tech',
    'TIMERS': 'Tech', 'HUMIDIFIERS & DEHUMIDIFIERS': 'Tech', 'ALARMS & PROTECTIVE DEVICES': 'Tech',
    'COMPUTER ACCESSORIES': 'Tech',
    'Key Chains-Leather': 'Keychains', 'Key Chains-General': 'Keychains', 'Key Chains-Metal': 'Keychains',
    'Key Chains-With Bottle or Can Opener': 'Keychains', 'Key Chains-With Flashlight and/or Whistle': 'Keychains',
    'BELLS': 'Keychains', 'Clips-Utility-Magnetic': 'Keychains', 'STRAPS': 'Keychains',
    'Towels-Beach': 'Home & Living', 'Towels-Wrap Around': 'Home & Living', 'BLANKETS': 'Home & Living',
    'Mats-General': 'Home & Living', 'BOWLS': 'Home & Living', 'Containers-Food Storage': 'Home & Living',
    'Plates-General': 'Home & Living', 'COOKWARE & BAKEWARE': 'Home & Living', 'Tools-Kitchen-Tongs': 'Home & Living',
    'Tools-Kitchen-Spatulas/Spreaders': 'Home & Living', 'Tools-Kitchen-Slicers & Graters-Cheese': 'Home & Living',
    'Tools-Kitchen-Pizza Accessories': 'Home & Living', 'SCALES': 'Home & Living', 'SOAP': 'Home & Living',
    'CANDLES & INCENSE & POTPOURRI': 'Home & Living', 'LAMPS': 'Home & Living', 'Lights-Night': 'Home & Living',
    'COASTERS & COASTER SETS': 'Home & Living', 'LOCKS': 'Home & Living', 'BUCKETS': 'Home & Living',
    'JARS': 'Home & Living', 'PILLOWS': 'Home & Living', 'BACK SCRATCHERS': 'Home & Living',
    'SCARVES': 'Home & Living', 'Gloves-General': 'Home & Living', 'EARMUFFS': 'Home & Living', 'SLIPPERS': 'Home & Living',
    'Vests-Insulated': 'Home & Living', 'Sweat Shirts-Unisex': 'Home & Living', 'BANDANNAS': 'Home & Living',
    'Stress Relievers-Balls': 'Outdoor & Sports', 'Toys-General': 'Outdoor & Sports', 'INFLATABLES': 'Outdoor & Sports',
    'BEACH BALLS': 'Outdoor & Sports', 'BALLS': 'Outdoor & Sports', 'Games-Sets': 'Outdoor & Sports',
    'POKER SETS': 'Outdoor & Sports', 'Golf Accessories-Sets': 'Outdoor & Sports',
    'Golf Accessories-Putting Cups/Greens': 'Outdoor & Sports', 'GOLF TEES': 'Outdoor & Sports',
    'Sports Equipment & Access.-General': 'Outdoor & Sports', 'Sports Equipment & Access.-Fishing & Hunting': 'Outdoor & Sports',
    'Furniture-Chairs-Beach': 'Outdoor & Sports', 'Pet Items-Bowls & Feeders': 'Outdoor & Sports',
    'Pet Items-Leashes & Collars': 'Outdoor & Sports', 'Pet Items-General': 'Outdoor & Sports',
    'LINT REMOVERS': 'Outdoor & Sports', 'Gauges-Rain': 'Outdoor & Sports', 'SUNGLASSES': 'Outdoor & Sports',
    'Caps & Hats-General': 'Outdoor & Sports', "Caps & Hats-Chef's": 'Outdoor & Sports', 'Caps & Hats-Derby': 'Outdoor & Sports',
    'Caps & Hats-Swimming': 'Outdoor & Sports', 'Wristbands-Sports Type': 'Outdoor & Sports', 'Wristbands-General': 'Outdoor & Sports',
    'Masks-General': 'Outdoor & Sports', 'Masks-Novelty/Halloween': 'Outdoor & Sports', 'GOGGLES': 'Outdoor & Sports',
    'Eyeglasses-3D': 'Outdoor & Sports', 'EYEGLASS CLEANERS': 'Outdoor & Sports', 'Jewelry-Cuff Links & Tie Tacs': 'Outdoor & Sports',
    'DECORATIONS': 'Outdoor & Sports', 'Costumes & Accessories': 'Outdoor & Sports', 'Tobacco Related Products-Ashtrays': 'Outdoor & Sports',
    'Uniforms-Sports': 'Outdoor & Sports', 'Umbrellas-Folding': 'Outdoor & Sports',
    'PILL BOXES & BOTTLES': 'Health & Beauty', 'Beauty Aids-Hair': 'Health & Beauty',
    'MASSAGERS': 'Health & Beauty', 'COMBS': 'Health & Beauty',
}

products = []
for _, row in df.iterrows():
    orig_cat = str(row['Categories']).strip() if pd.notna(row['Categories']) else 'Other'
    new_cat = cat_map.get(orig_cat, 'Other')
    
    images = str(row['Images']) if pd.notna(row['Images']) else ''
    images_list = [img.strip() for img in images.split(',') if img.strip()]
    
    def get_val(col):
        return str(row[col]) if pd.notna(row[col]) else ''
    
    def get_int(col):
        return int(row[col]) if pd.notna(row[col]) else 0
    
    def get_float(col):
        return round(float(row[col]), 2) if pd.notna(row[col]) else 0
    
    product = {
        'id': get_val('SKU'),
        'name': get_val('Name'),
        'short_description': get_val('Short description'),
        'description': get_val('Description'),
        'categories': get_val('Categories'),
        'tags': get_val('Tags'),
        'images1': '/images/' + images_list[0].split('/')[-1] if images_list else '',
        'images2': '/images/' + images_list[1].split('/')[-1] if len(images_list) > 1 else '',
        'color': get_val('color'),
        'material': get_val('material'),
        'product_size': get_val('product size'),
        'imprint_method': get_val('imprint method'),
        'imprint_size': get_val('imprint size'),
        'production_time': get_val('production time'),
        'shipping_dimensions': get_val('shipping dimensions'),
        'shipping_weight': get_val('shipping weight'),
        'unit_per_ctn': get_val('unit per ctn'),
        'price_code': get_val('price code'),
        'product_number': get_val('product number'),
        'qty1': get_int('Qty1'),
        'qty2': get_int('Qty2'),
        'qty3': get_int('Qty3'),
        'qty4': get_int('Qty4'),
        'qty5': get_int('Qty5'),
        'qty6': get_int('Qty6'),
        'price1': get_float('Price1'),
        'price2': get_float('Price2'),
        'price3': get_float('Price3'),
        'price4': get_float('Price4'),
        'price5': get_float('Price5'),
        'price6': get_float('Price6'),
        'imprinting_charges': get_val('Imprinting Charges'),
        'price_includes': get_val('Price Includes:'),
        'category': new_cat,
    }
    products.append(product)

output = 'var products = ' + json.dumps(products, ensure_ascii=False, indent=2) + ';'
with open(r'D:\Openclaw-Local\44promotions.com\products_data.js', 'w', encoding='utf-8') as f:
    f.write(output)

print(f'Saved {len(products)} products with all fields')
print('Fields:', list(products[0].keys()))
