from tkinter import *
from tkinter import filedialog
import pdfplumber
import json

def summarize_pdf(file_path):
    # Open the PDF file
    with pdfplumber.open(file_path) as pdf:
        # Initialize a string to store the summary
        summary = ""
        # Loop over each page in the PDF file
        for page in pdf.pages:
            # Get the page text
            page_text = page.extract_text()
            # Split the page text into sentences
            sentences = page_text.split(".")
            # Add the first sentence from each page to the summary
            if len(sentences) > 0:
                summary += sentences[0] + ". "
            # If we've reached 20 lines, stop summarizing
            if summary.count("\n") >= 20:
                break
    return summary

def browse_file():
    file_path = filedialog.askopenfilename()
    e1.delete(0, END)
    e1.insert(0, file_path)
    summary = summarize_pdf(file_path)
    summary_text.delete('1.0', END)
    summary_text.insert('1.0', summary)

master = Tk()
master.grid_columnconfigure(0, weight=1)
master.grid_columnconfigure(1, weight=1)
master.grid_columnconfigure(2, weight=1)

# Configure the rows to expand when the window is resized
master.grid_rowconfigure(0, weight=1)
master.grid_rowconfigure(1, weight=1)
master.grid_rowconfigure(2, weight=1)

# Create widgets and add them to the grid
label1 = Label(master, text="Label 1")
label2 = Label(master, text="Label 2")
label3 = Label(master, text="Label 3")

label1.grid(row=0, column=0, sticky="nsew")
label2.grid(row=0, column=1, sticky="nsew")
label3.grid(row=0, column=2, sticky="nsew")


Label(master, text='PDF File Path').grid(row=0)
e1 = Entry(master, width=50)
e1.insert(0, "")
e1.grid(row=0, column=1)

browse_button = Button(master, text="Browse", command=browse_file)
browse_button.grid(row=0, column=2)

summary_label = Label(master, text="Summary:")
summary_label.grid(row=2, column=0)

summary_text = Text(master, height=10)
summary_text.grid(row=2, column=1, columnspan=2)

master.mainloop()
