# picxt

Picxt is a standalone application to retrieve images (such as screenshots) which contain keyword of your choice, in any specific directory.
The app is based upon pytesseract which is a wrapper for Tesseract-OCR Engine. 

# Installation

This app requires no installation. It can be used on-the-go. Note that opening app may take a few seconds due to 
temporary extraction of dependencies required at runtime.

# Usage

User needs to select a directory inorder to search for the images. After the keyword is entered, the tool scans every image in the directory & checks
whether an image contains the keyword. If positive, the application returns a list of images containing the keyword in tabular form. 
Double-click the file-name to open an image.
