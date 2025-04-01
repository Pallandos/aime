from PyQt5 import QtCore, QtGui, QtWidgets

from py.gui.main_window import Ui_AIME
from py.gui.a_propos import Ui_A_Propos

import py.regex as regex
import py.pathologies as pathologies

class AIME(QtWidgets.QMainWindow, Ui_AIME):

    def __init__(self):
        super(AIME, self).__init__()
        self.setupUi(self)
        self.pushButton_options.clicked.connect(self.options_clicked)
        self.pushButton_valider.clicked.connect(self.valider_clicked)
        self.actionA_propos.triggered.connect(self.a_propos_clicked)

    
    def options_clicked(self):
        """Quand le boutton options est cliqué
        """

        self.stackedWidget.setCurrentIndex(1)

    def valider_clicked(self):
        """Quand le boutton valider est cliqué 
        """

        # page de chargement :
        self.stackedWidget.setCurrentIndex(1)

        text_saisi = self.plainTextEdit.toPlainText()

        # appel de la fonction d'extraction : 
        texte_interesse = regex.extract_text(text_saisi)

        maladies = []

        # appel de la fonction d'extraction :
        for texte in texte_interesse:
            maladies += pathologies.extract_pathologies(texte)

        # affichage des maladies
        print(maladies)


    def a_propos_clicked(self):
        """Affiche la fenêtre à propos
        """

        dialog = QtWidgets.QDialog()
        ui = Ui_A_Propos()
        ui.setupUi(dialog)
        dialog.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AIME = AIME()
    AIME.show()
    sys.exit(app.exec_())