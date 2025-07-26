# main.py
import customtkinter as ctk
from views.accueil import AccueilFrame, MainClient, Connection,FormulaireFrame
from models.database import init_db

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gestion de Bourse d'étude")
        self.geometry("900x600")
        init_db()
        self.current_frame = None
        self.switch_frame(MainClient)

    def switch_frame(self, frame_class):
        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = frame_class(self)
        self.current_frame.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()