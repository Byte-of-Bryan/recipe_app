import os
import random
import tkinter as tk
from PIL import Image, ImageTk

WINDOW_TITLE = "My Recipes"
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 1000
IMG_WIDTH = 400
IMG_HEIGHT = 900
PINK_COLOR_HEX = '#ed9c87'

# store all the recipies into a file we can access
ALL_RECIPES = [str('recipes/') + file for file in os.listdir("recipes/")
               if not file.startswith('.')]


class RecipeApp:
    def __init__(self, root):
        self.root = root

        # show recipe image in the window
        self.recipe_images = ALL_RECIPES

        # save single recipe
        self.recipe_image_path = self.recipe_images[0]

        # create and add recipe image into frame
        self.recipe_frame = tk.Frame(self.root, bg=PINK_COLOR_HEX)
        self.recipe_image_label = self.create_photo(
            self.recipe_image_path, self.recipe_frame)

        # add it to pack
        self.recipe_image_label.pack(side=tk.TOP)

        # create background
        self.create_background()

    def create_background(self):

        # add title to window and change the size
        self.root.title(WINDOW_TITLE)
        self.root.geometry('{0}x{1}'.format(WINDOW_WIDTH, WINDOW_HEIGHT))

        # add all buttons
        self.create_buttons()

        # add recipes
        self.recipe_frame.pack(fill=tk.BOTH, expand=tk.YES)

    def create_buttons(self):
        pick_recipe_button = tk.Button(
            self.recipe_frame, text="PICK RECIPE", command=self.pick_recipe)
        pick_recipe_button.pack(side=tk.LEFT)

        recipe_prev_button = tk.Button(
            self.recipe_frame, text="Prev", command=self.get_next_recipe)
        recipe_prev_button.pack(side=tk.LEFT)

        recipe_next_button = tk.Button(
            self.recipe_frame, text="Next", command=self.get_prev_recipe)
        recipe_next_button.pack(side=tk.LEFT)

    # general function that will allow us to move front and back

    def _get_next_item(self, current_item, category, increment=True):

        # if we know where the current item index is in a category, then we find the pic before/after it
        item_index = category.index(current_item)
        final_index = len(category) - 1
        next_index = 0

        # edge cases
        if increment and item_index == final_index:
            # add the end, and need to go back to beginning
            next_index = 0
        elif not increment and item_index == 0:
            # go back to the end
            next_index = final_index
        else:
            # regular up and down
            # based on increment
            increment = 1 if increment else -1
            next_index = item_index + increment
        next_image = category[next_index]

        # reset and update the image based in next_image path
        if current_item in self.recipe_images:
            image_label = self.recipe_image_label
            self.recipe_image_path = next_image

        # use update function to change the image
        self.update_image(next_image, image_label)

    def get_next_recipe(self):
        self._get_next_item(self.recipe_image_path, self.recipe_images)

    def get_prev_recipe(self):
        self._get_next_item(self.recipe_image_path,
                            self.recipe_images, increment=False)

    def update_image(self, new_image_path, image_label):
        image_file = Image.open(new_image_path)
        image_resized = image_file.resize(
            (IMG_WIDTH, IMG_HEIGHT), Image.ANTIALIAS)
        tk_photo = ImageTk.PhotoImage(image_resized)

        # update based on provided image label
        image_label.configure(image=tk_photo)

        image_label.image = tk_photo

    def create_photo(self, image_path, frame):
        image_file = Image.open(image_path)
        image_resized = image_file.resize(
            (IMG_WIDTH, IMG_HEIGHT), Image.ANTIALIAS)
        tk_photo = ImageTk.PhotoImage(image_resized)
        image_label = tk.Label(frame, image=tk_photo, anchor=tk.CENTER)
        image_label.image = tk_photo

        # so we can add later
        return image_label

    def pick_recipe(self):

        # rand select a recipe index
        new_recipe_index = random.randint(0, len(self.recipe_images)-1)

        # add recipes onto the screen
        self.update_image(
            self.recipe_images[new_recipe_index], self.recipe_image_label)


root = tk.Tk()
app = RecipeApp(root)
root.mainloop()
