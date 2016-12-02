import sys
from DungeonAttackUI import *

#import generated UI file here


class MyForm(QtWidgets.QMainWindow):


        #DO NOT MODIFY THIS SECTION OF CODE
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #END DO NOT MODIFY

        # ADD SLOTS HERE


    # ADD SLOT FUNCTIONS HERE


    # ADD ALL OTHER HELPER FUNCTIONS HERE


#DO NOT MODIFY THIS SECTION OF CODE
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
#END DO NOT MODIFY
