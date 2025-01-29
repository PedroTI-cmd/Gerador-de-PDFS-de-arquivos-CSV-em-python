import pandas as pd 
from fpdf import FPDF
import customtkinter as ctk
from tkinter import filedialog, messagebox


ctk.set_appearance_mode("light")  
ctk.set_default_color_theme("blue")  

janela = ctk.CTk()
janela.title("Gerador de Resumo de CSV")
janela.geometry("700x700")
janela.configure(bg="yellow")


def carregar_csv():
    caminho_arquivo = filedialog.askopenfilename(filetypes=[("Arquivos CSV", "*.csv")])
    if caminho_arquivo:
        try:
            global df
            df = pd.read_csv(caminho_arquivo)
            messagebox.showinfo("Sucesso", "Arquivo carregado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar arquivo: {e}")

def gerar_pdf():
    try:
        resumo = df.describe()
        class PDF(FPDF):
            def header(self):
                self.set_font("Arial", "B", 12)
                self.cell(200, 10, "Relatório Automático", ln=True, align="C")
            def footer(self):
                self.set_y(-15)
                self.set_font("Arial", "I", 8)
                self.cell(0, 10, f'Página {self.page_no()}', align="C")
        
        pdf = PDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, "Resumo dos Dados", ln=True, align="C")
        for col in resumo.columns:
            pdf.cell(0, 10, f"{col}: Média = {resumo[col]['mean']:.2f}, Máx = {resumo[col]['max']:.2f}", ln=True)
        pdf.output("relatorio.pdf")
        messagebox.showinfo("Sucesso", "Relatório gerado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao gerar PDF: {e}")


botao_carregar = ctk.CTkButton(janela, text="Carregar CSV", command=carregar_csv)
botao_carregar.pack(pady=20)

botao_gerar = ctk.CTkButton(janela, text="Gerar PDF", command=gerar_pdf)
botao_gerar.pack(pady=20)

janela.mainloop()
