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
        self.merge_btt.place(x=110, y=400)
        self.split_btt.place(x=600, y=400)







    def Merge(self):

        # When user click on Merge then the layout is change
        self.merge_btt.destroy()
        self.split_btt.destroy()
        self.welcome_lbl.destroy()

        self.file1_lbl = Label(self.root, text="Select File 1", font=(self.font, 25))
        self.file2_lbl = Label(self.root, text="Select File 2", font=(self.font, 25))
        self.file1_btt = Button(self.root, text="File 1", padx=30, pady=10)
        self.file2_btt = Button(self.root, text="File 2", padx=30, pady=10)
        self.output_file_lbl = Label(self.root, text="Save the output file, with the file ending", font=(self.font, 25))
        self.output_file_ety = Entry(self.root)
        self.merger_btt = Button(self.root, text="Merge", padx=100, pady=30, command=self.merge_func)


        self.file1_lbl.place(x=150, y=200)
        self.file2_lbl.place(x=800, y=200)
        self.file1_btt.place(x=167, y=240)
        self.file2_btt.place(x=813, y=240)
        self.output_file_lbl.place(x=340, y=300)
        self.output_file_ety.place(x=440, y=340)
        self.merger_btt.place(x=420, y=500)


    def merge_func(self):

        # Merge the files together and go back in home program




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
        self.split_file_btt = Button(self.root, text="File", padx=30, pady=10)
        self.output_split_lbl = Label(self.root, text="Select Output Location", font=(self.font, 30))
        self.output_split_btt = Button(self.root, text="Output", padx=30, pady=10)
        self.spliter_btt = Button(self.root, text="Split", padx=100, pady=30, command=self.split_func)


        self.split_file_lbl.place(x=440, y=150)
        self.split_file_btt.place(x=495, y=220)
        self.output_split_lbl.place(x=400, y=300)
        self.output_split_btt.place(x=485, y=370)
        self.spliter_btt.place(x=425, y=500)


    def split_func(self):

        # Split the file in each side and go back to home program





        # Delete all spliter labels and buttons and load the start layout of program
        self.split_file_lbl.destroy()
        self.split_file_btt.destroy()
        self.output_split_lbl.destroy()
        self.output_split_btt.destroy()
        self.spliter_btt.destroy()
        self.titel_lbl.destroy()

        self.Start_design()












if __name__ == "__main__":
    pdf = PDF()
    pdf.Start_design()