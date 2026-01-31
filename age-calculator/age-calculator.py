import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.title('Age Calculator')
try:
    icon = tk.PhotoImage(file='calculator.png')
    root.iconphoto(True, icon)
except:
    pass
root['background'] = 'black'


def calculate_age(day, month, year):
        date_of_birth = datetime(year=year, month=month, day=day)
        return datetime.now() - date_of_birth    

def get_age():
    try:
        return calculate_age(
            int(entry1.get()),
            int(entry2.get()),
            int(entry3.get())
            )
    except ValueError as e:
        error_handler_var.set(f"Error: {e}")
        return None

def total():
    age = get_age()
    if not age:
         return
    

    days = age.days
    years = days // 365
    months = (days % 365) // 30
    days = (days % 365) % 30

    result_var.set(f"You were here for {years} years, {months} months and {days} days")


def find_days():
     age = get_age()
     if not age:
          return
     result_var.set(f"Total days: {age.days}")


def find_seconds():
    age = get_age()
    if not age:
          return
    result_var.set(f"Total seconds: {round(age.total_seconds(), 2)}")

text1 = tk.Label(root, text = 'Date of Birth', font = ('Death Hector', 14), bg = 'black', fg = 'white').pack(padx=20, pady=10)

frame = tk.Frame(root)

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.columnconfigure(3, weight=1)
frame.columnconfigure(4, weight=1)
frame.columnconfigure(5, weight=1)


text1 = tk.Label(frame, text = 'Day: ', font = ('Death Hector', 12), bg = 'black', fg = 'white').grid(row = 0, column=0, sticky='WE')
entry1 = tk.Entry(frame, width=2, font = ('Death Hector', 12), bg = '#363636', fg = 'white')
entry1.grid(row=0, column=1, sticky='WE')

text2 = tk.Label(frame, text = '  Month: ', font = ('Death Hector', 12), bg = 'black', fg = 'white').grid(row = 0, column=2, sticky='WE')
entry2 = tk.Entry(frame, width=2, font = ('Death Hector', 12), bg = '#363636', fg = 'white')
entry2.grid(row=0, column=3, sticky='WE')

text3 = tk.Label(frame, text = '  Year: ', font = ('Death Hector', 12), bg = 'black', fg = 'white').grid(row = 0, column=4, sticky='WE')
entry3 = tk.Entry(frame, width=4, font = ('Death Hector', 12), bg = '#363636', fg = 'white')
entry3.grid(row=0, column=5, sticky='WE')



frame.pack(padx=10, pady=30, fill='x')

frame1 = tk.Frame(root, borderwidth=2)

frame1.columnconfigure(0, weight=1)
frame1.columnconfigure(1, weight=1)
frame1.columnconfigure(2, weight=1)

btn1 = tk.Button(frame1, text='Calculate\nAge', command= total, font = ('Death Hector', 10)).grid(row=0, column=0, sticky='WE')
btn2 = tk.Button(frame1, text='Calculate\nIn Days', command= find_days, font = ('Death Hector', 10)).grid(row=0, column=1, sticky='WE')
btn3 = tk.Button(frame1, text='Calculate\nIn Seconds', command= find_seconds, font = ('Death Hector', 10)).grid(row=0, column=2, sticky='WE')

frame1.pack(padx=20, pady=20, fill='x')

frame2 = tk.Frame(root)
frame2.pack(padx=20, pady=20, fill='x')

error_handler_var = tk.StringVar()
error_handler_label = tk.Label(root, textvariable=error_handler_var, fg='red', bg='black')
error_handler_label.pack()

result_var = tk.StringVar()
result_label = tk.Label(
    frame2,
    textvariable=result_var,
    font=('Death Hector', 10),
    bg='black',
    fg='white'
)
result_label.grid(row=0, column=0, sticky='WE')


root.mainloop()
