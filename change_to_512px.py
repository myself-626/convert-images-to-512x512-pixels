from PIL import Image
import os

# Specify the input and output folders
input_folder = 'input_images'
output_folder = 'output_images'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate over all files in the input folder
for filename in os.listdir(input_folder):
    # Check if the file is a GIF or WebP image
    if filename.lower().endswith(('.gif', '.webp')):
        # Open the image
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Crop the image to 512x512 pixels
        width, height = img.size
        left = (width - 512) // 2
        top = (height - 512) // 2
        right = (width + 512) // 2
        bottom = (height + 512) // 2

        # If the image is smaller than 512x512, pad it with black color
        if width < 512 or height < 512:
            new_img = Image.new('RGBA', (512, 512), (0, 0, 0))
            new_img.paste(img, ((512 - width) // 2, (512 - height) // 2))
            img = new_img
        else:
            img = img.crop((left, top, right, bottom))

        # Save the cropped image to the output folder
        output_path = os.path.join(output_folder, filename)
        img.save(output_path)

        print(f'Cropped and saved {filename}')
    else:
        print(f'Skipped {filename} (not a GIF or WebP image)')