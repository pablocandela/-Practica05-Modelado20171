import sys
import datetime
from PyQt4 import QtGui, QtCore

class Ventana(QtGui.QWidget):
   
    def __init__(self):
        super(Ventana, self).__init__()
        self.initUI()
   
    def initUI(self):
        self.setGeometry(150, 150, 300, 250)
        self.setWindowTitle('¡Viva México!')
       
        self.resultado_lbl = QtGui.QLabel('Ignacio Allende', self)
        self.resultado_lb2 = QtGui.QLabel('Josefa Ortiz De Dominguez', self)
        self.resultado_lb3 = QtGui.QLabel('Juan Aldama', self)   
        self.resultado_lbl.move(0,30)
        self.resultado_lb2.move(0,40)
        self.resultado_lb3.move(0,50)
        
        self.boton = QtGui.QPushButton('Aprietame', self)
        self.boton.clicked.connect(self.modificar_Boton)
        self.boton.resize(self.boton.sizeHint())
        self.boton.move(20, 200)     
        self.show()
     
    def modificar_Boton(self):
       self.boton.setText(
           str(self.dias_faltantes())
       )
       self.boton.resize(self.boton.sizeHint())
        
    def dias_faltantes(self):
      hoy = datetime.date.today()
      septiembre_15 = datetime.date(hoy.year, 9, 15)
      if hoy <= septiembre_15:
          total = (septiembre_15 - hoy).days
      else:
          total = (datetime.date(hoy.year+1, 9, 15) - hoy).days
      return "faltan "+ str(total) + " dias para el 15 de septiembre"

def main():
    app = QtGui.QApplication(sys.argv)
    vent = Ventana()
    vent.setWindowIcon(QtGui.QIcon("bandera"))
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()
