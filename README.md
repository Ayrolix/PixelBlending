# Pixel Blending
This project kinda/sorta came about on accident while messing with recoloring pixels of a pre-existing image but essentially, what it does, is selects a pixel, gets the surrounding (top, left, right, and bottom) pixels and adds all their values together (as long as no positional values are negative and/or the transparency value is 0) and gets the average of them all, assigning the source pixel to the new average value.
