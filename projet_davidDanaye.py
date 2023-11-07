import tkinter as tk
from tkinter import messagebox

class Produit:
    def __init__(self, nom, prix, quantite, categorie=None):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite
        self.categorie = categorie

class GestionStock:
    def __init__(self):
        self.stock = []
        self.historique = []

    def ajouter_produit(self, produit):
        self.stock.append(produit)
        self.historique.append(f"Ajout du produit '{produit.nom}'")
        self.sauvegarder_stock()
        self.afficher_message("Produit ajouté au stock.")
  
    def afficher_stock(self):
        if not self.stock:
            self.afficher_message("Le stock est vide.")
        else:
            stock_str = "Stock :\n"
            for produit in self.stock:
                stock_str += f"Nom: {produit.nom}, Prix: {produit.prix}, Quantité: {produit.quantite}\n"
            self.afficher_message(stock_str)


       

    def rechercher_produit(self):
        fenetre_recherche = tk.Toplevel(fenetre)
        fenetre_recherche.title("Recherche d'un produit")

        label_nom = tk.Label(fenetre_recherche, text="Nom du produit:")
        label_nom.pack()
        entry_nom = tk.Entry(fenetre_recherche)
        entry_nom.pack()

        def rechercher():
            nom = entry_nom.get()
            produits_trouves = [produit for produit in self.stock if produit.nom == nom]
            if produits_trouves:
                resultat_text = "Résultat de la recherche:\n"
                for produit in produits_trouves:
                    resultat_text += f"Nom: {produit.nom} - Prix: {produit.prix} - Quantité: {produit.quantite} - Catégorie: {produit.categorie}\n"
                messagebox.showinfo("Résultat de la recherche", resultat_text)
            else:
                messagebox.showinfo("Résultat de la recherche", "Aucun produit trouvé.")

        button_rechercher = tk.Button(fenetre_recherche, text="Rechercher", command=rechercher)
        button_rechercher.pack()

    def mettre_a_jour_quantite(self):
        fenetre_maj = tk.Toplevel(fenetre)
        fenetre_maj.title("Mettre à jour la quantité")

        label_nom = tk.Label(fenetre_maj, text="Nom du produit:")
        label_nom.pack()
        entry_nom = tk.Entry(fenetre_maj)
        entry_nom.pack()

        label_quantite = tk.Label(fenetre_maj, text="Nouvelle quantité:")
        label_quantite.pack()
        entry_quantite = tk.Entry(fenetre_maj)
        entry_quantite.pack()

        def mettre_a_jour():
            nom = entry_nom.get()
            quantite = int(entry_quantite.get())
            produit_trouve = next((produit for produit in self.stock if produit.nom == nom), None)
            if produit_trouve:
                ancienne_quantite = produit_trouve.quantite
                produit_trouve.quantite = quantite
                self.historique.append(f"Mise à jour de la quantité du produit '{produit_trouve.nom}': {ancienne_quantite} -> {quantite}")
                messagebox.showinfo("Mise à jour de la quantité", "Quantité mise à jour avec succès.")
            else:
                messagebox.showinfo("Mise à jour de la quantité", "Produit non trouvé.")

        button_mettre_a_jour = tk.Button(fenetre_maj, text="Mettre à jour", command=mettre_a_jour)
        button_mettre_a_jour.pack()

    def supprimer_produit(self):
        fenetre_suppression = tk.Toplevel(fenetre)
        fenetre_suppression.title("Supprimer un produit")

        label_nom = tk.Label(fenetre_suppression, text="Nom du produit:")
        label_nom.pack()
        entry_nom = tk.Entry(fenetre_suppression)
        entry_nom.pack()

        def supprimer():
            nom = entry_nom.get()
            produit_trouve = next((produit for produit in self.stock if produit.nom == nom), None)
            if produit_trouve:
                self.stock.remove(produit_trouve)
                self.historique.append(f"Suppression du produit '{produit_trouve.nom}'")
                messagebox.showinfo("Suppression du produit", "Produit supprimé avec succès.")
            else:
                messagebox.showinfo("Suppression du produit", "Produit non trouvé.")

        button_supprimer = tk.Button(fenetre_suppression, text="Supprimer", command=supprimer)
        button_supprimer.pack()

    def calculer_prix_total(self):
        fenetre_calcul = tk.Toplevel(fenetre)
        fenetre_calcul.title("Calculer le prix total")

        text_calcul = tk.Text(fenetre_calcul)
        text_calcul.pack()

        total_text = "Prix total par produit:\n"
        for produit in self.stock:
            prix_total = produit.prix * produit.quantite
            total_text += f"Nom: {produit.nom} - Prix total: {prix_total}\n"
        text_calcul.insert(tk.END, total_text)

    def trier_stock(self, critere, ordre):
        if critere == "nom":
            self.stock.sort(key=lambda produit: produit.nom, reverse=(ordre == "décroissant"))
        elif critere == "prix":
            self.stock.sort(key=lambda produit: produit.prix, reverse=(ordre == "décroissant"))
        elif critere == "quantite":
            self.stock.sort(key=lambda produit: produit.quantite, reverse=(ordre == "décroissant"))

        messagebox.showinfo("Tri du stock", "Stock trié avec succès.")

    def afficher_statistiques(self):
        fenetre_stats = tk.Toplevel(fenetre)
        fenetre_stats.title("Statistiques du stock")

        text_stats = tk.Text(fenetre_stats)
        text_stats.pack()

        nombre_total_produits = len(self.stock)
        valeur_totale_stock = sum(produit.prix * produit.quantite for produit in self.stock)
        quantite_minimale = min(produit.quantite for produit in self.stock)
        quantite_maximale = max(produit.quantite for produit in self.stock)

        stats_text = f"Statistiques du stock:\nNombre total de produits: {nombre_total_produits}\nValeur totale du stock: {valeur_totale_stock}\nQuantité minimale: {quantite_minimale}\nQuantité maximale: {quantite_maximale}"
        text_stats.insert(tk.END, stats_text)

    def gestion_categories(self):
        fenetre_categories = tk.Toplevel(fenetre)
        fenetre_categories.title("Gestion des catégories de produits")

        label_nom = tk.Label(fenetre_categories, text="Nom du produit:")
        label_nom.pack()
        entry_nom = tk.Entry(fenetre_categories)
        entry_nom.pack()

        label_categorie = tk.Label(fenetre_categories, text="Catégorie:")
        label_categorie.pack()
        entry_categorie = tk.Entry(fenetre_categories)
        entry_categorie.pack()

        def assigner_categorie():
            nom = entry_nom.get()
            categorie = entry_categorie.get()
            produit_trouve = next((produit for produit in self.stock if produit.nom == nom), None)
            if produit_trouve:
                produit_trouve.categorie = categorie
                messagebox.showinfo("Gestion des catégories", "Catégorie assignée avec succès.")
            else:
                messagebox.showinfo("Gestion des catégories", "Produit non trouvé.")

        button_assigner_categorie = tk.Button(fenetre_categories, text="Assigner Catégorie", command=assigner_categorie)
        button_assigner_categorie.pack()

    def rechercher_par_categorie(self):
        fenetre_filtre = tk.Toplevel(fenetre)
        fenetre_filtre.title("Rechercher par catégorie")

        label_categorie = tk.Label(fenetre_filtre, text="Catégorie:")
        label_categorie.pack()
        entry_categorie = tk.Entry(fenetre_filtre)
        entry_categorie.pack()

        def filtrer_par_categorie():
            categorie = entry_categorie.get()
            produits_filtres = [produit for produit in self.stock if produit.categorie == categorie]
            if produits_filtres:
                resultat_text = f"Produits de la catégorie '{categorie}':\n"
                for produit in produits_filtres:
                    resultat_text += f"Nom: {produit.nom} - Prix: {produit.prix} - Quantité: {produit.quantite}\n"
                messagebox.showinfo("Produits de la catégorie", resultat_text)
            else:
                messagebox.showinfo("Produits de la catégorie", "Aucun produit trouvé.")

        button_filtrer_par_categorie = tk.Button(fenetre_filtre, text="Filtrer", command=filtrer_par_categorie)
        button_filtrer_par_categorie.pack()

    def alertes_stock_bas(self, seuil):
        produits_stock_bas = [produit for produit in self.stock if produit.quantite < seuil]
        if produits_stock_bas:
            alerte_text = "Alerte de stock bas:\n"
            for produit in produits_stock_bas:
                alerte_text += f"Produit '{produit.nom}' - Quantité: {produit.quantite}\n"
            messagebox.showinfo("Alerte de stock bas", alerte_text)
        else:
            messagebox.showinfo("Alerte de stock bas", "Aucun produit en stock bas.")

    def afficher_historique(self):
        fenetre_historique = tk.Toplevel(fenetre)
        fenetre_historique.title("Historique des modifications")

        text_historique = tk.Text(fenetre_historique)
        text_historique.pack()

        historique_text = "Historique des modifications:\n"
        for modification in self.historique:
            historique_text += f"{modification}\n"
        text_historique.insert(tk.END, historique_text)

    def quitter(self):
        fenetre.quit()

    # Jai ajouter une fonction pour enregistrer le stock dans un fichier text
    def sauvegarder_stock(self):
        try:
            with open("stock.txt", "a") as fichier:
                for produit in self.stock:
                    ligne = f"{produit.nom},{produit.prix},{produit.quantite}\n"
                    fichier.write(ligne)
        except OSError as e:
            self.afficher_message("Erreur lors de la sauvegarde du stock : " + str(e))
        else:
            self.afficher_message("Stock sauvegardé dans le fichier.")




    def afficher_message(self, message):
        messagebox.showinfo("Gestion du stock", message)

