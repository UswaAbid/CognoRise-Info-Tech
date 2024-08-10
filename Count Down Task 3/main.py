import time
from tkinter import *
from tkinter import ttk, messagebox
from threading import *

# Hour list
hour_list = [i for i in range(25)]

# Minute and Second List
min_sec_list = [i for i in range(60)]

class CountDown:
    def __init__(self, root):
        self.window = root
        self.window.geometry("480x500+0+0")  # Window height set to 500
        self.window.title('CountDown Timer')
        self.window.configure(bg='#87CEEB')
        self.window.resizable(width=False, height=False)

        self.pause = False

        # Labels for time setup
        time_label = Label(self.window, text="Set Time", 
        font=("times new roman", 20, "bold"), bg='#87CEEB', fg='black')
        time_label.place(x=180, y=25)

        hour_label = Label(self.window, text="Hour", 
        font=("times new roman", 15), bg='#87CEEB', fg='black')
        hour_label.place(x=50, y=75)

        minute_label = Label(self.window, text="Minute", 
        font=("times new roman", 15), bg='#87CEEB', fg='black')
        minute_label.place(x=200, y=75)

        second_label = Label(self.window, text="Second", 
        font=("times new roman", 15), bg='#87CEEB', fg='black')
        second_label.place(x=350, y=75)


        # Comboboxes for selecting time
        self.hour = IntVar()
        self.hour_combobox = ttk.Combobox(self.window, width=7, 
        height=10, textvariable=self.hour, 
        font=("times new roman", 15))
        self.hour_combobox['values'] = hour_list
        self.hour_combobox.current(0)
        self.hour_combobox.place(x=50, y=110)

        self.minute = IntVar()
        self.minute_combobox = ttk.Combobox(self.window, width=7, 
        height=10, textvariable=self.minute, 
        font=("times new roman", 15))
        self.minute_combobox['values'] = min_sec_list
        self.minute_combobox.current(0)
        self.minute_combobox.place(x=200, y=110)

        self.second = IntVar()
        self.second_combobox = ttk.Combobox(self.window, width=7, 
        height=10, textvariable=self.second, 
        font=("times new roman", 15))
        self.second_combobox['values'] = min_sec_list
        self.second_combobox.current(0)
        self.second_combobox.place(x=350, y=110)

        # Buttons for control
        cancel_button = Button(self.window, text='Cancel', 
        font=('Helvetica', 12), bg="gray", fg="white", width=7, 
        height=1, command=self.Cancel)
        cancel_button.place(x=125, y=170)

        set_button = Button(self.window, text='Set', 
        font=('Helvetica', 12), bg="blue", fg="white", width=7, 
        height=1, command=self.Get_Time)
        set_button.place(x=280, y=170)

        # Time Left Label (Initially hidden)
        self.time_left_label = Label(self.window, text="Time Left", 
        font=("times new roman", 20, "bold"), bg='#87CEEB', fg='black')

        # Countdown Timer Display (Initially hidden)
        self.time_display = Label(self.window, 
        font=("times new roman", 60, "bold"), bg='#87CEEB', fg='black')

    def Cancel(self):
        self.pause = True
        self.window.destroy()

    def Get_Time(self):
        try:
            h = int(self.hour_combobox.get()) * 3600
            m = int(self.minute_combobox.get()) * 60
            s = int(self.second_combobox.get())
            self.time_left = h + m + s

            if s == 0 and m == 0 and h == 0:
                messagebox.showwarning('Warning!', 'Please select a valid time to set')
            else:
                start_button = Button(self.window, text='Start', 
                font=('Helvetica', 12), bg="green", fg="white", width=7, 
                height=1, command=self.Threading)
                start_button.place(x=125, y=230)

                pause_button = Button(self.window, text='Pause', 
                font=('Helvetica', 12), bg="red", fg="white", width=7, 
                height=1, command=self.pause_time)
                pause_button.place(x=280, y=230)

        except Exception as es:
            messagebox.showerror("Error!", f"Error due to {es}")

    def Threading(self):
        self.x = Thread(target=self.start_time, daemon=True)
        self.x.start()

    def start_time(self):
        self.pause = False

        # Display the "Time Left" label and countdown timer after starting
        self.time_left_label.place(x=180, y=300)
        self.time_display.place(x=90, y=360)

        while self.time_left > 0:
            mins, secs = divmod(self.time_left, 60)
            hours = 0
            if mins > 60:
                hours, mins = divmod(mins, 60)

            self.time_display.config(text=f"{hours:02}:{mins:02}:{secs:02}")
            self.time_display.update()
            time.sleep(1)
            self.time_left -= 1

            if self.time_left <= 0:
                messagebox.showinfo('Time Over', 'Please ENTER to stop')
                
            if self.pause:
                break

    def pause_time(self):
        self.pause = True
        mins, secs = divmod(self.time_left, 60)
        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)

        self.time_display.config(text=f"{hours:02}:{mins:02}:{secs:02}")
        self.time_display.update()

if __name__ == "__main__":
    root = Tk()
    obj = CountDown(root)
    root.mainloop()
