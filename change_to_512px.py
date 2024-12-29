from PIL import Image
import os

def crop_images(input_folder, output_folder, crop_size):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        # Open the image
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Crop the image to the desired size
        width, height = img.size
        left = (width - crop_size[0]) // 2
        top = (height - crop_size[1]) // 2
        right = (width + crop_size[0]) // 2
        bottom = (height + crop_size[1]) // 2

        # If the image is smaller than the crop size, pad it with black color
        if width < crop_size[0] or height < crop_size[1]:
            new_img = Image.new('RGBA', crop_size, (0, 0, 0))
            new_img.paste(img, ((crop_size[0] - width) // 2, (crop_size[1] - height) // 2))
            img = new_img
        else:
            img = img.crop((left, top, right, bottom))

        # Save the cropped image to the output folder
        output_path = os.path.join(output_folder, filename)
        img.save(output_path)

        print(f"Cropped and saved {filename}")

# Specify the input and output folders
input_folder = 'input_images'
output_folder = 'output_images'

# Specify the crop size
crop_size = tuple(map(int, input("Enter the crop size (e.g., 512 512): ").split()))

# Crop the images
crop_images(input_folder, output_folder, crop_size)
