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










    def Split(self):

        # When user click on Split then the layout is change
        self.merge_btt.destroy()
        self.split_btt.destroy()











if __name__ == "__main__":
    pdf = PDF()
    pdf.Start_design()