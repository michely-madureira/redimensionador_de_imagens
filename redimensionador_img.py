from tkinter import *
from PIL import Image
from tkinter.filedialog import *
from tkinter import messagebox

# Definição de cores
cor1 = "#ffffff"   # branco
cor2 = "#cf0e0e"   # vermelho
cor3 = "#0050c3"   # azul
cor4 = "#f3d500"   # amarelo
cor5 = "#46c001"   # verde

# Configuração da janela principal
janela = Tk()
janela.geometry("420x550")
janela.title("Redimensione Imagens")
janela.configure(background=cor3)
janela.resizable(False, False)

# Criação do frame principal
frame = Frame(janela, width=420, height=550, background=cor3, relief="flat")
frame.grid(row=0, column=0, sticky=NSEW)

# Título do aplicativo
app_name = Label(frame, text="Redimensionar Imagem", width=24, height=1, anchor=CENTER,
                 pady=10, padx=10, relief="flat", font=("Lato 20 bold"), bg=cor3, fg=cor1)
app_name.grid(row=0, column=0, columnspan=2, sticky=NSEW, pady=1)

# Frase de instrução
instrucao_texto = "Redimensione imagens definindo o tamanho ideal dos seus arquivos sem perder a qualidade original."
instrucao = Label(frame, text=instrucao_texto, wraplength=380, anchor=CENTER,
                  pady=10, padx=10, relief="flat", font=("Lato", 14, "bold"), bg="#ffffff", fg="#0050c3")
instrucao.grid(row=1, column=0, columnspan=2, sticky=NSEW, pady=(20, 0))


def novoArquivo():
    # Abrir imagem
    ficheiro = askopenfilename(
        filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.bmp"), ("Todos os arquivos", "*.*")])
    if not ficheiro:
        return  # Se nenhum arquivo for selecionado, não faz nada

    img = Image.open(ficheiro)
    img_altura, img_largura = img.size

    def converter():
        altura = entrada_altura.get()
        largura = entrada_largura.get()

        # Validação de entrada
        if not (altura.isdigit() and largura.isdigit()):
            messagebox.showerror(
                "Erro de Entrada", "Por favor, insira apenas números inteiros para altura e largura.")
            return

        altura = int(altura)
        largura = int(largura)

        novo_valor = (altura, largura)

        nova_img = img.resize(novo_valor)

        # Mensagem para o usuário
        img_salvar = asksaveasfilename(defaultextension=".jpg", filetypes=[
                                       ("JPEG files", "*.jpg"), ("All files", "*.*")])
        if img_salvar:
            nova_img.save(img_salvar)
            messagebox.showinfo(
                "Sucesso", "A imagem foi convertida e salva com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Operação cancelada pelo usuário.")

        # Limpar widgets após a conversão
        limpar_widgets()
        inicializar_widgets()

    # Labels e campos de entrada para altura e largura
    tamanho_original = Label(frame, text=f"Altura e Largura original: {img_altura} x {img_largura}", width=24, height=1, anchor=CENTER,
                             pady=7, padx=10, relief="flat", font=("Lato 15 bold"), bg=cor3, fg=cor4)
    tamanho_original.grid(row=3, column=0, columnspan=2, sticky=NSEW, pady=20)

    nova_altura = Label(frame, text="Digite nova altura", width=10, height=1, anchor=CENTER,
                        pady=7, padx=10, relief="flat", font=("Lato 11 bold"), bg=cor3, fg=cor1)
    nova_altura.grid(row=4, column=0, sticky=NSEW, pady=3)

    nova_largura = Label(frame, text="Digite nova largura", width=10, height=1, anchor=CENTER,
                         pady=7, padx=10, relief="flat", font=("Lato 11 bold"), bg=cor3, fg=cor1)
    nova_largura.grid(row=4, column=1, sticky=NSEW, pady=3)

    entrada_altura = Entry(frame, width=15, font=("Lato 15"), justify="center")
    entrada_altura.grid(row=5, column=0, pady=10)

    entrada_largura = Entry(
        frame, width=15, font=("Lato 15"), justify="center")
    entrada_largura.grid(row=5, column=1, pady=10)

    # Botão para converter
    b_converter = Button(frame, text="Converter", width=10, height=1, font=("Lato 15 bold"),
                         anchor=CENTER, relief=RAISED, bg=cor5, fg=cor1, command=converter)
    b_converter.grid(row=6, column=0, columnspan=2, pady=30)


def limpar_widgets():
    # Remove widgets que foram adicionados durante o processo de conversão
    for widget in frame.winfo_children():
        if widget not in [app_name, instrucao, b_novo]:
            widget.grid_forget()


def inicializar_widgets():
    # Recria o botão "Inserir" e reposiciona-o para manter o layout
    b_novo.grid(row=2, column=0, columnspan=2, pady=20)


# Botão para selecionar novo arquivo
b_novo = Button(frame, text="Inserir", width=10, height=1, font=("Lato 15 bold"),
                anchor=CENTER, relief=RAISED, bg=cor2, fg=cor1, command=novoArquivo)

# Inicializar a interface
inicializar_widgets()

janela.mainloop()
