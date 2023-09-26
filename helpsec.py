import tkinter as tk
from tkinter import ttk



def open_hs():
    hswindow = tk.Toplevel()
    hswindow.title("Picxt Help Section")
    hsw_bg = "#1E272E"
    hsw_fg = "#cccccc"
    hswindow.geometry("900x600")
    hswindow.minsize(width=530, height=400)

    
    style=ttk.Style()
    style.theme_use("classic")
    style.configure("Vertical.TScrollbar", background="#374754",  arrowcolor="gray", troughcolor="#455f73",borderwidth=0)
    style.map("Vertical.TScrollbar", background=[("active", "#5e8399")])


    hswindow["background"] = hsw_bg
    hdng="---------------Help Section: FAQs & Tips---------------"
    heading_lbl = tk.Label(hswindow, font=("Poppins bold", 24), text=hdng,
                foreground=hsw_fg, background="#151B21")
    heading_lbl.pack(ipady=20, fill="both")

    tqa = tk.Text(hswindow, height=100, width=100, bd=0, bg=hsw_bg, wrap="word")
    tqa.pack(side="left", fill="both", expand=True)

    

    tqa.tag_configure("th", font=("Poppins bold", 19), foreground=hsw_fg, background=hsw_bg, justify="center")
    tqa.tag_configure("tq", font=("Poppins semibold", 16), lmargin1=20, foreground=hsw_fg, background=hsw_bg)
    tqa.tag_configure("ta", font=("Poppins", 13), lmargin1=20, foreground=hsw_fg, background=hsw_bg)
    tqa.tag_add("ta", "2.0", "end")

    #FAQs
    tqa.insert("insert", "FAQs\n", "th")
    tqa.insert("insert", "1. What does this app do?\n", "tq")
    tqa.insert("insert", "The app allows you to search for images that contain a specific text entered by you. It's useful for finding screenshots or images which contain the specified keyword. Before searching, you need to select a directory in your drive where the app will look for images, using SELECT DIRECTORY button.\n\n", "ta")

    tqa.insert("insert", "2. How to specify the keyword I want to search?\n", "tq")
    tqa.insert("insert", "You can enter a keyword of your choice in the text-box on the main screen. Keep in mind that the keyword entry is case sensitive. Mismatch of letter cases may not fetch desired results.\n\n", "ta")

    tqa.insert("insert", "3. How do I perform search for images? \n", "tq")
    tqa.insert("insert", "Make sure you have selected the target directory in which you want to search for images. A green-tick will appear once you have selected the directory. After entering the desired keyword you can click the SEARCH button to search for images that contain the keyword. This may take a while hence your patience is appreciated. \n\n", "ta")

    tqa.insert("insert", "4. What happens after the search is completed? \n", "tq")
    tqa.insert("insert", "Once the search has completed, a prompt is displayed on the screen showing the number of retrieved images containing your specified keyword. Click on YES to view all the results.\n\n", "ta")

    tqa.insert("insert", "5. How are the results displayed? \n", "tq")
    tqa.insert("insert", "The results are displayed in tabular form that includes columns for: File Name, Date of Creation, Extension, File Size. \n\n", "ta")

    tqa.insert("insert", "6. How can I view retrieved images in the results? \n", "tq")
    tqa.insert("insert", "You can view the retrieved images by double-clicking on the file name in results. The images will be displayed through your default image viewer application. \n\n", "ta")

    tqa.insert("insert", "7. How do I clear the search results? \n", "tq")
    tqa.insert("insert", "After performing a search, you can click on the CLEAR button to remove the entered keyword and start a new search. \n\n", "ta")

    # tqa.insert("insert", " \n", "tq")
    # tqa.insert("insert", " \n", "ta")

    tqa.insert("insert", "Tips for Effective Usage & Troubleshooting: \n", "th")

    tqa.insert("insert", "• To Improve Search Results:  \n", "tq")
    tqa.insert("insert", "To get accurate results, use specific keywords related to the content you're looking for in the images. Avoid multiple keywords, except if they occur subsequently in your expected images. Partial matches aren't supported. \n", "ta")

    tqa.insert("insert", "• No Results Found:  \n", "tq")
    tqa.insert("insert", "If you're not getting any results, double-check your keyword spelling and try case and other variations. If your images have very low resolution or are corrupted, it may also lead to incorrect results or failure to scan the images. \n", "ta")

    tqa.insert("insert", "• Slow Performance:  \n", "tq")
    tqa.insert("insert", "The application might perform slow if there are large number of images in your selected folder. Consider waiting for the result prompt to appear once the search has completed. \n", "ta")

    tqa.insert("insert", "• Supported Formats: \n", "tq")
    tqa.insert("insert", "The app only supports the following file formats: JPEG, PNG, TIFF, GIF & BMP. Make sure the images you're searching for are in supported formats. \n\n", "ta")

    tqa.insert("insert", "CONTACT SUPPORT: \n", "th")
    tqa.insert("insert", "If you encounter any issues, have questions, or need further assistance, please feel free to contact at support@example.com. Thank you for using Picxt. We hope you have a great experience searching for images efficiently and effectively. \n", "ta")

    

    tqa_scrollbar = ttk.Scrollbar(hswindow, command=tqa.yview)
    tqa_scrollbar.pack(side="right", fill="y")

    tqa.config(yscrollcommand=tqa_scrollbar.set)

    hswindow.mainloop()

#open_hs()