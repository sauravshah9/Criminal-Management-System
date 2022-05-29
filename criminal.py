from logging import root
from msilib.schema import tables
from re import I
from tkinter import*
from tkinter import ttk
from tkinter.tix import Select
from PIL import Image,ImageTk



class Criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1920x1080+0+0')
        self.root.title('CRIMINAL MANAGEMENT SYSTEM')
        
        lbl_title=Label(self.root,text='CRIMINAL MANAGEMENT SYSTEM SOFTWARE',font =('times new roman', 30, 'bold'), bg="black", fg="gold")
        lbl_title.place(x=0,y=0, width=1300, height=40)
        
        #ncr logo
        img_logo =Image.open('images/ncrlogo.jpg')
        img_logo=img_logo.resize((40,40), Image.ANTIALIAS)
        self.photo_logo =ImageTk.PhotoImage(img_logo)
        
        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=70, y=3, height=40, width=40)
    
        #Imf Frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=40, width=1080, height=90)
    

        #1st Image
        img1 =Image.open('images/police1.jpg')
        img1=img1.resize((440,110), Image.ANTIALIAS)
        self.photo1 =ImageTk.PhotoImage(img1)
        
        self.img1=Label(img_frame,image=self.photo1)
        self.img1.place(x=0, y=0, height=110, width=440)
    
        #2nd Image
        img2 =Image.open('images/police2.jpg')
        img2=img2.resize((440,110), Image.ANTIALIAS)
        self.photo2 =ImageTk.PhotoImage(img2)
        
        self.img2=Label(img_frame,image=self.photo2)
        self.img2.place(x=360, y=0, height=110, width=440)
        
        #3rd Image
        img3 =Image.open('images/police3.jpg')
        img3=img3.resize((440,110), Image.ANTIALIAS)
        self.photo3 =ImageTk.PhotoImage(img3)
        
        self.img3=Label(img_frame,image=self.photo3)
        self.img3.place(x=720, y=0, height=110, width=440)
    
    
        #Main Frame
        Main_frame =Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=0,y=130, width=1760,height=550)
       
       #upper frame
        upper_frame =LabelFrame(Main_frame,bd=2,relief=RIDGE, text='Criminal Information',font =('times new roman', 10, 'bold'), fg="red", bg="white")
        upper_frame.place(x=7,y=5, width=1600,height=350)

        #Labels and Entry
        
        
        #case id
        caseid = Label(upper_frame, text ='Case ID:',font =('arial', 11, 'bold'), bg="white") 
        caseid.grid(row=0,column=0,padx=2,sticky=W)

        caseentry=ttk.Entry(upper_frame,width=20,font =('arial', 11, 'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)

        #Criminal No
        lbl_criminal_no =Label(upper_frame,text='Criminal NO:',font =('arial', 12, 'bold'), fg="red", bg="white")
        lbl_criminal_no.grid(row=0,column=2,padx=2,pady=7,sticky=W)

        txt_criminal_no =ttk.Entry(upper_frame,width=22,font=("arial", 11, "bold"))
        txt_criminal_no.grid(row=0,column=3,padx=2,pady=7)

        #Criminal Name
        lbl_Name =Label(upper_frame,text='Criminal Name:',font =('arial', 11, 'bold'), fg="red", bg="white")
        lbl_Name.grid(row=1,column=0,padx=2,pady=7,sticky=W)

        txt_Name =ttk.Entry(upper_frame,width=22,font=("arial", 11, "bold"))
        txt_Name.grid(row=1,column=1,padx=2,pady=7)
        
        #Nickname
        lbl_nickname =Label(upper_frame,text='NickName:',font =('arial', 11, 'bold'), fg="red", bg="white")
        lbl_nickname.grid(row=1,column=2,padx=2,pady=7,sticky=W)

        txt_nickname =ttk.Entry(upper_frame,width=22,font=("arial", 11, "bold"))
        txt_nickname.grid(row=1,column=3,padx=2,pady=7)
        
        #Arrest Date
        lbl_arrestDate =Label(upper_frame,text='Arrest Date:',font =('arial', 11, 'bold'), fg="red", bg="white")
        lbl_arrestDate.grid(row=2,column=0,padx=2,pady=7,sticky=W)

        txt_arrestDate =ttk.Entry(upper_frame,width=22,font=("arial", 11, "bold"))
        txt_arrestDate.grid(row=2,column=1,padx=2,pady=7)
        
        #Date of Crime
        lbl_dateOfCrime =Label(upper_frame,text='Date of Crime:',font =('arial', 11, 'bold'), fg="red", bg="white")
        lbl_dateOfCrime.grid(row=2,column=2,padx=2,pady=7,sticky=W)

        txt_dateOfCrime =ttk.Entry(upper_frame,width=22,font=("arial", 11, "bold"))
        txt_dateOfCrime.grid(row=2,column=3,padx=2,pady=7)
        
        
        #Address
        lbl_address =Label(upper_frame,text='Address:',font =('arial', 11, 'bold'), fg="red", bg="white")
        lbl_address.grid(row=3,column=0,padx=2,pady=7,sticky=W)

        txt_address =ttk.Entry(upper_frame,width=22,font=("arial", 11, "bold"))
        txt_address.grid(row=3,column=1,padx=2,pady=7)
        
        #Age
        lbl_age=Label(upper_frame,text='Age:',font =('arial', 11, 'bold'), fg="red", bg="white")
        lbl_age.grid(row=3,column=2,padx=2,pady=7,sticky=W)

        txt_age =ttk.Entry(upper_frame,width=22,font=("arial", 11, "bold"))
        txt_age.grid(row=3,column=3,padx=2,pady=7)
        
        
        #Occupation
        lbl_occupation=Label(upper_frame,text='Occupation:',font =('arial', 11, 'bold'), fg="red", bg="white")
        lbl_occupation.grid(row=4,column=0,padx=2,pady=7,sticky=W)

        txt_occupation=ttk.Entry(upper_frame,width=22,font=("arial", 11, "bold"))
        txt_occupation.grid(row=4,column=1,padx=2,pady=7)
        
        #birthmark
        lbl_birthMark=Label(upper_frame,text='Birth Mark:',font =('arial', 11, 'bold'), fg="red", bg="white")
        lbl_birthMark.grid(row=4,column=2,padx=2,pady=7,sticky=W)

        txt_birthMark=ttk.Entry(upper_frame,width=22,font=("arial", 11, "bold"))
        txt_birthMark.grid(row=4,column=3,padx=2,pady=7)
        
        #Crime Type
        lbl_crimeType=Label(upper_frame,text='Crime Type:',font =('arial', 11, 'bold'), fg="red", bg="white")
        lbl_crimeType.grid(row=0,column=4,padx=2,pady=7,sticky=W)

        txt_crimeType=ttk.Entry(upper_frame,width=22,font=("arial", 11, "bold"))
        txt_crimeType.grid(row=0,column=5,padx=2,pady=7)
        
        
        #Father Name
        lbl_fatherName=Label(upper_frame,text='Father Name:',font =('arial', 11, 'bold'), fg="red", bg="white")
        lbl_fatherName.grid(row=1,column=4,padx=2,pady=7,sticky=W)

        txt_fatherName=ttk.Entry(upper_frame,width=22,font=("arial", 11, "bold"))
        txt_fatherName.grid(row=1,column=5,padx=2,pady=7)
        
        #gender
        lbl_gender=Label(upper_frame,text='Gender:',font =('arial', 11, 'bold'), fg="red", bg="white")
        lbl_gender.grid(row=2,column=4,padx=2,pady=7,sticky=W)
        
        #wanted
        lbl_wanted=Label(upper_frame,text='Most Wanted:',font =('arial', 11, 'bold'), fg="red", bg="white")
        lbl_wanted.grid(row=3,column=4,padx=2,pady=7,sticky=W)
        
        #Radio Button gender
        radio_frame_gender=Frame(upper_frame,bd=2,relief=RIDGE, bg='white')
        radio_frame_gender.place(x=670,y=80,width=190,height=30)
        
        male=Radiobutton(radio_frame_gender,text='Male', value='male', font =('arial', 9, 'bold'), bg='white')
        male.grid(row=0,column=0, pady=2,padx=4,sticky=W)
        
        female=Radiobutton(radio_frame_gender,text='Female', value='female', font =('arial', 9, 'bold'), bg='white')
        female.grid(row=0,column=1, pady=2,padx=4,sticky=W)
        
        
    
        
        #Radio Button wanted
        radio_frame_wanted=Frame(upper_frame,bd=2,relief=RIDGE, bg='white')
        radio_frame_wanted.place(x=710,y=120,width=190,height=30)
        
        yes=Radiobutton(radio_frame_wanted,text='Yes', value='yes', font =('arial', 9, 'bold'), bg='white')
        yes.grid(row=0,column=0, pady=2,padx=4,sticky=W)
        
        no=Radiobutton(radio_frame_wanted,text='No', value='no', font =('arial', 9, 'bold'), bg='white')
        no.grid(row=0,column=1, pady=2,padx=4,sticky=W)
        
        #Buttons
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=5,y=200,width=640,height=45)
        
        #add button
        btn_add=Button(button_frame,text='Record Save',font =('arial', 12, 'bold'),width=14, bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=3,pady=5,sticky=W)
        
        #Update button
        btn_add=Button(button_frame,text='Update',font =('arial', 12, 'bold'),width=14, bg='blue',fg='white')
        btn_add.grid(row=0,column=1,padx=3,pady=5, sticky=W)
        
        #Delete button
        btn_add=Button(button_frame,text='Delete',font =('arial', 12, 'bold'),width=14, bg='blue',fg='white')
        btn_add.grid(row=0,column=2,padx=3,pady=5,sticky=W)
        
        #Clear button
        btn_add=Button(button_frame,text='Clear',font =('arial', 12, 'bold'),width=14, bg='blue',fg='white')
        btn_add.grid(row=0,column=3,padx=3,pady=5,sticky=W)
        
        #background Side Image
        img4 =Image.open('images/police3.jpg')
        img4=img4.resize((470,245), Image.ANTIALIAS)
        self.photo4 =ImageTk.PhotoImage(img4)
        
        self.img4=Label(upper_frame,image=self.photo4)
        self.img4.place(x=910, y=30, height=245, width=470)
        
        
        
        
        
        #down frame
        down_frame =LabelFrame(Main_frame,bd=2,relief=RIDGE, text='Criminal Information Table',font =('times new roman', 10, 'bold'), fg="red", bg="white")
        down_frame.place(x=7,y=280, width=1600,height=370)

        
        #search frame
        search_frame =LabelFrame(down_frame,bd=2,relief=RIDGE, text='Search Criminal Record',font =('times new roman', 10, 'bold'), fg="red", bg="white")
        search_frame.place(x=0,y=0, width=1580,height=50)
        

        search_by=Label(search_frame,text='Search By:',font =('arial', 11, 'bold'), fg="white", bg="red")
        search_by.grid(row=0,column=0,padx=5,sticky=W)

        combo_search_box=ttk.Combobox(search_frame,font=("arial", 11, "bold"),width=18 ,state='readonly')
        combo_search_box['value']=('Select Option', 'Case_id', 'Criminal_no')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1, sticky=W, padx=5)
        
        search_txt=ttk.Entry(search_frame,width=18,font=("arial", 11, "bold"))
        search_txt.grid(row=0,column=2,padx=2,pady=5)

        #Search Button
        btn_search=Button(search_frame,text='Search',font =('arial', 13, 'bold'),width=14, bg='blue',fg='white')
        btn_search.grid(row=0,column=3,padx=3,pady=2)
        
        #All button
        btn_all=Button(search_frame,text='Show All',font =('arial', 13, 'bold'),width=14, bg='blue',fg='white')
        btn_all.grid(row=0,column=4,padx=3,pady=2)
        
        crimeagency = Label(search_frame, text='NATIONAL CRIME AGENCY', font=('arial', 30, 'bold'), fg="crimson", bg="white")
        lbl_gender.grid(row=0, column=5, padx=50, pady=0 ,sticky=W)
        
        #Table Frame
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=50,width=1470, height=170)
        
        #Scrollbar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        
        self.criminal_table = ttk.Treeview(table_frame, column=("1","2","3","4","5","6","7","8","9","10","11","12","13","14"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading('1',text='CaseId')
        self.criminal_table.heading('2', text="CrimeNo")
        self.criminal_table.heading('3', text='Criminal Name')
        self.criminal_table.heading('4', text='NickName')
        self.criminal_table.heading('5', text='ArrestDate')
        self.criminal_table.heading('6', text='CrimeOfDate')
        self.criminal_table.heading('7', text='Address')
        self.criminal_table.heading('8', text='Age')
        self.criminal_table.heading('9', text='Occupation')
        self.criminal_table.heading('10', text='Birth Mark')
        self.criminal_table.heading('11', text='Crime Type')
        self.criminal_table.heading('12', text='Father Name')
        self.criminal_table.heading('13', text='Gender')
        self.criminal_table.heading('14', text='Wanted')

        self.criminal_table['show'] = 'headings'

        self.criminal_table.column("1",width=100)
        self.criminal_table.column("2", width=100)
        self.criminal_table.column("3", width=100)
        self.criminal_table.column("4", width=100)
        self.criminal_table.column("5", width=100)
        self.criminal_table.column("6", width=100)
        self.criminal_table.column("7", width=100)
        self.criminal_table.column("8", width=100)
        self.criminal_table.column("9", width=100)
        self.criminal_table.column("10", width=100)
        self.criminal_table.column("11", width=100)
        self.criminal_table.column("12", width=100)
        self.criminal_table.column("13", width=100)
        self.criminal_table.column("14", width=100)

        self.criminal_table.pack(fill=BOTH,expand=1)
        
if __name__ =="__main__":
    root=Tk()
    obj=Criminal(root)
    root.mainloop()
