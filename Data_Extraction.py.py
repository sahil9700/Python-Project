from tkinter import *
import tkinter
import PyPDF2
from tkinter import filedialog
def select_PDF():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("pdf files","*.pdf"),("all files","*.*")))
    label_file_explorer.configure(text="File Opened: " + filename)
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    ls = []
    email = []
    numbers = []
    time = []
    date = []
    # List of 10 largest countries in the world
    Countries_Largest = ['Russia', 'Canada', 'United States', 'China', 'Brazil', 'Australia', 'India', 'Argentina',
                         'Kazakhstan', 'Algeria']
    # A dictionary to store the frequency of each country that occured in our pdf
    Country_Freq = {'Russia': 0, 'Canada': 0, 'United States': 0, 'China': 0, 'Brazil': 0, 'Australia': 0, 'India': 0,
                    'Argentina': 0, 'Kazakhstan': 0, 'Algeria': 0}
    print('The data is : ')

    # Function to check if the email address is valid or not
    def EmailId_Validity(word):
        if (word.find('@') >= 0):
            email.append(word)

    # Function to check if the phone number is valid or not
    def Number_Validity(word):
        if (word.isdigit() and len(word) == 10):
            numbers.append(word)

    # Function to check if the time is valid or not
    def Time_Validity(word):
        if (word.find(':') >= 0):
            ls = word.split(':')
            valid_time = True
            if (len(ls) != 3 and len(ls) != 2):
                valid_time = False
            else:
                for i in ls:
                    if (i.isdigit() == False):
                        valid_time = False
                        break
            if (valid_time == True):
                time.append(word)

    # Function to check if the date is valid or not
    def Date_Validity(word):
        if (word.find('/') >= 0):
            ls = word.split('/')
            valid_date = True
            if (len(ls) != 3):
                valid_date = False
            else:
                for i in ls:
                    if (i.isdigit() == False):
                        valid_date = False
                        break
                if (valid_date == True):
                    if (int(ls[0]) > 31 or int(ls[1]) > 12):
                        valid_date = False
            if (valid_date == True):
                date.append(word)

    # Function to extract data from a single page
    def Extract(pageObj):
        for line in pageObj.extractText().splitlines():
            line = line.strip()
            # print(line)
            for word in line.split():

                Number_Validity(word)
                EmailId_Validity(word)
                Time_Validity(word)
                Date_Validity(word)

                if word in Country_Freq:
                    Country_Freq[word] = Country_Freq[word] + 1

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
    print('Time are : ', time)
    print('______________________________')
    print('Date : ', date)
    print('______________________________')
    print(Country_Freq)
    pdfFileObj.close()
    print('\n\n')
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




