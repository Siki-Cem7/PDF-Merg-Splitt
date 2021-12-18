# PDF Split/Merge Program
#
# Produce starts in 2021 December
# Producer: Sik Cem


import PyPDF2
from tkinter import *
from tkinter.filedialog import *
from PyPDF2 import *




class PDF():

    def __init__(self):

        # Design Frame of programm
        self.root = Tk()
        self.root.geometry("1080x720")
        self.root.minsize(width=1080, height=720)
        self.root.maxsize(width=1080, height=720)
        self.root.config(bg="white")
        self.font = "Apple Chancery"
        self.welcome_txt = """
        Welcome to PDF Merg/Split
        
        Down of the page you can choose your program you need.
        Producer: Siki Cem    
        """

        self.Start_design()


        self.root.mainloop()



    def Start_design(self):

        # Make the start page of the program
        self.titel_lbl = Label(self.root, text="PDF Merge/Split", font=(self.font, 50))
        self.welcome_lbl = Label(self.root, text=self.welcome_txt, font=(self.font, 30))

        self.titel_lbl.pack()
        self.welcome_lbl.pack()

        self.merge_btt = Button(self.root, text="Merge", padx=150, pady=50, font=(self.font, 25), fg="black", command=self.Merge)
        self.split_btt = Button(self.root, text="Split", padx=150, pady=50, font=(self.font, 25), fg="black", command=self.Split)
        self.home_btt = Button(self.root, text="Home", padx=60, pady=20, command=self.home)
        self.merge_btt.place(x=110, y=400)
        self.split_btt.place(x=600, y=400)
        self.home_btt.place(x=20, y=640)







    def Merge(self):

        # When user click on Merge then the layout is change
        self.merge_btt.destroy()
        self.split_btt.destroy()
        self.welcome_lbl.destroy()

        self.file1_lbl = Label(self.root, text="Select File 1", font=(self.font, 25))
        self.file2_lbl = Label(self.root, text="Select File 2", font=(self.font, 25))
        self.file1_btt = Button(self.root, text="File 1", padx=30, pady=20, command=self.search_merge_file1)
        self.file2_btt = Button(self.root, text="File 2", padx=30, pady=20, command=self.search_merge_file2)
        self.output_file_lbl = Label(self.root, text="Give a output file name, with the file ending", font=(self.font, 25))
        self.output_file_ety = Entry(self.root)
        self.merger_btt = Button(self.root, text="Merge", padx=100, pady=30, command=self.merge_func)


        self.file1_lbl.place(x=180, y=200)
        self.file2_lbl.place(x=820, y=200)
        self.file1_btt.place(x=197, y=240)
        self.file2_btt.place(x=833, y=240)
        self.output_file_lbl.place(x=340, y=300)
        self.output_file_ety.place(x=440, y=340)
        self.merger_btt.place(x=420, y=500)


    def merge_func(self):

        # Merge the files together and go back in home program
        self.PDF_merger = PdfFileMerger()
        self.PDF_merger.append(self.merge_file1)
        self.PDF_merger.append(self.merge_file2)

        # Take the Entry string from "self.output_file_ety" and save it
        self.merge_output_name = self.output_file_ety.get()
        print(self.merge_output_name)


        self.PDF_merger.write(f"{self.merge_output_name}")



        # Delete all Merge labels and buttons and load the start layout of program
        self.file1_lbl.destroy()
        self.file2_lbl.destroy()
        self.file1_btt.destroy()
        self.file2_btt.destroy()
        self.output_file_lbl.destroy()
        self.output_file_ety.destroy()
        self.merger_btt.destroy()
        self.titel_lbl.destroy()

        self.Start_design()










    def Split(self):

        # When user click on Split then the layout is change
        self.merge_btt.destroy()
        self.split_btt.destroy()
        self.welcome_lbl.destroy()

        self.split_file_lbl = Label(self.root, text="Select your File", font=(self.font, 30))
        self.split_file_btt = Button(self.root, text="File", padx=40, pady=20, command=self.search_split_file)
        self.output_split_lbl = Label(self.root, text="Select Output Location", font=(self.font, 30))
        self.output_split_btt = Button(self.root, text="Output", padx=40, pady=20, command=self.selcet_output)
        self.spliter_btt = Button(self.root, text="Split", padx=100, pady=30, command=self.split_func)


        self.split_file_lbl.place(x=440, y=150)
        self.split_file_btt.place(x=495, y=220)
        self.output_split_lbl.place(x=400, y=300)
        self.output_split_btt.place(x=485, y=370)
        self.spliter_btt.place(x=435, y=500)


    def split_func(self):

        # Split the file in each side and go back to home program
        with open(str(self.split_file.name), "rb") as file:
            self.PDF = PyPDF2.PdfFileReader(file)
            self.pages = self.PDF.getNumPages()

            for page in range(self.PDF.getNumPages()):
                self.file_writer = PyPDF2.PdfFileWriter()

                self.file_writer.addPage(self.PDF.getPage(page))
                with open(f"{self.split_output_dir}/{int(page) + 1}.pdf", "wb") as file_write:
                   self.file_writer.write(file_write)





        # Delete all spliter labels and buttons and load the start layout of program
        self.split_file_lbl.destroy()
        self.split_file_btt.destroy()
        self.output_split_lbl.destroy()
        self.output_split_btt.destroy()
        self.spliter_btt.destroy()
        self.titel_lbl.destroy()

        self.Start_design()



    def selcet_output(self):

        # The user is going to choose a output location for the splited files
        self.split_output_dir = askdirectory(parent=self.root, title="Select Location to save your splited Files")
        self.output_split_btt.config(padx=30, text="Checked")
        self.output_split_btt.place(x=490, y=370)




    def search_split_file(self):

        # To choose the file, which the user will split
        self.split_file = askopenfile(mode="rb", parent=self.root, title="Select your File", filetypes=[("PDF Files", "*.pdf")])
        self.split_file_btt.config(text="Checked", padx=20)



    def search_merge_file1(self):

        # Search merge file 1
        self.merge_file1 = askopenfile(mode="rb", parent=self.root, title="Select your File", filetypes=[("PDF Files", "*.pdf")])
        self.file1_btt.config(text="Checked", padx=20)



    def search_merge_file2(self):

        # Search merge file 2
        self.merge_file2 = askopenfile(mode="rb", parent=self.root, title="Select your File", filetypes=[("PDF Files", "*.pdf")])
        self.file2_btt.config(text="Checked", padx=20)



    def home(self):

        # Go back to home. First i destroy all labels or button, then i start the Start the start layout
        try:
            self.titel_lbl.destroy()
            self.welcome_lbl.destroy()
            self.merge_btt.destroy()
            self.split_btt.destroy()
            self.home_btt.destroy()
        except:
            print("No")
        try:
            self.file1_lbl.destroy()
            self.file2_lbl.destroy()
            self.file1_btt.destroy()
            self.file2_btt.destroy()
            self.output_file_lbl.destroy()
            self.output_file_ety.destroy()
            self.merger_btt.destroy()
            self.titel_lbl.destroy()
        except:
            print("No")
        try:
            self.split_file_lbl.destroy()
            self.split_file_btt.destroy()
            self.output_split_lbl.destroy()
            self.output_split_btt.destroy()
            self.spliter_btt.destroy()
            self.titel_lbl.destroy()
        except:
            print("No")


        self.Start_design()








if __name__ == "__main__":
    pdf = PDF()
    pdf.Start_design()