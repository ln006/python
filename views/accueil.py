from tkinter import filedialog, messagebox

import customtkinter as ctk
import self

from controllers.gestion_formulaire import soumettre_candidat
from .liste_candidats import ListeCandidatsFrame


# Page d'acceuil de notre application
class AccueilFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        label = ctk.CTkLabel(self, text="Bienvenue dans le Gestionnaire de Bourse", font=("Arial", 24))
        label.pack(pady=140)

        btn_formulaire = ctk.CTkButton(self, text="Se connecter",
                                       command=lambda: master.switch_frame(Connection))
        btn_formulaire.pack(pady=20)

        btn_formulaire = ctk.CTkButton(self, text="Formulaire",
                                       command=lambda: master.switch_frame(ListeCandidatsFrame))
        btn_formulaire.pack(pady=20)


#page de connection
class Connection(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.Main_frame= ctk.CTkFrame(self)
        self.Main_frame.pack(pady=100,padx=100)
        self.nom = ctk.CTkLabel(self.Main_frame, text="Nom")
        self.nom.pack(padx=0,)
        self.ent_nom = ctk.CTkEntry(self.Main_frame, placeholder_text="Entrer votre nom", width=300)
        self.ent_nom.pack(padx=10)

        self.nom = ctk.CTkLabel(self.Main_frame, text="Mot de passe")
        self.nom.pack(pady=0)
        self.ent_nom = ctk.CTkEntry(self.Main_frame, placeholder_text="Votre mot de passe", width=300)
        self.ent_nom.pack(padx=10)

        self.bouton_connect = ctk.CTkButton(self.Main_frame, text="Se connecter")
        self.bouton_connect.pack(pady=20)

        self.btn_retour = ctk.CTkButton(self, text="retour",width=40, command=lambda: master.switch_frame(AccueilFrame))
        self.btn_retour.place(x=10, y=10)


# Class de la page du formulaire
class FormulaireFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.photo_path = ""

        self.label = ctk.CTkLabel(self, text="Formulaire de demande de bourse", font=("Arial", 20))
        self.label.pack(pady=20)

        self.entry_nom = ctk.CTkEntry(self, placeholder_text="Nom complet")
        self.entry_nom.pack(pady=3)

        self.entry_email = ctk.CTkEntry(self, placeholder_text="Email")
        self.entry_email.pack(pady=10)

        self.comboniveau = ctk.CTkOptionMenu(self, values=["Licence", "Master", "Doctorat"])
        self.comboniveau.set("Licence")
        self.comboniveau.pack(pady=10)

        self.txt_motivation = ctk.CTkTextbox(self, height=100, width=400)
        self.txt_motivation.pack(pady=10)

        self.btn_photo = ctk.CTkButton(self, text="Joindre une photo", command=self.choisir_photo)
        self.btn_photo.pack(pady=10)

        self.btn_submit = ctk.CTkButton(self, text="Soumettre", command=self.soumettre)
        self.btn_submit.pack(pady=20)

        self.btn_retour = ctk.CTkButton(self, text="retour", command=lambda: master.switch_frame(AccueilFrame))
        self.btn_retour.pack(pady=10)

    def choisir_photo(self):
        path = filedialog.askopenfilename(filetypes=[("Images", "*.png *.jpg *.jpeg")])
        if path:
            self.photo_path = path
            messagebox.showinfo("Photo ajoutée", "Photo ajoutée avec succès")

    def soumettre(self):
        nom = self.entry_nom.get()
        email = self.entry_email.get()
        niveau = self.comboniveau.get()
        motivation = self.txt_motivation.get("1.0", "end").strip()

        if not nom or not email or not motivation:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs")
            return

        soumettre_candidat(nom, email, niveau, motivation, self.photo_path)
        messagebox.showinfo("Succès", "Candidature soumise avec succès")

class MainClient(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

       # === COLONNE GAUCHE ===
        self.left = ctk.CTkFrame(self, fg_color="gray")
        self.left.grid(row=0, column=0, sticky="nsew", padx=100, pady=100)
        self.left.grid_rowconfigure(2, weight=1)

       # Zone de notifications
        notif_label = ctk.CTkLabel(self.left, text="NOTIFICATIONS", font=("Arial", 16, "bold"))
        notif_label.pack(anchor="w", pady=(0, 10))

        self.notif_box = ctk.CTkFrame(self.left, fg_color="#E6E6E6", corner_radius=8)
        self.notif_box.pack(fill="x", pady=(0, 20))
        notif_text = ctk.CTkLabel(self.notif_box, text="informations personnelles du formulaire", text_color="black")
        notif_text.pack(padx=10, pady=10)

        # Liste de postulation
        self.postulation_box = ctk.CTkFrame(self.left, fg_color="#D9D9D9", corner_radius=8)
        self.postulation_box.pack(fill="x", pady=(10, 0))

        self.post_title = ctk.CTkLabel(self.postulation_box, text="ETAT DE LA CANDIDATURE POUR LA BOURSE", text_color="black")
        self.post_title.pack(anchor="w", padx=10, pady=(10, 2))

        bourse_label = ctk.CTkLabel(self.postulation_box, text="BOURSE DE CHINE", text_color="black")
        bourse_label.pack(anchor="w", padx=10)

        status_label = ctk.CTkLabel(self.postulation_box, text="en attente", text_color="gray")
        status_label.pack(anchor="e", padx=10, pady=(0, 10))

         # === COLONNE DROITE ===
        self.right = ctk.CTkFrame(self, fg_color="gray")
        self.right.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)


        bourses = [
        "BOURSE DE CHINE",
        "BOURSE DE LA FINLANDE",
        "BOURSE DE USA",
        "BOURSE FRANCE"
        ]

        for b in bourses:
          row = ctk.CTkFrame(self.right, fg_color="#D9D9D9", corner_radius=8)
          row.pack(fill="x", pady=10)

          lbl = ctk.CTkLabel(row, text=b, text_color="black")
          lbl.pack(side="left", padx=10, pady=10)

          btn = ctk.CTkButton(row, text="POSTULER", width=100, fg_color="black", text_color="white")
          btn.pack(side="right", padx=10, pady=10)
