from fpdf import FPDF
from Controlador import *
objControl2 = Controlador() 

class GeneradorPDF(FPDF):
     
    def header(self):
        self.set_font('Arial', 'BU', 14)
        self.cell(0, 10, 'Reporte de usuarios', 0, 1, 'C')
        
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Página ' + str(self.page_no()), 0, 0, 'C')
        
    def chapter_body(self):
        self.set_font('Arial', 'I', 10)
        self.set_fill_color(200, 220, 255)
        lista = objControl2.obtenerUsuarios()
        self.multi_cell(100,10,'ID: ' + 'Usuario: ' + 'Correo:',1,'C',1)
        for i in lista:
            self.multi_cell(100,10,str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[2]),1,'C',1)
        
    