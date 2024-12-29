from PIL import Image
import os

def convert_images(input_folder, output_folder, output_format):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        # Open the image
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Convert the image to the desired format
        output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.{output_format.lower()}")
        img.save(output_path)

        print(f"Converted {filename} to {output_format}")

# Specify the input and output folders
input_folder = 'input_images'
output_folder = 'output_images'

# Specify the output format
output_format = input("Enter the output format (e.g., PNG, JPEG, GIF, BMP, TIFF): ")

# Convert the images
convert_images(input_folder, output_folder, output_format)
