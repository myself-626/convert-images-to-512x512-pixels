GIF and WebP Image Cropper
Table of Contents

    Overview
    Requirements
    Usage
    Example Output

Overview
This Python script crops GIF and WebP images to 512x512 pixels and saves them to a specified output folder.
Requirements

    Python 3.x
    Pillow library (pip install Pillow)

Usage

    Clone the repository: git clone https://github.com/your-username/your-repo-name.git
    Install the required libraries: pip install Pillow
    Create an input folder (input_images) and add your GIF and WebP images to it.
    Run the script: python crop_images.py
    The cropped images will be saved to the output folder (output_images).

Example Output
Before Cropping
Image	Size
image1.gif	1024x768
image2.webp	640x480
After Cropping
Image	Size
image1.gif	512x512
image2.webp	512x512
Note: The script will skip non-GIF and non-WebP images in the input folder.
