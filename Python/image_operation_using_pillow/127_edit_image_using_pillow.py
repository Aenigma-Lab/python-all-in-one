# installation of pillow library
# change the image extension
# resize image files.
# resize multiple images using for loop
# sharpness
# brightness
# color
# contrast
# Image blur, GaussianBlur

# Changing image extension......
from PIL import Image
from PIL import Image, ImageFilter
img = Image.open('nature.jpg')
# img.save('nature.png') #save file in diffrent format
# img.save('download.pdf')
# img.show() # view file 

# RESIZE THE IMAGE----

# try:
#     img = Image.open('nature.jpg')  # Replace with a valid image
#     img.thumbnail((250, 250))
#     img.save('resized_image.jpg')
#     print("Image processed successfully.")
# except Exception as e:
#     print(f"Error processing image: {e}")

# MULTIPLE IMAGE RESIZE
# for item in os.listdir():
#     if item.endswith('.jpg'):
#         img1 = Image.open(item)
#         filename,extension = os.path.splittext(item)
#         img1.save(f'{filename}.png')


#IMAGE SHARPNESSS
from PIL import Image, ImageEnhance
img2 = Image.open('nature.jpg')
# enhancer = ImageEnhance.Sharpness(img2)# this will make object for sharpness
color = ImageEnhance.Color(img2)
# enhancer.enhance(5).save('nature_sharp.jpg')
color.enhance(0).save('nature_color.jpg')# this 0 will make black and white image and increase number will change color
brightness = ImageEnhance.Brightness(img2)
brightness.enhance(3).save('nature_brightness.jpg')

# 0--> blurry 
# 1---> original Image
# 2---> image with increased shapness
# 3---> more increase sharpness continue with 4 ,5 till n
img2.filter(ImageFilter.GaussianBlur(radius=4)).save('nature_GaussianBlur.jpg')