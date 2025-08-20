import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Intelligent Travel Planning with Budget Optimization")

# Set the background image
background_image = tk.PhotoImage(file="background.png")  # Replace with the path to your image file
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Create a frame for the input fields
frame = tk.Frame(root, bg='white', bd=5)
frame.pack(padx=20, pady=20)

# From City dropdown
from_city_label = tk.Label(frame, text="From City")
from_city_label.grid(row=0, column=0)
from_city_option = ttk.Combobox(frame, values=["Mumbai","Delhi"])
from_city_option.grid(row=1, column=0)
from_city_option.set("Select Option")

# To City entry
to_city_label = tk.Label(frame, text="To City")
to_city_label.grid(row=0, column=1)
to_city_entry = tk.Entry(frame)
to_city_entry.grid(row=1, column=1)

# Departure Date entry
departure_date_label = tk.Label(frame, text="Departure Date")
departure_date_label.grid(row=0, column=2)
departure_date_entry = tk.Entry(frame)
departure_date_entry.grid(row=1, column=2)

# Guests entry
guests_label = tk.Label(frame, text="Guests")
guests_label.grid(row=0, column=4)
guests_entry = tk.Entry(frame)
guests_entry.grid(row=1, column=4)

# Radio button for flight search
flight_search_var = tk.BooleanVar()
flight_search_radio = tk.Radiobutton(frame, text="I'm looking for flights", variable=flight_search_var)
flight_search_radio.grid(row=2, columnspan=1)

# Submit button
submit_button = tk.Button(frame, text="Submit", bg='purple', fg='white')
submit_button.grid(row=5, columnspan=2)

# Run the application
root.mainloop()