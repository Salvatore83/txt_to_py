import os

class Programme():

    def __init__(self):
        try:
            self.fichier_python = open("fichiers/fichier_python.py", "w")
        except:
            quit()
        self.content = ""
        self.avant = ""
        self.ligne = ""
        self.fin_ligne = ""
        self.dictionnaire_fonction = {"AFFICHER":"print( "}
        self.dictionnaire_conditions = {"SINON_SI":"elif ", "SI":"if "}
        self.dictionnaire_boucle = {"DEBUT_TANT_QUE":"for", "DEBUT_POUR":"while"}
        self.dictionnaire_symboles = {'+':"+ ", "-":"- ", "/":"/ ", ",":", ", "<":"<", ">":"> ", "=":"== ", "!=":"!= ", "<=":"<= ", ">=":">= "}
    def _ouvrir_fichier(self):
        try:
            self.fichier_txt = open("fichiers/fichier_txt.txt", "r")
        except:
            quit()
    

    def _savoir_si_MAJ(self, chaine):
        return chaine == chaine.upper()

    def _creer_liste(self, chaine):
        self.liste = chaine.split(" ")

    def _ecrire_fichier_py(self, chaine):
        self.fichier_python.write(chaine + "\n")

    def _ecrire_debut_fichier_python(self):
        self._ecrire_fichier_py("# Ce fichier python a ete ecrit pas un convertisseur .txt to .py_" + "\n")
        self._ecrire_fichier_py("def main():")
        self.avant = "  "

    def _ecrire_fin_fichier_python(self):
        self._ecrire_fichier_py("\n" + "if __name__ == '__main__':")
        self._ecrire_fichier_py("   main()")


    def _fonction_definir(self, mot):
        if mot in self.dictionnaire_fonction:
            self.fin_ligne = ")"
            self.ligne = self.ligne + self.dictionnaire_fonction[mot]
        elif mot in self.dictionnaire_boucle:
            pass
        else:
            pass

    def _definir_ligne(self, mot):
        print(mot)
        try:
            mot = int(mot)
        except:
            pass
        if mot == "<-":
            self.ligne = self.ligne + "= "
        elif mot in self.dictionnaire_symboles:
            self.ligne = self.ligne + self.dictionnaire_symboles[mot]
        elif type(mot) == int:
            self.ligne = self.ligne + str(mot) + " "
        elif "FIN" in mot:
            nombre = len(self.avant)
            self.avant = self.avant[:(nombre - 4)]
        elif mot in self.dictionnaire_conditions:
            self.fin_ligne = ":"
            self.ligne = self.ligne + self.dictionnaire_conditions[mot]
            self.avant = self.avant + "    "
        else:
            if self._savoir_si_MAJ(mot) == True:
                self._fonction_definir(mot)
            else:
                mot = mot.replace("\n", "")
                self.ligne = self.ligne + mot + " "

    def _traitement(self):
        self._ecrire_debut_fichier_python()
        self.debut = self.avant
        if os.stat("fichiers/fichier_txt.txt").st_size != 0:
            for ligne in self.fichier_txt:
                self.content = ligne
                # print(ligne)
                self._creer_liste(self.content)
                for mot in self.liste:
                    self._definir_ligne(mot)
                self._ecrire_fichier_py(self.debut + self.ligne + self.fin_ligne)
                self.ligne = ""
                self.fin_ligne = ""
                self.debut = self.avant
        else:
            self._ecrire_fichier_py(self.avant + "pass")
        self._ecrire_fin_fichier_python()

    def _fermer_fichiers(self):
        self.fichier_python.close()
        self.fichier_txt.close()

    def _main(self):
        self._ouvrir_fichier()
        self._traitement()
        self._fermer_fichiers()