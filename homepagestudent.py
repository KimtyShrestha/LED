import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkcalendar import Calendar
from datetime import datetime
from tkinter import Tk, Label




def update_image():
    selected_event = event_name_var.get()
    if selected_event == "Holi":
        image_label_frame.config(image=img2)
    elif selected_event == "Diwali":
        image_label_frame.config(image=img3)
    elif selected_event == "Christmas":
        image_label_frame.config(image=img4)
    elif selected_event == "New Year":
        image_label_frame.config(image=img5)
    elif selected_event == "Sports":
        image_label_frame.config(image=img6)
    elif selected_event == "Valentine's Day":
        image_label_frame.config(image=img7)
    elif selected_event == "Tours":
        image_label_frame.config(image=img8)
    elif selected_event == "Sarswati puja":
        image_label_frame.config(image=img9)
    elif selected_event == "Dashain":
        image_label_frame.config(image=img10)

def change_mode():
    mode = mode_var.get()
    if mode == "Student":
        event_names = ["Holi", "Diwali", "Christmas", "New Year", "Valentine's Day", "Sports", "Tours"]
    elif mode == "Administrator":
        event_names = ["Holi", "Diwali", "Christmas", "New Year", "Sarswati puja", "Valentine's Day", "Sports", "Tours", "Dashain"]
    event_name_var.set(event_names[0])


def grad_date(event=None):
    selected_date = cal.get_date()
    selected_date = datetime.strptime(selected_date, "%m/%d/%y").strftime("%Y-%m-%d")
    event = events.get(selected_date, "No event scheduled")
    date_label.config(text="Selected Date is: " + selected_date + " and the event for today is: " + event)




root = Tk()
root.title("KASA - The Event Manager")
root.config(bg='#ADD8E6')
root.geometry("800x600")

frame = Frame(root, width=800, height=100, bg="white")
frame.place(x=0, y=0, relwidth=1)
frame.config(bg='#001F3F')
titleLabel = Label(frame, text="KASA- The Event Manager", font=('Jumhuria', 50,'bold'),fg='#FAFFFE',bg='#001F3F')
titleLabel.place(x=700, y=45, anchor='center')

root.minsize(400, 300)

Label1=Label(root,text=" Upcoming Event",fg="black",bg='#ADD8E6',font=("katibeh",20,"bold"))
Label1.place(x=50 ,y=150) 


try:
    image = Image.open('Holi.jpg')
    resized_image = image.resize((150, 150), Image.BILINEAR)
    img = ImageTk.PhotoImage(resized_image)
    
    label = Label(root, image=img)
    label.place(x=100, y=190)  
    
except FileNotFoundError:
    print("Image file not found.")
except Exception as e:
    print("An error occurred while loading the image:", e)
#

try:
    image1 = Image.open('kasa.png')
    resized_image1 = image1.resize((80, 80), Image.BILINEAR)
    img1 = ImageTk.PhotoImage(resized_image1)
    image_label1 = Label(frame, image=img1)
    image_label1.place(x=10, y=10)
except FileNotFoundError:
    print("Image file not found.")
except Exception as e:
    print("An error occurred while loading the image:", e)

try:
    image2 = Image.open('holi.jpg')
    resized_image2 = image2.resize((180, 180), Image.BILINEAR)
    img2 = ImageTk.PhotoImage(resized_image2)
except FileNotFoundError:
    print("Image file not found.")
except Exception as e:
    print("An error occurred while loading the image:", e)

try:
    image3 = Image.open('diwali.jpg')
    resized_image3 = image3.resize((180, 180), Image.BILINEAR)
    img3 = ImageTk.PhotoImage(resized_image3)
except FileNotFoundError:
    print("Image file not found.")
except Exception as e:
    print("An error occurred while loading the image:", e)

try:
    image4 = Image.open('cheistmas.jpg')
    resized_image4 = image4.resize((180, 180), Image.BILINEAR)
    img4 = ImageTk.PhotoImage(resized_image4)
except FileNotFoundError:
    print("Image file not found.")
except Exception as e:
    print("An error occurred while loading the image:", e)

try:
    image5 = Image.open('newyear.jpg')
    resized_image5 = image5.resize((180, 180), Image.BILINEAR)
    img5 = ImageTk.PhotoImage(resized_image5)
except FileNotFoundError:
    print("Image file not found.")
except Exception as e:
    print("An error occurred while loading the image:", e)

try:
    image6 = Image.open('sports.jpg')
    resized_image6 = image6.resize((180, 180), Image.BILINEAR)
    img6 = ImageTk.PhotoImage(resized_image6)
except FileNotFoundError:
    print("Image file not found.")
except Exception as e:
    print("An error occurred while loading the image:", e)

try:
    image7 = Image.open('valentine.jpg')
    resized_image7 = image7.resize((180, 180), Image.BILINEAR)
    img7 = ImageTk.PhotoImage(resized_image7)
except FileNotFoundError:
    print("Image file not found.")
except Exception as e:
    print("An error occurred while loading the image:", e)

try:
    image8 = Image.open('tour.jpg')
    resized_image8 = image8.resize((180, 180), Image.BILINEAR)
    img8 = ImageTk.PhotoImage(resized_image8)
