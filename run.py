import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

from process import processing_img
import asyncio

class ImageSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Выбор изображения")
        self.root.geometry("300x210")

        self.caption_label = tk.Label(root, text="Выберите изображение и нажмите 'Разукрасить'", font=("Arial", 16))
        self.caption_label.pack()

        self.image_label = tk.Label(root)
        self.image_label.pack(padx=10, pady=10)

        self.img_path = "img\default.jpg"

        image = Image.open(self.img_path)
        self.width, self.height = 600, 500

        image = image.resize((self.height, self.width), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        self.image_label.configure(image=photo)
        self.image_label.image = photo
        self.root.geometry(f"{self.width}x{self.height + 250}")

        self.add_buttons()
    
    def add_buttons(self):
        select_button = tk.Button(self.root, text="Выбрать изображение", command=self.select_image)
        select_button.pack(side=tk.TOP, padx=15, pady=10)

        process_button = tk.Button(self.root, text="Разукрасить", command=self.process_image)
        process_button.pack(side=tk.TOP, padx=15, pady=10)

    def process_image(self):
        asyncio.run(self.processing())

    async def processing(self):
        await processing_img(self.img_path, self.width, self.height)
        # self.image_label.image = None
        # image = image.resize((0, 0), Image.LANCZOS)
        # self.root.geometry(f"300x200")

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Изображения", "*.jpg *.png")])
        self.img_path = file_path

        if file_path:
            image = Image.open(file_path)           
            self.width, self.height = image.size

            if self.width > 600 or self.height > 800:
                self.width, self.height = 600, 800

            image = image.resize((self.height, self.width), Image.LANCZOS)
            self.root.geometry(f"{self.width}x{self.height}")
            photo = ImageTk.PhotoImage(image)
            self.image_label.configure(image=photo)
            self.image_label.image = photo


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageSelectorApp(root)
    root.mainloop()
