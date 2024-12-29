GIF and WebP Image Cropper
==========================
Table of Contents
-----------------

    Overview
    Requirements
    Usage
    Example Output

Overview
------------
Crop GIF and WebP Images with Ease!
This Python script crops GIF and WebP images to 512x512 pixels and saves them to a specified output folder. Perfect for creating uniform images for your social media or website.
Requirements
------------
Make Sure You Have:

    Python 3.x installed on your system
    Pillow library installed (pip install Pillow)

Usage
-----
Step-by-Step Instructions:

    Clone the repository: git clone https://github.com/your-username/your-repo-name.git
    Install required libraries: pip install Pillow
    Create input folder: Create a folder named input_images and add your GIF and WebP images to it.
    Run the script: python crop_images.py
    Get your cropped images: The cropped images will be saved to the output folder (output_images).

Example Output
----------------
Before Cropping:
Image	Size
image1.gif	1024x768
image2.webp	640x480
After Cropping:
Image	Size
image1.gif	512x512
image2.webp	512x512
Note: The script will skip non-GIF and non-WebP images in the input folder.
