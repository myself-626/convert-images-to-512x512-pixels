```markdown
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
  ```

---

## Usage

### Step-by-Step Instructions:
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```
2. **Install Required Libraries**  
   ```bash
   pip install Pillow
   ```
3. **Prepare Your Input Folder**  
   Create a folder named `input_images` in the project directory and add your images to it.
4. **Run the Script**  
   ```bash
   python image_cropper.py
   ```
5. **Specify the Crop Size**  
   When prompted, enter the desired crop size (e.g., `512 512`).
6. **Get Your Cropped Images**  
   The cropped images will be saved to the `output_images` folder.

---

## Example Output

### Before Cropping:
| Image       | Size      |
|-------------|-----------|
| image1.jpg  | 1024x768  |
| image2.png  | 640x480   |

### After Cropping:
| Image       | Size      |
|-------------|-----------|
| image1.jpg  | 512x512   |
| image2.png  | 512x512   |

### Note:
- The script will crop all images in the input folder to the specified size.
- Images smaller than the crop size will be padded with black.

---

## License
MIT License

Copyright (c) 2024 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy  
of this software and associated documentation files (the "Software"), to deal  
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all  
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  
SOFTWARE.

```
