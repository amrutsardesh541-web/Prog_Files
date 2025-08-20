import openai
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Set your OpenAI API key
openai.api_key = "your_api_key_here"

def generate_image(prompt):
    """Generates an image using OpenAI's DALL·E."""
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    return response["data"][0]["url"]

def open_original_image():
    """Opens an original image chosen by the organizer."""
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", ".png;.jpg;*.jpeg")])
    if filepath:
        original_image = Image.open(filepath)
        original_image = original_image.resize((512, 512))
        original_photo = ImageTk.PhotoImage(original_image)
        original_label.config(image=original_photo)
        original_label.image = original_photo
        global original_img_path
        original_img_path = filepath  # Store original image path

def generate_and_display():
    """Generates an image from the user prompt and displays it."""
    prompt = prompt_entry.get()
    if not prompt:
        status_label.config(text="Enter a prompt first!", fg="red")
        return

    try:
        img_url = generate_image(prompt)
        response = requests.get(img_url)
        gen_image = Image.open(BytesIO(response.content))
        gen_image = gen_image.resize((512, 512))

        gen_photo = ImageTk.PhotoImage(gen_image)
        generated_label.config(image=gen_photo)
        generated_label.image = gen_photo
        status_label.config(text="Image Generated Successfully!", fg="green")

    except Exception as e:
        status_label.config(text=f"Error: {str(e)}", fg="red")

# GUI setup
root = tk.Tk()
root.title("Image Prompt Challenge")
root.geometry("1100x700")

tk.Label(root, text="Original Image (Seen by Demonstrator)").pack()
original_label = tk.Label(root)
original_label.pack()

tk.Button(root, text="Upload Original Image", command=open_original_image).pack()

tk.Label(root, text="Enter Prompt to Generate Image:").pack()
prompt_entry = tk.Entry(root, width=50)
prompt_entry.pack()

tk.Button(root, text="Generate Image", command=generate_and_display).pack()

tk.Label(root, text="Generated Image from Prompt").pack()
generated_label = tk.Label(root)
generated_label.pack()

status_label = tk.Label(root, text="", fg="blue")
status_label.pack()

root.mainloop()