gestion_stock = GestionStock()

fenetre = tk.Tk()
fenetre.title("Gestion de stock")

# Ajouter un produit au stock
label_nom = tk.Label(fenetre, text="Nom du produit:")
label_nom.pack()
entry_nom = tk.Entry(fenetre)
entry_nom.pack()

label_prix = tk.Label(fenetre, text="Prix:")
label_prix.pack()
entry_prix = tk.Entry(fenetre)
entry_prix.pack()

label_quantite = tk.Label(fenetre, text="Quantité:")
label_quantite.pack()
entry_quantite = tk.Entry(fenetre)
entry_quantite.pack()

button_ajouter = tk.Button(fenetre, text="Ajouter au stock", bg="blue", fg="white", command=lambda: gestion_stock.ajouter_produit(Produit(entry_nom.get(), float(entry_prix.get()), int(entry_quantite.get()))))
button_ajouter.pack()

# Afficher le stock
button_afficher_stock = tk.Button(fenetre, text="Afficher le stock", bg="blue", fg="white", command=gestion_stock.afficher_stock)
button_afficher_stock.pack()


# Bouton pour sauvegarder le stock
button_sauvegarder_stock = tk.Button(fenetre, text="Sauvegarder le stock", bg="blue", fg="white", command=gestion_stock.sauvegarder_stock)
button_sauvegarder_stock.pack()

