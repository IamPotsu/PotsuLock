from pathlib import Path
import tkinter as tk
from tkinter import messagebox
from Auth import gerar_senha
import pygame

pygame.mixer.init()

PASTA = Path(__file__).parent


def tocar_audio(nome_arquivo):
    pygame.mixer.music.load(str(PASTA / nome_arquivo))
    pygame.mixer.music.play()


def verificar_nome():
    usuario = entry_usuario.get().strip()

    if not usuario:
        messagebox.showwarning(
            "Atenção",
            "Por favor, insira o nome de usuário."
        )
        entry_usuario.focus()
        return None

    return usuario


def mostrar_creditos():
    creditos = tk.Toplevel(root)
    creditos.title("Créditos")
    creditos.geometry("380x220")
    creditos.resizable(False, False)
    creditos.configure(bg="#f4f6f9")

    tk.Label(
        creditos,
        text="Créditos",
        font=("Segoe UI", 16, "bold"),
        bg="#f4f6f9",
        fg="#2c3e50",
    ).pack(pady=(20, 10))

    texto_creditos = (
        "Desenvolvido por Potsu\n"
        "Luan Lopes Nascimento\n\n"
        "Com auxílio de Inteligência Artificial"
    )

    tk.Label(
        creditos,
        text=texto_creditos,
        font=("Segoe UI", 11),
        bg="#f4f6f9",
        fg="#555555",
        justify="center",
    ).pack(pady=5)

    tk.Button(
        creditos,
        text="Fechar",
        command=creditos.destroy,
        font=("Segoe UI", 10, "bold"),
        bg="#3498db",
        fg="white",
        activebackground="#2980b9",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        width=12,
        pady=5,
    ).pack(pady=15)


def verificar_autenticacao():
    usuario = verificar_nome()

    if usuario is None:
        return

    senha_digitada = entry_senha.get()
    senha_gerada = gerar_senha(usuario)

    if senha_digitada == senha_gerada:
        tocar_audio("duolingo-correct.mp3")
        messagebox.showinfo(
            "Autenticação",
            "Senha correta! Acesso concedido."
        )
        mostrar_creditos()
    else:
        tocar_audio("duolingo-wrong.mp3")
        messagebox.showerror(
            "Autenticação",
            "Senha incorreta! Acesso negado."
        )


def gerar_e_copiar_senha():
    usuario = verificar_nome()

    if usuario is None:
        return

    senha = gerar_senha(usuario)

    root.clipboard_clear()
    root.clipboard_append(senha)
    root.update()

    messagebox.showinfo(
        "Senha gerada",
        f"Senha: {senha}\n\n"
        "A senha foi copiada para a área de transferência.",
    )


root = tk.Tk()
root.title("Autenticação de Usuário")
root.geometry("320x330")
root.resizable(False, False)
root.configure(bg="#f4f6f9")

tk.Label(
    root,
    text="Painel de Acesso",
    font=("Segoe UI", 16, "bold"),
    bg="#f4f6f9",
    fg="#2c3e50",
).pack(pady=(15, 10))

tk.Label(
    root,
    text="Nome de Usuário:",
    font=("Segoe UI", 10, "bold"),
    bg="#f4f6f9",
    fg="#555555",
).pack(anchor="w", padx=30)

entry_usuario = tk.Entry(
    root,
    font=("Segoe UI", 11),
    relief="solid",
    bd=1,
)
entry_usuario.pack(pady=(2, 8), ipadx=10, ipady=3)

tk.Label(
    root,
    text="Senha:",
    font=("Segoe UI", 10, "bold"),
    bg="#f4f6f9",
    fg="#555555",
).pack(anchor="w", padx=30)

entry_senha = tk.Entry(
    root,
    show="*",
    font=("Segoe UI", 11),
    relief="solid",
    bd=1,
)
entry_senha.pack(pady=(2, 12), ipadx=10, ipady=3)

btn_autenticar = tk.Button(
    root,
    text="Autenticar",
    command=verificar_autenticacao,
    font=("Segoe UI", 10, "bold"),
    bg="#27ae60",
    fg="white",
    activebackground="#219653",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    width=22,
    pady=5,
)
btn_autenticar.pack(pady=3)

btn_versenha = tk.Button(
    root,
    text="Gerar e Copiar Senha",
    command=gerar_e_copiar_senha,
    font=("Segoe UI", 10, "bold"),
    bg="#3498db",
    fg="white",
    activebackground="#2980b9",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    width=22,
    pady=5,
)
btn_versenha.pack(pady=3)

root.mainloop()