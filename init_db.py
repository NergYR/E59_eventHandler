import sqlite3

# Créer une base de données
conn = sqlite3.connect('produits.db')
cursor = conn.cursor()

# Créer une table produits
cursor.execute('''
CREATE TABLE IF NOT EXISTS produits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    code_barres TEXT NOT NULL
)
''')

# Insérer des exemples de produits
cursor.execute('''
INSERT INTO produits (nom, code_barres) VALUES
('Produit A', '123456789012'),
('Produit B', '987654321098')
''')

# Sauvegarder et fermer la connexion
conn.commit()
conn.close()
