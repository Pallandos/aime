from PyQt5 import QtCore, QtGui, QtWidgets
from sympy import sec

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

        url = QUrl("https://github.com/Pallandos/aime/wiki")
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
        self.model_table.setHorizontalHeaderLabels(["Code", "Priorité", "Référence à :", "Description"])

        self.add_data()
        self.tableView.setModel(self.model_table)
    
    def add_data(self):
        for item in self.codes_finaux:

            # premier résultat
            item = item[0]
            code = item["best_match_code"]
            description = item["best_match_description"]
            priorite = "haute"
            ref = item["entity"]
            
            # second résultat
            code2 = item["second_best_match_code"]
            description2 = item["second_best_match_description"]
            priorite2 = "moyenne"

            # 3e résultat
            code3 = item["third_best_match_code"]
            description3 = item["third_best_match_description"]
            priorite3 = "moyenne"

            
            # convert to model item
            code_item = QtGui.QStandardItem(code)
            description_item = QtGui.QStandardItem(description)
            priorite_item = QtGui.QStandardItem(priorite)
            ref_item = QtGui.QStandardItem(ref)

            code_item2 = QtGui.QStandardItem(code2)
            description_item2 = QtGui.QStandardItem(description2)
            priorite_item2 = QtGui.QStandardItem(priorite2)

            code_item3 = QtGui.QStandardItem(code3)
            description_item3 = QtGui.QStandardItem(description3)
            priorite_item3 = QtGui.QStandardItem(priorite3)
            

            # add to model
            self.model_table.appendRow([code_item, priorite_item, ref_item, description_item])
            self.model_table.appendRow([code_item2, priorite_item2, ref_item, description_item2])
            self.model_table.appendRow([code_item3,priorite_item3, ref_item, description_item3])

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