import customtkinter as ctk
import tkinter.ttk as ttk
from models.database import recuperer_candidats,recherche


class ListeCandidatsFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        ctk.CTkLabel(self, text="Liste des Candidats", font=("Arial", 20)).pack(pady=10)

        # partie tableau  des données

        d_frame = ctk.CTkFrame(self)
        d_frame.pack(fill="both", padx=10, pady=10)

        # bouton filtre et recherche

        ctk.CTkLabel(d_frame, text="Recherche").pack()

        self.rech = ctk.StringVar()
        self.recherche_btn = ctk.CTkEntry(d_frame, textvariable=self.rech).pack(padx=10, pady=10)
       # self.recherche_btn.bind("<KeyRelease>",self.resultat_rech)

        self.table = ttk.Treeview(d_frame, columns=("id", "Nom", "Email", "Photo",), show='headings')
        self.table.heading("id", text="ID")
        self.table.heading("Nom", text="Nom")
        self.table.heading("Email", text="Email")
        self.table.heading("Photo", text="Photo")
        self.table.pack(fill="both", padx=10, pady=10)

        candidats = recuperer_candidats()
        for id, nom, email, niveau, motivation, photo in candidats:
            self.table.insert('', 'end', values=(id, nom, niveau, motivation, photo))


    def resultat_rech(self):
        for item in self.table.get_children():
            self.table.delete(item)
        for row in recherche(self.rech):
            self.table.insert("", "end", values=row)


