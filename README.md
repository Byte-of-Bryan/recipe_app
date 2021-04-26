# recipe_app
Program written by Bryan Morandi - 2021

Created an app with Python, Tkinter and Pillow to store images of recipes.

Over the past few months I have accumulated a number of vegitarian/vegan recipes that I have found cut out from 
cooking magazines and the New York Times. I have stored these in a physical folder but have lost some of the recipes or 
have spilled something on the paper that ruins the recipe. 

I thought that a Python app that could store these images of the recipes could be a fun and simple project that
was actually useful for my cooking hobby. 

In this application I used Tkinter for my GUI, and used Pillow to import/resize the images of recipes to be displayed.
There are three interactive buttons, 'prev' and 'next' cycle through all the recipes and bring you back to the first index
if you reach the end and vice versa. The third button is 'PICK RECIPE' this button pick a random recipe from all the stored 
recipes, this is sort of like a "What should I cook for dinner tonight" button, thought it was a fun addition!

I just wanted this to store my recipes, but below are a few optimizations/additions that I could implement in the future:
  - Dropdown Button that has categoies "Pasta, Soup, Salad, Rice, Beans, Other" - when you choose a category the photos that 
    are tagged with that attribute are only shown.
  - Dropdown rating button, once I have cooked the recipe I can rate it and this infomation is saved.
  - Notes button, takes you to a text prompt to add any changes that I wanted to make to the recipe. 
