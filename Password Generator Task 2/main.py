import customtkinter
from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
import os


app = customtkinter.CTk()
app.title(' Password Generator')
app.geometry('400x300+480+200')
app.config(bg='#000')
app.resizable(True,True)
app.iconbitmap('key.ico')

title_font = ('Arial', 18, 'bold')
subtitle_font = ('Arial', 14, 'bold')
password_font = ('Arial', 14, 'bold') 
button_font = ('Arial', 18, 'bold')

min_password_length = 6
max_password_length = 30
default_password_length = 10


def generate_password():
    password_length = password_length_var.get()
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_text_box.configure(state = 'normal')
    password_text_box.delete(0, END)
    password_text_box.insert(0, password)
    password_text_box.configure(state = 'disabled')

def copy_password():
    password = password_text_box.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo(title='Copied', message='Password successfully copied to your clipboard.')
    else:
        messagebox.showerror(title='Error', message='Generate a password to copy.')    

def update_length_value(*args):
    length_label.configure(text = f"Password length: {password_length_var.get()}")



title_label = customtkinter.CTkLabel(app, text = 'Password Generator', font = title_font, text_color = '#FFF', bg_color = '#000' )
title_label.place(x=115, y=25)

password_text_box = customtkinter.CTkEntry(app, font = password_font, state ='disabled', text_color='#FFF', fg_color ='#000', border_color ='#BF40BF', width=280, height=30 )
password_text_box.place(x=55, y=70)

length_label = customtkinter.CTkLabel(app, text=f"Password Length: { default_password_length}", font = subtitle_font, text_color='#FFF', bg_color = '#000')
length_label.place(x=55, y=122)

password_length_var = IntVar(value=default_password_length)
password_length_var.trace_add('write', update_length_value)

length_slider = customtkinter.CTkSlider(app, from_=min_password_length, to=max_password_length, progress_color='#E0B0FF', button_color= '#DA70D6',button_hover_color= '#DA70D6', fg_color= '#FFF', bg_color= '#000',height = 19, width = 290, variable = password_length_var )
length_slider.place(x=50, y=170)

generate_button = customtkinter.CTkButton(app, command = generate_password, font = button_font, text_color = '#FFF', text = 'Generate', fg_color = '#680289', hover_color = '#BF40BF', bg_color = '#000', cursor = 'hand2', corner_radius = 8, width = 110, height = 40 )
generate_button.place(x=70, y=220)

copy_button = customtkinter.CTkButton(app, command = copy_password, font = button_font, text_color = '#FFF', text = 'Copy', fg_color = '#680289', hover_color = '#BF40BF', bg_color = '#000', cursor = 'hand2', corner_radius = 8, width = 110, height = 40 )
copy_button.place(x=215, y=220)

app.mainloop()