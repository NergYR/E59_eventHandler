from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from plyer import camera
from pyzbar.pyzbar import decode
from PIL import Image

import sqlite3  # Pour interagir avec la base de données SQLite

class BarcodeScannerApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.label = Label(text="Scanner un code-barres")
        self.layout.add_widget(self.label)

        self.button = Button(text="Lancer le scan")
        self.button.bind(on_press=self.scan_barcode)
        self.layout.add_widget(self.button)

        return self.layout

    def scan_barcode(self, instance):
        # Utilisation de la caméra via Plyer pour prendre une photo
        camera.take_picture(filename="barcode.png", on_complete=self.process_image)

    def process_image(self, filepath):
        # Traite l'image pour décoder le code-barres
        try:
            image = Image.open(filepath)
            barcodes = decode(image)
            if barcodes:
                for barcode in barcodes:
                    barcode_data = barcode.data.decode("utf-8")
                    self.label.text = f"Code-barres trouvé : {barcode_data}"
                    self.check_barcode_in_db(barcode_data)
            else:
                self.label.text = "Aucun code-barres trouvé."
        except Exception as e:
            self.label.text = f"Erreur : {str(e)}"

    def check_barcode_in_db(self, barcode_data):
        # Connexion à la base de données SQLite et vérification du code-barres
        try:
            conn = sqlite3.connect('produits.db')  # Connecte à la base de données
            cursor = conn.cursor()

            query = "SELECT * FROM produits WHERE code_barres = ?"
            cursor.execute(query, (barcode_data,))
            result = cursor.fetchone()

            if result:
                self.label.text = f"Produit trouvé : {result[1]}"  # Supposons que la deuxième colonne soit le nom du produit
            else:
                self.label.text = "Produit non trouvé."
            
            conn.close()
        except sqlite3.Error as e:
            self.label.text = f"Erreur base de données : {str(e)}"

if __name__ == '__main__':
    BarcodeScannerApp().run()
