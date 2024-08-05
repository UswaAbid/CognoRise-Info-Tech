
import customtkinter
from tkinter import *
from tkinter import messagebox

app = customtkinter.CTk()
app.title('Calculator')
app.geometry('270x305')
app.config(bg='#000')
app.resizable(True, True)

font1 = ('Arial', 20,'bold')


def button_click(number):
    if equation_entry.get() == "Error":
        clear()
    equation_entry.insert(END, number)

def clear():
    equation_entry.delete(0, END)

def calculate():
    try:
        equation = equation_entry.get()
        new_equation = equation.replace('x','*')
        result = eval(new_equation)
        clear()
        equation_entry.insert(0, result)
    except ZeroDivisionError:
        clear()
        equation_entry.insert(0, "Error")
    except:
        clear()
        equation_entry.insert(0, "Error")


equation_entry = customtkinter.CTkEntry(app, font = font1, text_color = '#fff', fg_color = '#000', corner_radius=0, border_color = '#222222', width = 240, height = 50 )
equation_entry.place(x=15, y=20)

b1_button = customtkinter.CTkButton(app, command = lambda: button_click('7'), font = font1, text_color = '#fff', text = '7', corner_radius=15, fg_color ='#222222', hover_color = '#3b3b3b', bg_color= '#000', cursor = 'hand2', width = 50 )
b1_button.place(x=15, y=90)

b2_button = customtkinter.CTkButton(app, command = lambda: button_click('8'), font = font1, text_color = '#fff', text = '8', corner_radius=15, fg_color ='#222222', hover_color = '#3b3b3b', bg_color= '#000', cursor = 'hand2', width = 50 )
b2_button.place(x=75, y=90)

b3_button = customtkinter.CTkButton(app, command = lambda: button_click('9'), font = font1, text_color = '#fff', text = '9', corner_radius=15, fg_color ='#222222', hover_color = '#3b3b3b', bg_color= '#000', cursor = 'hand2', width = 50 )
b3_button.place(x=135, y=90)

b4_button = customtkinter.CTkButton(app, command = lambda: button_click('4'), font = font1, text_color = '#fff', text = '4', corner_radius=15, fg_color ='#222222', hover_color = '#3b3b3b', bg_color= '#000', cursor = 'hand2', width = 50 )
b4_button.place(x=15, y=130)

b5_button = customtkinter.CTkButton(app, command = lambda: button_click('5'), font = font1, text_color = '#fff', text = '5', corner_radius=15, fg_color ='#222222', hover_color = '#3b3b3b', bg_color= '#000', cursor = 'hand2', width = 50 )
b5_button.place(x=75, y=130)

b6_button = customtkinter.CTkButton(app, command = lambda: button_click('6'), font = font1, text_color = '#fff', text = '6', corner_radius=15, fg_color ='#222222', hover_color = '#3b3b3b', bg_color= '#000', cursor = 'hand2', width = 50 )
b6_button.place(x=135, y=130)

b7_button = customtkinter.CTkButton(app, command = lambda: button_click('1'), font = font1, text_color = '#fff', text = '1', corner_radius=15, fg_color ='#222222', hover_color = '#3b3b3b', bg_color= '#000', cursor = 'hand2', width = 50 )
b7_button.place(x=15, y=170)

b8_button = customtkinter.CTkButton(app, command = lambda: button_click('2'), font = font1, text_color = '#fff', text = '2', corner_radius=15, fg_color ='#222222', hover_color = '#3b3b3b', bg_color= '#000', cursor = 'hand2', width = 50 )
b8_button.place(x=75, y=170)

b9_button = customtkinter.CTkButton(app, command = lambda: button_click('3'), font = font1, text_color = '#fff', text = '3', corner_radius=15, fg_color ='#222222', hover_color = '#3b3b3b', bg_color= '#000', cursor = 'hand2', width = 50 )
b9_button.place(x=135, y=170)

b10_button = customtkinter.CTkButton(app, command = lambda: button_click('0'), font = font1, text_color = '#fff', text = '0', corner_radius=15, fg_color ='#222222', hover_color = '#3b3b3b', bg_color= '#000', cursor = 'hand2', width = 50 )
b10_button.place(x=15, y=210)

b11_button = customtkinter.CTkButton(app, command = lambda: button_click('.'), font = font1, text_color = '#fff', text = '.', corner_radius=15, fg_color ='#222222', hover_color = '#3b3b3b', bg_color= '#000', cursor = 'hand2', width = 50 )
b11_button.place(x=75, y=210)

b12_button = customtkinter.CTkButton(app, command = clear, font = font1, text_color = '#ad290e', text = 'C', corner_radius=15, fg_color ='#222222', hover_color = '#3b3b3b', bg_color= '#000', cursor = 'hand2', width = 50 )
b12_button.place(x=135, y=210)

b13_button = customtkinter.CTkButton(app, command = calculate, font = font1, text_color = '#fff', text = '=', corner_radius=15, fg_color ='#0039a6', hover_color = '#318CE7', bg_color= '#000', cursor = 'hand2', width = 240 )
b13_button.place(x=15, y=255)

b14_button = customtkinter.CTkButton(app, command = lambda: button_click('+'), font = font1, text_color = '#007FFF', text = '+', corner_radius=15, fg_color ='#222222', hover_color = '#3b3b3b', bg_color= '#000', cursor = 'hand2', width = 60 )
b14_button.place(x=195, y=90)

b15_button = customtkinter.CTkButton(app, command = lambda: button_click('-'), font = font1, text_color = '#007FFF', text = '-', corner_radius=15, fg_color ='#222222', hover_color = '#3b3b3b', bg_color= '#000', cursor = 'hand2', width = 60 )
b15_button.place(x=195, y=130)

b16_button = customtkinter.CTkButton(app, command = lambda: button_click('x'), font = font1, text_color = '#007FFF', text = 'x', corner_radius=15, fg_color ='#222222', hover_color = '#3b3b3b', bg_color= '#000', cursor = 'hand2', width = 60 )
b16_button.place(x=195, y=170)

b17_button = customtkinter.CTkButton(app, command = lambda: button_click('/'), font = font1, text_color = '#007FFF', text = '/', corner_radius=15, fg_color ='#222222', hover_color = '#3b3b3b', bg_color= '#000', cursor = 'hand2', width = 60 )
b17_button.place(x=195, y=210)



app.mainloop()
