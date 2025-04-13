import sqlite3 as sql

conn = sql.connect('Sales.db')

cursor = conn.cursor()

# table creation

# Customers
create_customers = """
CREATE TABLE Customers(
customer_id INT PRIMARY KEY,
first_name VARCHAR(25),
last_name VARCHAR(25),
phone VARCHAR(20),
email VARCHAR(30),
street VARCHAR(50),
city VARCHAR(25),
state VARCHAR(20),
zip_code INT
);
"""

# Stores
create_store = """
CREATE TABLE Stores (
    store_id INT PRIMARY KEY,
    store_name VARCHAR(25),
    phone VARCHAR(25),
    email VARCHAR(25),
    street VARCHAR(50),
    city VARCHAR(25),
    state VARCHAR(25),
    zip_code INT
);
"""

# Staffs
create_staff = """
CREATE TABLE Staffs (
    staff_id INT PRIMARY KEY,
    first_name VARCHAR(25),
    last_name VARCHAR(25),
    email VARCHAR(25),
    phone VARCHAR(25),
    active BOOLEAN,
    store_id INT,
    manager_id INT,
    FOREIGN KEY (store_id) REFERENCES Stores(store_id),
    FOREIGN KEY (manager_id) REFERENCES Staffs(staff_id)
);
"""

# Brands
create_brands = """
CREATE TABLE Brands (
    brand_id INT PRIMARY KEY,
    brand_name VARCHAR(25)
);
"""

# Categories
create_categories = """
CREATE TABLE Categories (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(25)
);
"""

# Products
create_products = """
CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(25),
    brand_id INT,
    category_id INT,
    model_year INT,
    list_price DECIMAL(10,2),
    FOREIGN KEY (brand_id) REFERENCES Brands(brand_id),
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);
"""

# Stocks 
create_stocks = """
CREATE TABLE Stocks (
    store_id INT,
    product_id INT,
    quantity INT,
    PRIMARY KEY (store_id, product_id),
    FOREIGN KEY (store_id) REFERENCES Stores(store_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);
"""

# Orders
create_orders = """
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_status INT,
    order_date DATE,
    required_date DATE,
    shipped_date DATE,
    store_id INT,
    staff_id INT,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (store_id) REFERENCES Stores(store_id),
    FOREIGN KEY (staff_id) REFERENCES Staffs(staff_id)
);
"""

# Discount
create_order_item = """
CREATE TABLE OrderItems (
    order_id INT,
    item_id INT,
    product_id INT,
    quantity INT,
    list_price DECIMAL(10,2),
    discount DECIMAL(4,2),
    PRIMARY KEY (order_id, item_id),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);
"""

queries = [create_brands, create_categories, create_customers, create_order_item, create_orders, create_products, create_stocks, create_store, create_staff]

for q  in queries:
    cursor.execute(q)

conn.commit()
conn.close()