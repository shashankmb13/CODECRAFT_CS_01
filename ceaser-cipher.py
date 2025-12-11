import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Caesar Cipher Functions -------------------------------------
def caesar_encrypt(message, shift):
    encrypted = ""
    for char in message:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char
    return encrypted


def caesar_decrypt(message, shift):
    decrypted = ""
    for char in message:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted += char
    return decrypted

# GUI Functions --------------------------------------------------
def encrypt_text():
    msg = input_msg.get("1.0", tk.END).strip()
    if not msg:
        messagebox.showwarning("Warning", "Please enter a message.")
        return
    try:
        shift = int(shift_value.get())
    except:
        messagebox.showerror("Error", "Shift must be a number.")
        return
    output_msg.delete("1.0", tk.END)
    output_msg.insert(tk.END, caesar_encrypt(msg, shift))


def decrypt_text():
    msg = input_msg.get("1.0", tk.END).strip()
    if not msg:
        messagebox.showwarning("Warning", "Please enter a message.")
        return
    try:
        shift = int(shift_value.get())
    except:
        messagebox.showerror("Error", "Shift must be a number.")
        return
    output_msg.delete("1.0", tk.END)
    output_msg.insert(tk.END, caesar_decrypt(msg, shift))


def clear_all():
    input_msg.delete("1.0", tk.END)
    output_msg.delete("1.0", tk.END)
    shift_value.delete(0, tk.END)


# Main GUI Window -----------------------------------------------
root = tk.Tk()
root.title("Caesar Cipher - GUI")
root.geometry("500x500")
root.resizable(False, False)

title = ttk.Label(root, text="Caesar Cipher (Encrypt / Decrypt)", font=("Arial", 16, "bold"))
title.pack(pady=10)

# Input Frame
input_frame = ttk.LabelFrame(root, text="Enter Message")
input_frame.pack(fill="x", padx=20, pady=10)

input_msg = tk.Text(input_frame, height=5, width=50)
input_msg.pack(padx=10, pady=10)

# Shift Value
shift_label = ttk.Label(root, text="Shift Value:")
shift_label.pack()
shift_value = ttk.Entry(root, width=10, justify="center")
shift_value.pack()

# Buttons Frame
btn_frame = ttk.Frame(root)
btn_frame.pack(pady=15)

encrypt_btn = ttk.Button(btn_frame, text="Encrypt", width=15, command=encrypt_text)
encrypt_btn.grid(row=0, column=0, padx=10)

decrypt_btn = ttk.Button(btn_frame, text="Decrypt", width=15, command=decrypt_text)
decrypt_btn.grid(row=0, column=1, padx=10)

clear_btn = ttk.Button(btn_frame, text="Clear", width=15, command=clear_all)
clear_btn.grid(row=0, column=2, padx=10)

# Output Frame
output_frame = ttk.LabelFrame(root, text="Output")
output_frame.pack(fill="x", padx=20, pady=10)

output_msg = tk.Text(output_frame, height=5, width=50)
output_msg.pack(padx=10, pady=10)

# Exit Button
exit_btn = ttk.Button(root, text="Exit", command=root.destroy)
exit_btn.pack(pady=10)

# Run the GUI
root.mainloop()
