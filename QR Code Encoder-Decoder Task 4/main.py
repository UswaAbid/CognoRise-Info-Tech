from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from pyzbar.pyzbar import decode
import pyqrcode
import os

root = Tk()
root.title("QR Code Application")

root.configure(bg="light blue")

root.geometry("440x450")

root.resizable(False, False)

note = ttk.Notebook(root)
note.pack(fill="both", expand=True)

frame1 = Frame(note, bg="light blue")  # Set background of frame1 to light blue
frame2 = Frame(note, bg="light blue")  # Set background of frame2 to light blue

s = ttk.Style()
s.theme_create("style", parent="alt", settings={
    "TNotebook.Tab": {
        "configure": {
            "padding": [65, 5],
            "font": ('Times', '13', 'bold'),
            "width": 27,
            "focuscolor": "none",
            "focusthickness": 0,
            "background": "light grey",
            "foreground": "black"
        },
        "map": {
            "background": [("selected", "#FFD700")],  # Map background color when selected
            "foreground": [("selected", "black")]    # Map foreground color when selected
        }
    }
})

s.theme_use("style")

note.add(frame1, text="Encode QR")
note.add(frame2, text="Decode QR")

canvas1 = Canvas(frame1, width=350, height=200, relief=RIDGE, bd=2)
canvas1.pack(padx=10, pady=22)

canvas2 = Canvas(frame2, width=350, height=320, relief=RIDGE, bd=2)
canvas2.pack(padx=10, pady=22)

def generate():
    global info

    if 'info' in globals() and info.winfo_exists():
        info.destroy()

    if data_entry.get() != '' and save_entry.get() != '':
        qr = pyqrcode.create(data_entry.get())
        img = qr.png(save_entry.get() + ".png", scale=5.5)
        
        img = Image.open(save_entry.get() + ".png")
        img = ImageTk.PhotoImage(img)
        canvas1.create_image(180, 105, image=img)
        canvas1.image = img
    else:
        info = Label(frame1, text="Please enter the data for QR Code", font=('ariel 12 bold'), bg='light blue')  # Set the label background to light blue
        info.place(x=87, y=120)

def selected():
    canvas2.delete("all")

    img_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image",
                                          filetype=(("PNG file", "*.png"), ("All files", "*.")))

    if img_path:
        img = Image.open(img_path)
        img.thumbnail((150, 150))
        img = ImageTk.PhotoImage(img)
        canvas2.create_image(105, 10, anchor=NW, image=img)
        canvas2.image = img

        d = decode(Image.open(img_path))
        if d:
            data = d[0].data.decode()
            wrapped_text = canvas2.create_text(10, 180, anchor=NW, text=data, font=('Arial', 12), fill='black', width=330)
        else:
            canvas2.create_text(10, 180, anchor=NW, text="No QR code detected.", font=('Arial', 12), fill='black', width=330)

data_label = Label(frame1, text='Enter Data:', font=("Arial", 10, "bold"), bg='light blue')  # Set the label background to light blue
data_label.place(x=60, y=250)

save_label = Label(frame1, text='Specify Name:', font=("Arial", 10, "bold"), bg='light blue')  # Set the label background to light blue
save_label.place(x=50, y=285)

data_entry = Entry(frame1, font=('Arial', 10), relief=GROOVE, bd=2)
data_entry.place(x=161, y=250, width=220)

save_entry = Entry(frame1, font=('Arial', 10), relief=GROOVE, bd=2)
save_entry.place(x=161, y=285, width=220)

btn1 = Button(frame1, text="Generate", bg="light grey", fg="Black", width=10, font=('Arial', 12), relief=GROOVE, command=generate)
btn1.place(x=95, y=345)

btn2 = Button(frame1, text="Exit", bg="light grey", fg="Black", width=10, font=('Arial', 12), relief=GROOVE, command=root.destroy)
btn2.place(x=245, y=345)

btn1 = Button(frame2, text="Select Image", bg="light grey", fg="Black", width=15, font=('Arial', 12), relief=GROOVE, takefocus=False, command=selected)
btn1.place(x=43, y=365)

btn2 = Button(frame2, text="Exit", bg="light grey", fg="Black", width=10, font=('Arial', 12), relief=GROOVE, takefocus=False, command=root.destroy)
btn2.place(x=295, y=365)

root.mainloop()
