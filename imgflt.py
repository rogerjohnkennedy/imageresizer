from PIL import Image, ImageTk
import os
import tkinter as tk
from tkinter import filedialog

def resize_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)

        # Calculate target dimensions to achieve the desired file size
        target_size_bytes = target_file_size_kb.get() * 1024
        original_size_bytes = os.path.getsize(file_path)
        resize_factor = (target_size_bytes / original_size_bytes) ** 0.5
        new_width = int(image.width * resize_factor)
        new_height = int(image.height * resize_factor)

        # Resize the image
        resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)

        # Save the resized image in the location of this py file
        output_path = os.path.join(os.path.dirname(file_path), 'resized_image.jpg')
        # Adjust the quality based on your needed
        resized_image.save(output_path, quality=85)

        # Update the result label
        result_label.config(text=f"Image resized and saved as 'resized_image.jpg'.")

        # Display the resized image
        resized_image.thumbnail((300, 300))  # Limit the size for display
        resized_tk_image = ImageTk.PhotoImage(resized_image)
        image_label.config(image=resized_tk_image)
        image_label.image = resized_tk_image



# Create a Tkinter window
root = tk.Tk()
root.title("Image Resizing")

# Add custom styling based on your color taste on every hex color
root.configure(bg="#F0F0F0")

# Create a frame for the main content
main_frame = tk.Frame(root, bg="#F0F0F0")
main_frame.pack(padx=200, pady=20)

# Create a label for the title
title_label = tk.Label(main_frame, text="Max Size of Image in (KB)", font=("Helvetica", 16, "bold"), bg="#F0F0F0")
title_label.pack(pady=10)

# Create an entry for target file size
target_file_size_kb = tk.IntVar()
target_file_size_entry = tk.Entry(main_frame, textvariable=target_file_size_kb, font=("Helvetica", 12))
# Default size 400 kb, we can change in GIU as well
target_file_size_kb.set(400)
target_file_size_entry.pack(pady=10)

# Create a button to select and resize the image
resize_button = tk.Button(main_frame, text="Resize Image", command=resize_image, font=("Helvetica", 12), bg="#4CAF50", fg="white")
resize_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(main_frame, text="", font=("Helvetica", 12), bg="#F0F0F0")
result_label.pack()

# Create a label to display the resized image
image_label = tk.Label(main_frame)
image_label.pack()



# Run the Tkinter event loop
root.mainloop()
