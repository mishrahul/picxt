# picxt v1.0.0

Picxt.exe is a standalone application to retrieve images (such as screenshots) which contain user-defined keyword, in any specific directory.


## Usage

User needs to select a directory inorder to search for the images. After the keyword is entered, the tool scans every image in the directory & checks
whether an image contains the keyword. If positive, the application returns a list of images containing the keyword in tabular form. 
This includes file name, file creation date, file extension and its size. Double-click the file-name to open an image. 
For more info refer help section inside the application.
Supported image formats: JPEG, PNG, TIFF, GIF & BMP.


## Screenshots

### Home screen 
![main-screen](https://github.com/mishrahul/picxt/assets/145216845/063e11d8-3bec-4be2-b4cf-3bd16c9d4e33)

### Dialog-box if matches found
![success-dialog-box](https://github.com/mishrahul/picxt/assets/145216845/367c21f0-7b5a-413e-a8d6-3797383cc159)

### Dialog-box if no matches found
![nosuccess-dialog-box](https://github.com/mishrahul/picxt/assets/145216845/703aab30-6a89-4be2-a474-3ad1b1dd1314)

### Results window
![results](https://github.com/mishrahul/picxt/assets/145216845/9ddd4f35-2fb3-4233-a3b5-a2a48081e5a5)

### Help section
![help-section](https://github.com/mishrahul/picxt/assets/145216845/28dfacfb-ca98-42fe-84f6-ad853b3c77fa)


## Requirements

Requires Windows 8.1+.
Make sure you have python 3.11.1 installed in your system. 


## Installation

This app requires no installation for itself. It can be used on-the-go. 
Note that opening app may take a few seconds due to temporary extraction of dependencies required at runtime.


## Technologies 

* Python 3.11.1
* PyTesseract based on Tesseract OCR 0.3.10
* Tkinter library for GUI


## Support
For bugs-reports, queries or feedback, please reach out at rahulmishra9692@gmail.com
