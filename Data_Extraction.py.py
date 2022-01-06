from tkinter import *
import tkinter
import PyPDF2
from tkinter import filedialog
def select_PDF():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("pdf files","*.pdf"),("all files","*.*")))
    label_file_explorer.configure(text="File Opened: " + filename)
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    ls=[]
    email = []
    numbers = []
    name = []
    age= []
    print('The data is : ')

    # Function to check if the email address is valid or not
    def EmailId_Validity(word):
        if (word.find('EmailId')>= 0):
            ls=word.split(':')
            email.append(ls[1])

    # Function to check if the phone number is valid or not
    def Number_Validity(word):
        if (word.find('PhoneNumber') >= 0):
            ls=word.split(':')
            numbers.append(ls[1])

    # Function to check if the time is valid or not
    def Name_Validity(word):
        if (word.find('Name') >= 0):
            ls= word.split(':')
            name.append(ls[1])

    # Function to check if the date is valid or not
    def Age_Validity(word):
        if (word.find('Age') >= 0):
            ls= word.split(':')
            age.append(ls[1])

    # Function to extract data from a single page
    def Extract(pageObj):
        for line in pageObj.extractText().splitlines():
            line = line.strip()
            #print(line)
            for word in line.split():

                Number_Validity(word)
                EmailId_Validity(word)
                Name_Validity(word)
                Age_Validity(word)

    # Function to iterate over each page for data extraction in pdf
    for i in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(i)
        Extract(pageObj)
    print('______________________________')

    # printing all the information we searched for
    print('Email IDs are ', email)
    print('______________________________')
    print('Phone number are', numbers)
    print('______________________________')
    print('Names are : ', name)
    print('______________________________')
    print('Age : ', age)
    print('______________________________')
    pdfFileObj.close()
    print('\n')
    print('******THANK YOU*******')


window = Tk()
window.title('Select a PDF')
window.geometry("500x500")
window.config(background="white")
label_file_explorer = Label(window,
                            text="Select PDF",
                            width=100, height=4,
                            fg="blue")
button_explore = Button(window,
                        text="Choose a File",
                        command= select_PDF)

button_exit = Button(window,
                     text="Exit",
                     command=exit)

label_file_explorer.grid(column=1, row=1)

button_explore.grid(column=1, row=2)

button_exit.grid(column=1, row=3)
window.mainloop()