# Rechercher un produit
button_rechercher_produit = tk.Button(fenetre, text="Rechercher un produit", bg="blue", fg="white", command=gestion_stock.rechercher_produit)
button_rechercher_produit.pack()

# Mettre à jour la quantité d'un produit
button_maj_quantite = tk.Button(fenetre, text="Mettre à jour la quantité d'un produit", bg="blue", fg="white", command=gestion_stock.mettre_a_jour_quantite)
button_maj_quantite.pack()

# Supprimer un produit
button_supprimer_produit = tk.Button(fenetre, text="Supprimer un produit", bg="blue", fg="white", command=gestion_stock.supprimer_produit)
button_supprimer_produit.pack()

# Gestion des prix totaux
button_calculer_prix_total = tk.Button(fenetre, text="Calculer les prix totaux", bg="blue", fg="white", command=gestion_stock.calculer_prix_total)
button_calculer_prix_total.pack()

# Tri du stock
label_tri = tk.Label(fenetre, text="Trier le stock par:")
label_tri.pack()
variable_tri = tk.StringVar(fenetre)
variable_tri.set("nom")
menu_tri = tk.OptionMenu(fenetre, variable_tri, "nom", "prix", "quantite")
menu_tri.pack()

label_ordre = tk.Label(fenetre, text="Ordre:")
label_ordre.pack()
variable_ordre = tk.StringVar(fenetre)
variable_ordre.set("croissant")
menu_ordre = tk.OptionMenu(fenetre, variable_ordre, "croissant", "décroissant")
menu_ordre.pack()

button_trier_stock = tk.Button(fenetre, text="Trier le stock", bg="blue", fg="white", command=lambda: gestion_stock.trier_stock(variable_tri.get(), variable_ordre.get()))
button_trier_stock.pack()

# Statistiques du stock
button_stats_stock = tk.Button(fenetre, text="Statistiques du stock", bg="blue", fg="white", command=gestion_stock.afficher_statistiques)
button_stats_stock.pack()

# Gestion des catégories de produits
button_gestion_categories = tk.Button(fenetre, text="Gestion des catégories de produits", bg="blue", fg="white", command=gestion_stock.gestion_categories)
button_gestion_categories.pack()

# Rechercher, filtrer ou afficher les produits par catégorie
button_rechercher_categorie = tk.Button(fenetre, text="Rechercher par catégorie", bg="blue", fg="white", command=gestion_stock.rechercher_par_categorie)
button_rechercher_categorie.pack()

# Alerte de stock bas
label_seuil = tk.Label(fenetre, text="Seuil de stock bas:")
label_seuil.pack()
entry_seuil = tk.Entry(fenetre)
entry_seuil.pack()

button_alerte_stock_bas = tk.Button(fenetre, text="Alerte de stock bas", bg="blue", fg="white", command=lambda: gestion_stock.alertes_stock_bas(int(entry_seuil.get())))
button_alerte_stock_bas.pack()

# Afficher l'historique des modifications
button_afficher_historique = tk.Button(fenetre, text="Afficher l'historique des modifications", bg="blue", fg="white", command=gestion_stock.afficher_historique)
button_afficher_historique.pack()

# Quitter l'application
button_quitter = tk.Button(fenetre, text="Quitter", bg="gray", fg="white", command=gestion_stock.quitter)
button_quitter.pack()

fenetre.mainloop()
