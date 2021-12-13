# PDF Split/Merge Program
#
# Produce starts in 2021 December
# Producer: Sik Cem



from PyPDF2 import *
from tkinter import *



class PDF():

    def __init__(self):

        # Design Frame of programm
        self.root = Tk()
        self.root.geometry("1080x720")
        self.root.minsize(width=1080, height=720)
        self.root.maxsize(width=1080, height=720)
        self.root.config(bg="white")
        self.font = "Apple Chancery"
        self.Start_design()


        self.root.mainloop()



    def Start_design(self):

        # Make the start page of the program
        self.titel_lbl = Label(self.root, text="PDF Merge/Split", font=(self.font, 50))
        self.titel_lbl.pack()

        self.merge_btt = Button(self.root, text="Merge", padx=150, pady=50, font=(self.font, 25), fg="black", command=self.Merge)
        self.split_btt = Button(self.root, text="Split", padx=150, pady=50, font=(self.font, 25), fg="black", command=self.Split)
        self.merge_btt.place(x=110, y=400)
        self.split_btt.place(x=600, y=400)



    def Merge(self):

        # When user click on Merge then the layout is change
        self.merge_btt.destroy()
        self.split_btt.destroy()

        self.file1_lbl = Label(self.root, text="Select File 1", font=(self.font, 25))
        self.file2_lbl = Label(self.root, text="Select File 2", font=(self.font, 25))
        self.file1_btt = Button(self.root, text="File 1", padx=30, pady=10)
        self.file2_btt = Button(self.root, text="File 2", padx=30, pady=10)
        self.output_file_lbl = Label(self.root, text="Save the output file, with the file ending", font=(self.font, 25))
        self.output_file_ety = Entry(self.root)
        self.merger_btt = Button(self.root, text="Merge", padx=50, pady=20)


        self.file1_lbl.place(x=150, y=200)
        self.file2_lbl.place(x=800, y=200)
        self.file1_btt.place(x=167, y=240)
        self.file2_btt.place(x=813, y=240)
        self.output_file_lbl.place(x=340, y=300)
        self.output_file_ety.place(x=430, y=340)
        self.merger_btt.place(x=452, y=420)









    def Split(self):

        # When user click on Split then the layout is change
        self.merge_btt.destroy()
        self.split_btt.destroy()

        









if __name__ == "__main__":
    pdf = PDF()
    pdf.Start_design()