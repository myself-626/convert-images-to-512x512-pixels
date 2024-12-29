Enhanced README

# Image Cropper

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Usage](#usage)
- [Example Output](#example-output)

---

## Overview

Crop images effortlessly with this Python script!  
Specify the input and output folders, define the desired crop size, and let the script handle the rest.

---

## Requirements

Make sure you have the following installed:
- **Python 3.x**
- **Pillow library**  
  Install it via pip:  
  ```bash
  pip install Pillow

Usage
Step-by-Step Instructions:

    Clone the Repository

git clone https://github.com/your-username/your-repo-name.git

Install Required Libraries

pip install Pillow

Prepare Your Input Folder
Create a folder named input_images in the project directory and add your images to it.
Run the Script

    python image_cropper.py

    Specify the Crop Size
    When prompted, enter the desired crop size (e.g., 512 512).
    Get Your Cropped Images
    The cropped images will be saved to the output_images folder.

Example Output
Before Cropping:
Image	Size
image1.jpg	1024x768
image2.png	640x480
After Cropping:
Image	Size
image1.jpg	512x512
image2.png	512x512
Note:

    The script will crop all images in the input folder to the specified size.
    Images smaller than the crop size will be padded with black.
