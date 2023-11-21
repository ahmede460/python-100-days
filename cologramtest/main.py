import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('C:/Users/Ahmed/Downloads/image.jpeg', 10)

list_of_colors = []

for color in colors:
    
    current_color = color.rgb
    red = current_color.r
    green  = current_color.g
    blue = current_color.b
    list_of_colors.append((red, green, blue))
    
print(list_of_colors)