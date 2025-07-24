from models.database import ajouter_candidat

def soumettre_candidat(nom, email, niveau, motivation, photo_path):
    ajouter_candidat(nom, email, niveau, motivation, photo_path)