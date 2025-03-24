
import sqlite3
from fpdf import FPDF

#Header and Footer
class FPDF(FPDF):
    def header(self):
        self.set_y(0)
        self.cell(0, 10, "This is a Header, by truelanz", align="C", border=0, ln=1)
        self.ln(15)

    def footer(self): # Page Number
        self.set_y(-10)
        self.set_x(-10)

        pageNumber = self.page_no()
        self.cell(w=5, h=10, txt=str(pageNumber), border=0)
        
# Criar um objeto PDF
pdf = FPDF("P", "mm", "A4")  
pdf.set_font("Arial", "", 12)
pdf.add_page()


# Definir largura das colunas
col_width_cat = 40
col_width_prod = 65
col_before_after = 20
col_width_date = 45

#Altura e Largura da pagina:
w = 210
h = 297

# Cabeçalho da tabela products
pdf.set_font("Arial", "B", 12)
pdf.cell(w=0, h=10, txt="Produtos alterados", border=0, ln=1)
pdf.set_fill_color(126, 195, 222)
pdf.cell(col_width_cat, 7, "Categoria", border=1, fill=True)
pdf.cell(col_width_prod, 7, "Produtos", border=1, fill=True)
pdf.cell(col_before_after, 7, "antes", border=1, fill=True)
pdf.cell(col_before_after, 7, "depois", border=1, fill=True)
pdf.cell(col_width_date, 7, "Data", border=1, fill=True)
pdf.ln()  # Pular para a próxima linha

pdf.set_font("Arial", "", 12)

def join_tables(filter="all", month=None, year=None):
    con = sqlite3.connect("products.db")
    cursor = con.cursor()

    # Construindo a query base
    query = """
        SELECT p.category, p.product, h.quantity_before, h.quantity_after,
         strftime('%d/%m/%Y %H:%M:%S', h.data_modify) as data_formatada
        FROM products AS p
        INNER JOIN quantity_history AS h
        ON p.id_prod = h.prod_hist
    """

    # Adicionando filters dinâmicos de data
    if filter == "hoje":
        query += " WHERE DATE(h.data_modify) = DATE('now')"
    elif filter == "semana":
        query += " WHERE DATE(h.data_modify) >= DATE('now', '-7 days')"
    elif filter == "mes":
        query += " WHERE strftime('%Y-%m', h.data_modify) = strftime('%Y-%m', 'now')"
    elif filter == "mes_anterior":
        query += " WHERE strftime('%Y-%m', h.data_modify) = strftime('%Y-%m', 'now', '-1 month')"
    elif filter == "personalizado" and month and year:
        query += f" WHERE strftime('%Y-%m', h.data_modify) = '{year}-{str(month).zfill(2)}'"

    query += " ORDER BY h.data_modify DESC;"  # Ordenação por data mais recente primeiro

    # Executar a query
    cursor.execute(query)

    # Obter os resultados antes de fechar a conexão
    results = cursor.fetchall()

    # Fechar conexão
    con.close()
    
    if not results:
        pdf.set_text_color(255, 0, 0)
        pdf.cell(
            0, 7, "Nenhum dado encontrado para o filtro de data selecionada", border=1
        )
        pdf.set_text_color(0, 0, 0)
        pdf.ln()
    else:
        for product in results:
            pdf.set_text_color(0, 0, 0)  # Definir cor preta para o texto
            pdf.cell(col_width_cat, 7, str(product[0]), border=1)
            pdf.cell(col_width_prod, 7, str(product[1]), border=1)
            pdf.cell(col_before_after, 7, str(product[2]), border=1)
            pdf.cell(col_before_after, 7, str(product[3]), border=1)
            pdf.cell(col_width_date, 7, str(product[4]), border=1)
            pdf.ln()


join_tables("mes_anterior")

# Salvar o PDF
pdf.output("readFromDB.pdf")
