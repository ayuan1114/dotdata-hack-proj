import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from urllib.request import urlopen
from recipeapi import RecipeExtract

class RecipeApp:
    def __init__(self, app, ingredients: list, number=5):

        self.app = app
        self.app.title("Recipe Recommendation")

        self.recommendations_frame = ttk.Frame(app)
        self.recommendations_frame.grid(row=3, columnspan=2, padx=10, pady=5)

        self.extractor = RecipeExtract(ingredients, number=number)
        self.extractor.get()
        self.extractor.extract()
        self.display_recommendations() # call display

    def display_recommendations(self):

        recommendations = self.extractor.recipes
        # Clear previous recommendations
        for widget in self.recommendations_frame.winfo_children():
            widget.destroy()

        # Display new recommendations
        for i, recipe in enumerate(recommendations):
            recipe_frame = ttk.Frame(self.recommendations_frame, relief=tk.RAISED, borderwidth=2)
            recipe_frame.grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)

            # Load and display recipe image
            #recipe_image = Image.open(recipe["image"])
            #recipe_image = recipe_image.resize((100, 100), Image.ANTIALIAS)
            #recipe_image = ImageTk.PhotoImage(recipe_image)
            #recipe_image_label = ttk.Label(recipe_frame, image=recipe_image)
            #recipe_image_label.image = recipe_image
            #recipe_image_label.grid(row=0, column=0, rowspan=2, padx=5, pady=5)

            # Display recipe name
            recipe_name_label = ttk.Label(recipe_frame, text=recipe["name"])
            recipe_name_label.grid(row=0, column=1, padx=5, pady=5)

