from fpdf import FPDF

# CREATE HEADER E FOOTER - globalmente
class FPDF(FPDF):
    
    def header(self):
        self.set_font(family="Arial", style="U", size=11)
        self.cell(0, 10, "This is a Header", align="C", border=1)
        self.set_xy(x=5, y=15) #Espaçamento abaixo do header
        
    def footer(self):
        self.set_y(-10)
        self.set_font(family="Arial", style="U", size=11)
        self.cell(200, 10, "This is a Footer", align="C", border="T")
        
        # Mostrar numero da pagina a partir de uma determinada pagina.
        pageNumber = self.page_no()
        if pageNumber > 1:
            self.cell(w=5,h=10, txt=str(pageNumber-1), align="R", border="T")

# Definindo estrutura da pagina e tipo de medidas;
pdf = FPDF("P", "mm", "A4")
        
w = 210
h = 297

pdf.set_font(family="Arial", style="B", size=16 )
pdf.set_margins(0, 0, 0)

pdf.add_page()
pdf.cell(w=0, h=7, txt="Sem page number")
pdf.add_page()
pdf.cell(w=0, h=7, txt="TESTANDO")
pdf.add_page()

pdf.output("HeaderAndFooter.pdf")