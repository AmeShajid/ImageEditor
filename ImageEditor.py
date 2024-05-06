#we can edit our pictures using this instead of photoshop lol

#first pipinstall pillow

#import pillow and os
#from pillow import those three things right there

# Import necessary libraries
import os  # For interacting with the operating system
from PIL import Image, ImageFilter, ImageEnhance  # For image processing


#DONT FORGET TO MAKE A FOLDER WITH THE IMAGES YOU WANT TO EDIT AND PUT THE PATH IN THE INPUT_PATH VARIABLE

# Define input and output paths for images
input_path = "./imgs"  # Path to the directory containing original images
output_path = "./editedImgs"  # Path to the directory where edited images will be saved

# Create output directory if it doesn't exist
if not os.path.exists(output_path):
    os.makedirs(output_path)  # Create the output directory if it doesn't exist

# Process each image in the input directory
for filename in os.listdir(input_path):
    # Form the full path to the input image
    img_path = os.path.join(input_path, filename)
    
    # Open the image using PIL
    img = Image.open(img_path)


#HERE IS THE MAIN PART OF THE CODE WHERE YOU EDIT THE CODE YOU CAN MAKE IT WHATEVER YOU WANT
    # Apply image processing: Sharpen, convert to grayscale.
    edited_img = img.filter(ImageFilter.SHARPEN).convert("L")

    # Extract filename without extension
    clean_name = os.path.splitext(filename)[0]

    # Determine the output filename and path
    output_filename = f'{clean_name}_edited.{img.format.lower()}'
    output_img_path = os.path.join(output_path, output_filename)

    # Save the edited image with the same format as the original
    edited_img.save(output_img_path)

    # Print status messages
    print(f"Processed: {filename}")  # Print the name of the processed image
    print("Successfully saved edited image.")  # Print a success message




