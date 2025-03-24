import sqlite3

def create_tables():
    con = sqlite3.connect("products.db")
    cursor = con.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS products (id_prod INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, product TEXT, quantity INTEGER)"""
    )
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS quantity_history (
        id_hist INTEGER PRIMARY KEY AUTOINCREMENT,
        prod_hist INTEGER,
        quantity_before INTEGER,
        quantity_after INTEGER,
        data_modify TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (prod_hist) REFERENCES products(id_prod)
        );"""
    )
    con.close()

# Inserir 10 registros na tabela
def insert_data():
    con = sqlite3.connect("products.db")
    cursor = con.cursor()
    data = [
        ("Eletrônicos", "Smartphone", 15),
        ("Eletrônicos", "Notebook", 8),
        ("Eletrônicos", "Fone de Ouvido", 25),
        ("Alimentos", "Arroz", 50),
        ("Alimentos", "Feijão", 40),
        ("Alimentos", "Macarrão", 30),
        ("Bebidas", "Refrigerante", 20),
        ("Bebidas", "Suco Natural", 10),
        ("Limpeza", "Detergente", 35),
        ("Limpeza", "Desinfetante", 18),
    ]

    cursor.executemany("INSERT INTO products (category, product, quantity) VALUES (?, ?, ?)", data)
    # Confirmar as alterações
    con.commit()
    con.close()
    print("10 registros inseridos com sucesso!")

def create_trigger():
    con = sqlite3.connect("products.db")
    cursor = con.cursor()
    cursor.execute("""CREATE TRIGGER IF NOT EXISTS trg_update_quantity
        AFTER UPDATE OF quantity ON products
        FOR EACH ROW
        WHEN OLD.quantity != NEW.quantity
        BEGIN
        INSERT INTO quantity_history (prod_hist, quantity_before, quantity_after, data_modify)
        VALUES (OLD.id_prod, OLD.quantity, NEW.quantity, CURRENT_TIMESTAMP);
        END;"""
    )
    con.commit()
    con.close()


con = sqlite3.connect("products.db")
cursor = con.cursor()
# printSelectAll = cursor.execute("SELECT * FROM products")

cursor.execute("UPDATE products SET quantity = ? WHERE id_prod = ?", (2, 3))
con.commit()

def join_tables():
    con = sqlite3.connect("products.db")
    cursor = con.cursor()
    cursor.execute(
        """SELECT p.category, p.product, h.quantity_before, h.quantity_after, h.data_modify
        FROM products as p
        INNER JOIN quantity_history as h
        ON p.id_prod = h.prod_hist
        ORDER BY h.data_modify DESC;"""
    )
    
    
    results = cursor.fetchall()
    print("\n=== Histórico de Alterações ===")
    for row in results:
        category, product, q_before, q_after, date = row
        print(f"Categoria: {category} | Produto: {product} | Antes: {q_before} | Depois: {q_after} | Data: {date}")

    
    con.close()
    
#print(printSelectAll.fetchall())

# create_trigger()
# create_tables()
# insert_data()
join_tables()

# con.close()