from likeprocessing.processing import *

ihm = IhmScreen()


def dialogue_mot_cle():
    def enregister():
        print("enregister")

    def annuler():
        print("annuler")

    ihm.init()
    dia = Dialog(ihm, (10, 10, 200, 200), title="Nouveau mot clé")
    dia.addObjet(Label(dia, (10, 10, 100, 30), "nouveau mot clé :"), "0")
    dia.addObjet(LineEdit(dia, (10, 10, 100, 30), ""), 'mot_cle')
    dia.addObjet(Bouton(dia, (10, 10, 50, 30), "Enregistrer", command=enregister), "1")
    dia.addObjet(Bouton(dia, (10, 10, 50, 30), "Annuler", command=annuler), "2")
    dia.pack([["0", "mot_cle"], ["1", "2"]],padx=10)
    dia.ajuste(30)
    ihm.addObjet(dia)


def setup():
    createCanvas(400, 200)
    background("grey")
    dialogue_mot_cle()


def compute():
    ihm.scan_events()


def draw():
    ihm.draw()


run(globals())
