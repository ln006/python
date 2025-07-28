from os.path import expanduser
from tkinter import filedialog, messagebox

import customtkinter as ctk
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from controllers.gestion_formulaire import soumettre_candidat
from .liste_candidats import ListeCandidatsFrame


# Page d'acceuil de notre application
class AccueilFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.Frame = ctk.CTkFrame(self, fg_color="blue")
        self.Frame.pack(pady=10)
        label = ctk.CTkLabel(self.Frame, text="Bienvenue dans notre plateforme de gestion des bourses",
                             font=("Arial", 30, "bold"))
        label.pack(pady=90)
        label2 = ctk.CTkLabel(self, text="Faites votre choix pour un avenir plus sur !", font=("Arial", 24))
        label2.pack(pady=40)

        btn_formulaire = ctk.CTkButton(self, text="S'ENRENGISTRER", font=("Arial", 10, "bold"),
                                       command=lambda: master.switch_frame(Connection))
        btn_formulaire.pack(side="left", pady=20, padx=150)

        btn_formulaire = ctk.CTkButton(self, text="SE CONNECTER", font=("Arial", 10, "bold"),
                                       command=lambda: master.switch_frame(MainClient))
        btn_formulaire.pack(side="right", pady=20, padx=180)


#page de connection
class Connection(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.Main_frame = ctk.CTkFrame(self)
        self.Main_frame.pack(pady=(130, 10), padx=(200, 200))
        self.Text = ctk.CTkLabel(self.Main_frame, text="S'ENRENGISTRER", font=("Arial", 20, "bold"), bg_color="white")
        self.Text.pack(pady=(15, 5), padx=(50, 50))
        self.nom = ctk.CTkLabel(self.Main_frame, text="NOM")
        self.nom.pack(padx=(1, 190), pady=(1, 1))
        self.ent_nom = ctk.CTkEntry(self.Main_frame, placeholder_text="Entrer votre nom", width=300)
        self.ent_nom.pack(padx=(30, 30), pady=(3, 20))

        self.nom = ctk.CTkLabel(self.Main_frame, text="PRENOM")
        self.nom.pack(pady=(1, 1), padx=(1, 190))
        self.ent_nom = ctk.CTkEntry(self.Main_frame, placeholder_text="Votre prénom", width=300)
        self.ent_nom.pack(padx=(30, 30), pady=(3, 20))

        self.nom = ctk.CTkLabel(self.Main_frame, text="Mot de passe", )
        self.nom.pack(pady=(1, 1), padx=(1, 190))
        self.ent_nom = ctk.CTkEntry(self.Main_frame, placeholder_text="Votre mot de passe", width=300)
        self.ent_nom.pack(padx=(30, 30), pady=(3, 20))

        self.bouton_connect = ctk.CTkButton(self.Main_frame, text="Se connecter")
        self.bouton_connect.pack(pady=(30, 30), padx=(10, 10))

        self.btn_retour = ctk.CTkButton(self, text="retour", width=40,
                                        command=lambda: master.switch_frame(AccueilFrame))
        self.btn_retour.place(x=10, y=10)


# Class de la page du formulaire
class FormulaireFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.photo_path = ""

        self.label = ctk.CTkLabel(self, text="Formulaire de demande de bourse", font=("Arial", 20))
        self.label.pack(pady=20)

        self.btn_photo = ctk.CTkButton(self, text="Joindre une photo", command=self.choisir_photo)
        self.btn_photo.pack(pady=10)

        self.entry_nom = ctk.CTkEntry(self, placeholder_text="Nom complet", width=100)
        self.entry_nom.pack(pady=3)

        self.entry_email = ctk.CTkEntry(self, placeholder_text="Email", width=100)
        self.entry_email.pack(pady=10)
        self.label = ctk.CTkLabel(self, text="Date de naissance", font=("Arial", 15)).pack(pady=(1, 1), padx=(1, 10))

        date_entry = DateEntry(self, width=16, background='darkblue', foreground='white', borderwidth=2,
                               date_pattern='dd/mm/yyyy')
        date_entry.pack(pady=5)

        self.comboniveau = ctk.CTkOptionMenu(self, values=["Licence", "Master", "Doctorat", "BAC"])
        self.comboniveau.set("Licence")
        self.comboniveau.pack(pady=10)

        self.txt_motivation = ctk.CTkTextbox(self, height=100, width=400)
        self.txt_motivation.pack(pady=10)

        self.btn_submit = ctk.CTkButton(self, text="Soumettre", command=self.soumettre)
        self.btn_submit.pack(pady=20)

        self.btn_retour = ctk.CTkButton(self, text="retour", command=lambda: master.switch_frame(AccueilFrame))
        self.btn_retour.pack(pady=10)

    def choisir_photo(self):
        path = filedialog.askopenfilename(filetypes=[("Images", "*.png *.jpg *.jpeg")])
        if path:
            self.photo_path = path
            image = Image.open(path)
            self.photo = ctk.CTkImage(light_image=image, size=(150, 150))

            messagebox.showinfo("Photo ajoutée", "Photo ajoutée avec succès")
            label_photo = ctk.CTkLabel(self, image=self.photo, text="")
            label_photo.pack(pady=(10, 70), padx=(50, 10))

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
        self.left.pack(side="left", padx=(10, 40), pady=(25, 15), expand=True)
        self.master.geometry("900x600")
        # Zone de notifications
        notif_label = ctk.CTkLabel(self.left, text="NOTIFICATIONS", font=("Arial", 16, "bold"))
        notif_label.pack(anchor="w", pady=(10, 10), padx=(10, 30))

        self.notif_box = ctk.CTkFrame(self.left, fg_color="#E6E6E6", corner_radius=8)
        self.notif_box.pack(fill="x", pady=(20, 60), padx=(10, 130))
        notif_text = ctk.CTkLabel(self.notif_box, text="NOM DU CANDIDAT ", text_color="black")
        notif_text.pack(padx=1, pady=10)
        notif_text = ctk.CTkLabel(self.notif_box, text="PRENOM DU CANDIDAT", text_color="black")
        notif_text.pack(padx=1, pady=10)
        notif_text = ctk.CTkLabel(self.notif_box, text="EMAIL", text_color="black")
        notif_text.pack(padx=1, pady=10)

        # Liste de postulation
        self.postulation_box = ctk.CTkFrame(self.left, fg_color="#D9D9D9", corner_radius=8)
        self.postulation_box.pack(fill="x", pady=(10, 50), padx=(10, 40))

        self.post_title = ctk.CTkLabel(self.postulation_box, text="ETAT DE LA CANDIDATURE POUR LA BOURSE",
                                       text_color="black")
        self.post_title.pack(anchor="w", padx=(10, 5), pady=(10, 20))

        bourse_label = ctk.CTkLabel(self.postulation_box, text="BOURSE DE CHINE", text_color="black", bg_color="white")
        bourse_label.pack(anchor="w", padx=(10, 10))

        status_label = ctk.CTkLabel(self.postulation_box, text="En attente", text_color="gray")
        status_label.pack(anchor="e", padx=10)
        # === COLONNE DROITE ===

        canvas = ctk.CTkCanvas(self)
        self.scrollbar = ctk.CTkScrollbar(self, command=canvas.yview)
        self.scrollable_frame = ctk.CTkFrame(canvas, fg_color="gray")
        self.scrollable_frame.bind("<Configure>"
                                   , lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=self.scrollbar.set)
        canvas.pack(side="right", fill="both", expand=True)
        self.scrollable_frame.pack(side="right", fill="y")

        bourses = [
            "BOURSE DE CHINE",
            "BOURSE DE LA FINLANDE",
            "BOURSE DE USA",
            "BOURSE FRANCE"
        ]
        self.btn_retour = ctk.CTkButton(self, text="retour", width=40,
                                        command=lambda: master.switch_frame(AccueilFrame))
        self.btn_retour.place(x=10, y=10)

    def ajouter_labels(frame, nombre):
        for i in range(nombre):
            label = ctk.CTkLabel(frame, text=f"", text_color="black", pady=10)
            label.pack(fill="x", padx=10, pady=10)
