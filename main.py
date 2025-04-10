from PyQt5 import QtCore, QtGui, QtWidgets

from py.gui.main_window import Ui_AIME
from py.gui.a_propos import Ui_A_propos
from PyQt5.QtCore import QUrl

import py.regex as regex
import py.pathologies as pathologies
import py.matcher as matcher

class AIME(QtWidgets.QMainWindow, Ui_AIME):

    def __init__(self):
        super(AIME, self).__init__()
        self.setupUi(self)
        self.pushButton_options.clicked.connect(self.options_clicked)
        self.pushButton_valider.clicked.connect(self.valider_clicked)
        self.actionA_propos.triggered.connect(self.a_propos_clicked)
        self.pushButton_retour.clicked.connect(self.retour_clicked)
        self.actionAide.triggered.connect(self.aide_clicked)

    def aide_clicked(self):
        """Quand le boutton aide est cliqué

            Ouvre le dépot github
        """

        url = QUrl("https://github.com/Pallandos/aime/issues")
        QtGui.QDesktopServices.openUrl(url)

        pass

    def retour_clicked(self):
        """Quand le boutton retour est cliqué
        """

        # page d'accueil :
        self.stackedWidget.setCurrentIndex(0)

        # on vide le tableau
        self.model_table = QtGui.QStandardItemModel()
        self.tableView.setModel(self.model_table)

        # on vide le champ de texte
        self.plainTextEdit.clear()
    
    def options_clicked(self):
        """Quand le boutton options est cliqué
        """

        #! non supporté dans la version 1.1.0

        pass

    def valider_clicked(self):
        """Quand le boutton valider est cliqué 
        """

        # page de chargement :
        self.stackedWidget.setCurrentIndex(2)

        text_saisi = self.plainTextEdit.toPlainText()

        # appel de la fonction d'extraction : 
        texte_interesse = regex.extract_text(text_saisi)

        maladies = []

        # appel de la fonction d'extraction :
        for texte in texte_interesse:
            maladies += pathologies.extract_pathologies(texte)
        
        self.codes_finaux = []
        
        # on match avec les CIM10
        for mal in maladies:
            codes = matcher.match_cim10([mal])
            self.codes_finaux.append(codes)
        
        # affichage des résultats dans le tableau 
        self.model_table = QtGui.QStandardItemModel()
        self.model_table.setColumnCount(4)
        self.model_table.setHorizontalHeaderLabels(["Code", "Description", "Priorité", "Référence à :"])

        self.add_data()
        self.tableView.setModel(self.model_table)
    
    def add_data(self):
        for item in self.codes_finaux:
            item = item[0]
            code = item["best_match_code"]
            description = item["best_match_description"]
            priorite = "haute"
            ref = item["entity"]
            
            # convert to model item
            code_item = QtGui.QStandardItem(code)
            description_item = QtGui.QStandardItem(description)
            priorite_item = QtGui.QStandardItem(priorite)
            ref_item = QtGui.QStandardItem(ref)

            # add to model
            self.model_table.appendRow([code_item, description_item, priorite_item, ref_item])

    def a_propos_clicked(self):
        """Affiche la fenêtre à propos
        """

        dialog = QtWidgets.QDialog()
        ui = Ui_A_propos()
        ui.setupUi(dialog)
        dialog.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AIME = AIME()
    AIME.show()
    sys.exit(app.exec_())