from fpdf import FPDF

pdf = FPDF("P", "mm", "A4")

w = 210
h = 297

pdf.set_font(family="Arial", style="B", size=16 )
pdf.set_margins(0, 0, 0)


#Page 1
pdf.add_page()
pdf.cell(w=22, h=8, txt="Page 1", border=1, ln=1)
pdf.set_author("truelanz")
pdf.set_title("PDF with images")

# Adicionar imagem no pdf
aguy = pdf.image(name="assets/aGuy.jpg", x=55, y=50, w=100, h=100)

pdf.output("images.pdf")