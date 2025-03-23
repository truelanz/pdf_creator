import sqlite3
from fpdf import FPDF

# Criar um objeto PDF
pdf = FPDF("P", "mm", "A4")
pdf.set_font("Arial", "B", 12)
pdf.set_margins(20, 10, 20)
pdf.add_page()

# Definir largura das colunas
col_width_id = 20
col_width_name = 90
col_width_age = 50

# Cabeçalho da tabela
pdf.set_fill_color(126, 195, 222)
pdf.cell(col_width_id, 7, "ID", border=1, fill=True)
pdf.cell(col_width_name, 7, "Name", border=1, fill=True)
pdf.cell(col_width_age, 7, "Age", border=1, fill=True)
pdf.ln()  # Pular para a próxima linha

# Conectar ao banco de dados
con = sqlite3.connect("meu_banco.db")
cursor = con.cursor()

# Buscar todos os usuários
# id [0], nome [1], idade [2]
cursor.execute("SELECT id, nome, idade FROM usuarios")
usuarios = cursor.fetchall()

# Verificar se há dados antes de imprimir
if not usuarios:
    pdf.cell(0, 10, "Nenhum usuário encontrado.", border=1, ln=True, align="C")
else:
    # Preencher tabela com os dados
    for user in usuarios:
        pdf.cell(col_width_id, 7, str(user[0]), border=1)  # ID
        pdf.cell(col_width_name, 7, str(user[1]), border=1)  # Nome
        pdf.cell(col_width_age, 7, str(user[2]), border=1)  # Idade
        pdf.ln()  # Nova linha

# Fechar conexão com o banco
con.close()

# Salvar o PDF
pdf.output("readFromDB.pdf")
