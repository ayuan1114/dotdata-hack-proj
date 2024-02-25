# Author: Felix Zhu, Aaron Yuan, Jacob Hung
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from urllib.request import urlopen
from recipeapi import RecipeExtract
from io import BytesIO
import requests

class RecipeApp:
    def __init__(self, app, ingredients: list, number=5):
        # create tkinter window and name it
        self.app = app
        self.app.title("Recipe Recommendation")

        self.recommendations_frame = ttk.Frame(app)
        self.recommendations_frame.grid(row=3, columnspan=2, padx=10, pady=5)

        # call api
        self.extractor = RecipeExtract(ingredients, number=number)
        self.extractor.get()
        self.extractor.extract()
        self.display_recommendations() # call display

        #scrollbar = tk.Scrollbar(app)
        #scrollbar.grid(row=3, column=1, sticky='E')

    def display_recommendations(self):

        func = []
        butt = []

        recommendations = self.extractor.recipes
        # Clear previous recommendations
        for widget in self.recommendations_frame.winfo_children():
            widget.destroy()

        # Display new recommendations
        for index, recipe in enumerate(recommendations):
            recipe_frame = ttk.Frame(self.recommendations_frame, relief=tk.RAISED, borderwidth=2)
            recipe_frame.grid(row=index, column=0, padx=10, pady=5, sticky=tk.W)

            # Display recipe name
            butt.append(
                ttk.Button(recipe_frame, text=recipe["name"] + " (" + str(recipe["numIngredients"]) + " ingredients)",
                           command=(lambda index=index: self.clicked(index))))
            butt[index].grid(row=index, column=0, padx=5, pady=5)

            # process photo from URL
            img_url = recipe["image"]
            response = requests.get(img_url)
            image = Image.open(BytesIO(response.content))
            image = image.resize((100, 100))
            photo = ImageTk.PhotoImage(image)
            image_label = ttk.Label(recipe_frame, image=photo)
            image_label.grid(row=index, column=1, padx=5, pady=5)
            image_label.image = photo

    def clicked(self, index: int):

        # clear screen when clicked to make room for new content
        for widget in self.recommendations_frame.winfo_children():
            widget.destroy()

        # back button
        back_frame = ttk.Frame(self.recommendations_frame, relief=tk.RAISED, borderwidth=2)
        back_frame.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        back_button = ttk.Button(back_frame, text="Back", command=self.display_recommendations)
        back_button.grid(row=0, column=0, padx=5, pady=5)

        recipe = self.extractor.recipes[index]
        for i, ing in enumerate(recipe["ingredients"]):
            ing_frame = ttk.Frame(self.recommendations_frame, relief=tk.RAISED, borderwidth=2)
            ing_frame.grid(row=i + 1, column=0, padx=10, pady=5, sticky=tk.W)

            # Display recipe name
            ing_name_label = ttk.Label(ing_frame, text=ing["info"])
            ing_name_label.grid(row=i + 1, column=0, padx=5, pady=5)

            # process photo from URL
            img_url = ing["image"]
            response = requests.get(img_url)
            image = Image.open(BytesIO(response.content))
            image = image.resize((50, 50))
            photo = ImageTk.PhotoImage(image)
            image_label = ttk.Label(ing_frame, image=photo)
            image_label.grid(row=index, column=1, padx=5, pady=5)
            image_label.image = photo

        # display instructions
        inst_frame = ttk.Frame(self.recommendations_frame, relief=tk.RAISED, borderwidth=2)
        inst_frame.grid(row=len(recipe["ingredients"]) + 1, column=0, padx=10, pady=5, sticky=tk.W)

        inst_button = ttk.Label(inst_frame, text=self.extractor.getInstructions(index=index), wraplength=950)
        inst_button.grid(row=len(recipe["ingredients"]) + 1, column=0, padx=5, pady=5)
