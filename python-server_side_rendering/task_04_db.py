import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)

def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def read_sql(product_id=None):
    products = []
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row  # Bu sətir nəticələri lüğət (dict) kimi almağa imkan verir
        cursor = conn.cursor()
        
        if product_id:
            cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))
        else:
            cursor.execute('SELECT * FROM Products')
            
        rows = cursor.fetchall()
        for row in rows:
            products.append(dict(row))
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    products = []
    error = None

    # Mənbə seçimi
    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    elif source == 'sql':
        products = read_sql()
    else:
        return render_template('product_display.html', error="Wrong source")

    # ID-yə görə filtrləmə (JSON və CSV üçün köhnə məntiq)
    if product_id and source in ['json', 'csv']:
        try:
            target_id = int(product_id)
            products = [p for p in products if p['id'] == target_id]
        except ValueError:
            error = "Invalid ID format"

    # SQL üçün xüsusi ID filtrləməsi (read_sql funksiyasında artıq edilib, sadəcə yoxlayırıq)
    if product_id and source == 'sql':
        try:
            products = read_sql(int(product_id))
        except ValueError:
            error = "Invalid ID format"

    # Məhsul tapılmadıqda xəta mesajı
    if not products and not error:
        error = "Product not found"

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