except FileNotFoundError:
    print("Image file not found.")
except Exception as e:
    print("An error occurred while loading the image:", e)

try:
    image9 = Image.open('sarswatipuja.jpg')
    resized_image9 = image9.resize((180, 180), Image.BILINEAR)
    img9 = ImageTk.PhotoImage(resized_image9)
except FileNotFoundError:
    print("Image file not found.")
except Exception as e:
    print("An error occurred while loading the image:", e)

try:
    image10 = Image.open('dashain.jpg')
    resized_image10 = image10.resize((100, 100), Image.BILINEAR)
    img10 = ImageTk.PhotoImage(resized_image10)
except FileNotFoundError:
    print("Image file not found.")
except Exception as e:
    print("An error occurred while loading the image:", e)

event_text = Label(root, text=""" Holi, known as the festival of colors,
is a vibrant and joyous Hindu celebration
marking the arrival of spring,where people
come together to play with colored powders,
share festive treats, and revel in the spirit
of unity and renewal.""", bg='#ADD8E6', font=('JejuMyeongjo',15,'normal'))
event_text.place(x=30, y=350)
image_label_frame = Label(root, bg='#CDC5C5')
image_label_frame.place(x=620, y=170, width=700, height=400)

frame = Frame(root, width=550, height=75, bg="white")
frame.place(x=700, y=180)
frame.config(bg='#D9D9D9')

event_name_label = Label(frame, text="Event Name:", font=("Arial", 10),bg='#D9D9D9')
event_name_label.place(x=5, y=20, width=80, height=25)

mode_var = StringVar()
mode_var.set("Student")  # Default mode is Student

mode_label = Label(frame, text="Mode:", font=("Arial", 10), bg="#D9D9D9")
mode_label.place(x=200, y=20, width=80, height=25)

mode_menu = OptionMenu(frame, mode_var, "Student", "Administrator", command=change_mode)
mode_menu.place(x=280, y=20, width=100, height=25)

event_name_var = StringVar()
event_name_var.set("Holi")  # Default event name

event_names = ["Holi", "Diwali", "Christmas", "New Year", "Valentine's Day", "Sports", "Tours","sarswati puja"]
event_name_menu = OptionMenu(frame, event_name_var, *event_names)
event_name_menu.place(x=90, y=20, width=80, height=25)

event_date_label = Label(frame, text="Event Date:", font=("Arial", 10),bg='#D9D9D9')
event_date_label.place(x=200, y=20, width=80, height=25)

event_dates = ["14 Feb 2024", "4 Nov 2024", "25 Dec 2024", "1 Jan 2025", "1 Oct 2025", "3 Dec 2025", "7 May 2024"]
event_date_var = StringVar()
event_date_var.set(event_dates[0])

event_date_menu = OptionMenu(frame, event_date_var, *event_dates)
event_date_menu.place(x=280, y=20, width=95, height=25)

search_button = Button(frame, text="Search", font=("Arial", 10), command=update_image)
search_button.place(x=440, y=20, width=90, height=25)

# Create a button to show features
def show_features():
    # Create a new window to display features
    features_window = Toplevel(root)
    features_window.title("Features")
    features_window.geometry("175x175+1175+205")
    features_window.config(bg='#ADD8E6')

    # Add buttons for features
    upcoming_events_btn = Button(features_window, text="Upcoming Events")
    upcoming_events_btn.pack(pady=4, fill=X, expand=True)

    attendance_btn = Button(features_window, text="Attendance")
    attendance_btn.pack(pady=4, fill=X, expand=True)

    events_calendar_btn = Button(features_window, text="Events Calendar")
    events_calendar_btn.pack(pady=4, fill=X, expand=True)

    more_btn = Button(features_window, text="More")
    more_btn.pack(pady=4, fill=X, expand=True)

def toggle_menu():
    if features_button.winfo_viewable():
        features_button.pack_forget()
    else:
        features_button.place(x=10,y=2)

# Create a button to show features
features_button = Button(root, text="☰", command=show_features)
features_button.place(x=1300,y=105)

notification_button = Button(root, text="🔔")#command=show_features
notification_button.place(x=1270,y=105)

mid = Frame(root, width=600, height=400, bg="white")
mid.place(x=680, y=250)

name = Label(mid, text="Event Calendar", font=("Georgia", 20,'bold'), background="white", fg="black")
name.place(x=300, y=40, anchor=tk.CENTER)

events = {
    "2024-01-01": "New Year Event",
    "2024-02-14": "Valentine's Day",
    "2024-03-17": "Holi",
    "2024-04-01": "sports",
    "2024-05-05": "college program",
    "2024-07-04": "tihar",
    "2024-10-31": "Tour",
    "2024-12-25": "Christmas"
}

cal = Calendar(mid, selectmode='day', year=2024, month=1, day=1)
cal.bind("<<CalendarSelected>>", grad_date)
cal.place(x=300, y=160, anchor=tk.CENTER)

date_label = Label(mid, text="", font=("Helvetica", 12), wraplength=500, justify="center")
date_label.place(x=300, y=280, anchor=tk.CENTER)


def show_homepage():
    root = Tk()
root.mainloop()
