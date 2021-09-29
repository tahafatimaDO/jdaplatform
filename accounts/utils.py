from django.core.files import File
from pathlib import Path
from PIL import Image
from io import BytesIO

image_types = {
    "jpg": "JPEG",
    "JPG": "JPEG",
    "jpeg": "JPEG",
    "png": "PNG",
    "PNG": "PNG",
    "gif": "GIF",
    "GIF": "GIF",
    "tif": "TIFF",
    "tiff": "TIFF",
}


def image_resize(logo, width, height):
    # Open the image using Pillow
    img = Image.open(logo)
    # check if either the width or height is greater than the max
    if img.width > width or img.height > height:
        output_size = (width, height)
        # Create a new resized “thumbnail” version of the image with Pillow
        img.thumbnail(output_size)
        # Find the file name of the image
        img_filename = Path(logo.file.name).name
        # Spilt the filename on “.” to get the file extension only
        img_suffix = Path(logo.file.name).name.split(".")[-1]
        # Use the file extension to determine the file type from the image_types dictionary
        img_format = image_types[img_suffix]
        # Save the resized image into the buffer, noting the correct file type
        buffer = BytesIO()
        img.save(buffer, format=img_format)
        # Wrap the buffer in File object
        file_object = File(buffer)
        # Save the new resized file as usual, which will save to S3 using django-storages
        logo.save(img_filename, file_object)