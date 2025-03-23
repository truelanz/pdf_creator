from fpdf import FPDF

pdf = FPDF("P", "mm", "A4")

w = 210
h = 297

pdf.set_font(family="Arial", style="B", size=16 )
pdf.set_margins(0, 0, 0)


#Page 1
pdf.add_page()
pdf.cell(w=22, h=8, txt="Page 1", border=1, ln=1) # 1 true 0 false

#Setar cor do texto daqui para baixo
pdf.set_text_color(255, 0, 0)

#Setar cor das borders
pdf.set_draw_color(0,0,255)

#Alinhar texto de cells
pdf.cell(w=0, h=8, txt="Something on center", align="C", border=1, ln=1)

#Adicionar link
pdf.set_font(family="Arial", style="I", size=13 )
pdf.cell(w=0, h=8, txt="My github", align="R", border=0, link="www.github.com/truelanz", ln=1)

# Ler .txt
pdf.set_xy(x=25, y=25)
openTxt = open(file="text.txt", mode="r")
line = openTxt.readlines()
textTxt = ("").join(line)
pdf.multi_cell(w=160, h=7, txt=textTxt, border=1)

#Cell no centro, na vertical da folha
pdf.set_xy(0, h/2)
pdf.cell(w=22, h=8, txt="center cell", border=1)
pdf.cell(w=166, h=8, txt="", border=0) #celula vazia para alocar a dde baixo na direita
pdf.cell(w=22, h=8, txt="center cell", align="R", border=1)

#Page 2
pdf.add_page()
pdf.cell(w=22, h=8, txt="Page 2", border="B", ln=1)
pdf.cell(w=22, h=8, txt="Cell 1", border="B")  # border na esquerda
pdf.cell(w=22, h=8, txt="Cell 2", border=1)

pdf.output("teste.pdf")