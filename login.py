from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk  #pip install pillow
from tkinter import messagebox
import mysql.connector
from hotel import HotelManagementSystem

def main():
  win=Tk()
  app=login_window(win)
  win.mainloop()
  

class login_window:

  def __init__(self,root):
    self.root=root
    self.root.title("Login")
    self.root.geometry("1550x800+0+0")
    
    self.var_email=StringVar()
    self.var_pass=StringVar()

    self.bg=ImageTk.PhotoImage(file=r"D:\PROJECTS\hotel management\login page\IMAGE.jpg")
    lbl_bg= Label(self.root,image=self.bg)
    lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

    frame=Frame(self.root,bg="black")
    frame.place(x=610,y=170,width=340,height=450)
    
    img1=Image.open(r"D:\PROJECTS\hotel management\login page\img1.png")
    img1=img1.resize((100,100),img1.ANTIALTAS)
    self.photoimg1=ImageTk.PhotoImage(img1)
    lblimg1=Label(image=self.photoimg1,bg="black",borderwidth=0)
    lblimg1.place(x=730,y=175,width=100,height=100)

    get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
    get_str.place(x=95,y=100)
    
    # Label
    username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
    username.place(x=70,y=155)
    
    self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
    self.txtuser.place(x=40,y=180,width=270)
    
    password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
    password.place(x=70,y=225)
    
    self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
    self.txtpass.place(x=40,y=250,width=270)
    
    # ========Icon IMAGES=====
    img2=Image.open(r"D:\PROJECTS\hotel management\login page\img1.png")
    img2=img2.resize((25,25),img2.ANTIALTAS)
    self.photoimg2=ImageTk.PhotoImage(img2)
    lblimg2=Label(image=self.photoimg2,bg="black",borderwidth=0)
    lblimg2.place(x=650,y=323,width=25,height=25)
    
    img3=Image.open(r"D:\PROJECTS\hotel management\login page\img3.jpg")
    img3=img3.resize((25,25),img3.ANTIALTAS)
    self.photoimg3=ImageTk.PhotoImage(img3)
    lblimg3=Label(image=self.photoimg3,bg="black",borderwidth=0)
    lblimg3.place(x=650,y=395,width=25,height=25)
    
    # login button
    loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
    loginbtn.place(x=110,y=300,width=120,height=35)
    
    #register button 
    registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
    registerbtn.place(x=15,y=350,width=160)
    
    # forget password button 
    forgetpasswordbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
    forgetpasswordbtn.place(x=10,y=375,width=160)
  
  def register_window(self):
    self.new_window=Toplevel(self.root)
    self.app=Register(self.new_window) 
    
  def login(self):
    self.new_window=Toplevel(self.root)   #Extra which is not in real code
    if self.txtuser.get()=="" or self.txtpass.get()=="":
      
      messagebox.showerror("Error","all field required")
    elif self.txtuser.get()=="ganga" and self.txtpass.get()=="123":
      messagebox.showinfo("Sucess","congratulations! You have successfully logged in.")
    else:
      conn=mysql.connector.connect(host="localhost",user="root",password="Ganga@#123",database="mydata")
      my_cursor=conn.cursor()
      my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                              self.var_email.get(),
                                                                              self.var_pass.get()
                                                                      ))
      
      row=my_cursor.fetchone()
      if row!=None:
        messagebox.showerror("Error","Invalid Username and Password")
      else:
        open_main=messagebox.askyesno("YesNo","Access only admin")
        if open_main>0:
          self.new_window=Toplevel(self.root)
          # self.app=Hotel(self.new_window)        # add project class name
          self.app=HotelManagementSystem(self.new_window)
        else:
          if not open_main:
            return
      conn.commit()
      conn.close()
      
  # ========================= Reset password ===========================    
  def reset_pass(self):
    if self.combo_security_Q.get()=="Select":
      messagebox.showerror("Error","Select the security question")
    elif self.txt_security.get()=="":
      messagebox.showerror("Error","Please enter the answer")
    elif self.txt_newpass.get()=="":
      messagebox.showerror("Error","Please enter the new password")
    else:
      conn=mysql.connector.connect(host="localhost",user="root",password="Ganga@#123",database="mydata")
      my_cursor=conn.cursor()
      qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
      value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
      my_cursor.execute(qury,value)
      row=my_cursor.fetchone()
      if row==None :
        messagebox.showerror("Error","Please enter the correct Answer")
      else:
        query=("update register set password=%s where email=%s")
        values=(self.txt_newpass.get(),self.txtuser.get())
        my_cursor.execute(query,values)
        
        conn.commit()
        conn.close()
        messagebox.showinfo("Info","Your password has been reset, please login new password")
      
      
    
  # ========================= Forgot Password window ===========================
  def forgot_password_window(self):
    if self.txtuser.get()=="":
      messagebox.showerror("Error","Please Enter the Email address to reset password")
    else:
      conn=mysql.connector.connect(host="localhost",user="root",password="Ganga@#123",database="mydata")
      my_cursor=conn.cursor()
      query=("select * from register where email=%s")
      value=(self.txtuser.get(),)
      my_cursor.execute(query,value)
      row=my_cursor.fetchone()
      # print(row)
      
      if row==None :
        messagebox.showerror("Error","Please Enter the valid username")
      else:
        conn.close()
        self.root2=Toplevel()
        self.root2.title("Forgot password")
        self.root2.geometry("340x450+610+170")
        
        l=Label(self.root2,text="Forgot password",font=("times new roman",20,"bold"),fg="red",bg="white")
        l.place(x=0,y=10,relwidth=1)
        
        security_Q=Label(self.root2,text="Select Security Questions",font=("timews new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=80)
    
        self.combo_security_Q=ttk.Combobox(self.root2,font=("timews new roman",15,"bold"),state="realdonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Friend Name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=110,width=250)
        self.combo_security_Q.current(0)
    
        secutity_A=Label(self.root2,text="Security Answer",font=("timews new roman",15,"bold"),bg="white",fg="black")
        secutity_A.place(x=50,y=150)
    
        self.txt_security=ttk.Entry(self.root2,font=("timews new roman",15,"bold"))
        self.txt_security.place(x=50,y=180,width=250)
        
        new_password=Label(self.root2,text="New Password",font=("timews new roman",15,"bold"),bg="white",fg="black")
        new_password.place(x=50,y=220)
    
        self.txt_newpass=ttk.Entry(self.root2,font=("timews new roman",15,"bold"))
        self.txt_newpass.place(x=50,y=250,width=250)
        
        btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("timews new roman",15,"bold"),fg="white",bg="green")
        btn.place(x=100,y=290)
      
    
      
class Register:
  def __init__(self,root):
    self.root=root
    self.root.title("Register")
    self.root.geometry("1600x900+0+0")
    
    # ================= variables ================
    self.var_fname=StringVar()
    self.var_lname=StringVar()
    self.var_contact=StringVar()
    self.var_email=StringVar()
    self.var_SecurityQ=StringVar()
    self.var_SecurityA=StringVar()
    self.var_pass=StringVar()
    self.var_confpass=StringVar()
    
    # ================= background image ================
    self.bg=ImageTk.PhotoImage(file=r"D:\PROJECTS\hotel management\Register page\image.jpg")
    
    bg_lbl=Label(self.root,image=self.bg)
    bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
    
    # ================= left image =================
    self.bg1=ImageTk.PhotoImage(file=r"D:\PROJECTS\hotel management\Register page\image1.jpg")
    
    left_lbl=Label(self.root,image=self.bg1)
    left_lbl.place(x=50,y=100,width=470,height=550)
    
    # ================= main frame =================
    frame=Frame(self.root,bg="white")
    frame.place(x=520,y=100,width=800,height=550)
    
    # ================= Resister =================
    register_lbl=Label(frame,text="REGISTER HERE",font=("timews new roman",25,"bold"),fg="darkgreen",bg="white")
    register_lbl.place(x=20,y=20)
    
    # ================= label & entry =================
    # row1
    fname=Label(frame,text="First Name",font=("timews new roman",15,"bold"),bg="white")
    fname.place(x=50,y=100)
    
    fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("timews new roman",15))
    fname_entry.place(x=50,y=130,width=250)
    
    l_name=Label(frame,text="Last Name",font=("timews new roman",15,"bold"),bg="white",fg="black")
    l_name.place(x=370,y=100)
    
    self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("timews new roman",15))
    self.txt_lname.place(x=370,y=130,width=250)
    
    # row2
    contact=Label(frame,text="Contact No.",font=("timews new roman",15,"bold"),bg="white",fg="black")
    contact.place(x=50,y=170)
    
    self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("timews new roman",15))
    self.txt_contact.place(x=50,y=200,width=250)
    
    email=Label(frame,text="Email",font=("timews new roman",15,"bold"),bg="white",fg="black")
    email.place(x=370,y=170)
    
    self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("timews new roman",15))
    self.txt_email.place(x=370,y=200,width=250)
    
    # row3
    security_Q=Label(frame,text="Select Security Questions",font=("timews new roman",15,"bold"),bg="white",fg="black")
    security_Q.place(x=50,y=240)
    
    self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_SecurityQ,font=("timews new roman",15,"bold"),state="realdonly")
    self.combo_security_Q["values"]=("Select","Your Birth Place","Your Friend Name","Your Pet Name")
    self.combo_security_Q.place(x=50,y=270,width=250)
    self.combo_security_Q.current(0)
    
    secutity_A=Label(frame,text="Security Answer",font=("timews new roman",15,"bold"),bg="white",fg="black")
    secutity_A.place(x=370,y=240)
    
    self.txt_security=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("timews new roman",15))
    self.txt_security.place(x=370,y=270,width=250)
    
    # row4
    pswd=Label(frame,text="Password",font=("timews new roman",15,"bold"),bg="white",fg="black")
    pswd.place(x=50,y=310)
    
    self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("timews new roman",15))
    self.txt_pswd.place(x=50,y=340,width=250)
    
    confirm_pswd=Label(frame,text="Confirm Password",font=("timews new roman",15,"bold"),bg="white",fg="black")
    confirm_pswd.place(x=370,y=310)
    
    self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("timews new roman",15))
    self.txt_confirm_pswd.place(x=370,y=340,width=250)
    
    # ================= check button =================
    self.var_check=IntVar()
    checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("timews new roman",12,"bold"),onvalue=1,offvalue=0)
    checkbtn.place(x=50,y=380)
    
    
    # ================= buttons =================
    img=Image.open(r"D:\PROJECTS\hotel management\Register page\RN.png")
    img=img.resize((200,50),img.ANTIALTAS)
    self.photoimage=ImageTk.PhotoImage(img)
    b1=Button(frame,image=self.photoimage,command=self.register_data, borderwidth=0,cursor="hand2",font=("timews new roman",15,"bold"))
    b1.place(x=50,y=420,width=200)
    
    img1=Image.open(r"D:\PROJECTS\hotel management\Register page\LN1")
    img1=img1.resize((200,50),img1.ANTIALTAS)
    self.photoimage1=ImageTk.PhotoImage(img1)
    b2=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("timews new roman",15,"bold"))
    b2.place(x=370,y=420,width=200)
    
    
# ================== Function deckaration ===================
  def register_data(self):
    if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_SecurityQ.get()=="Select":
      messagebox.showerror("Error", "All Fields are reqquired")
    elif self.var_pass.get()!= self.var_confpass.get():
      messagebox.showerror("Error","password and confirm password  must be same")
    elif self.var_check.get()==0:
      messagebox.showerror("Error","Please agree our terms and comditions")
    else:
      conn=mysql.connector.connect(host="localhost",user="root",password="Ganga@#123",database="mydata")
      my_cursor=conn.cursor()
      query=("select * from register where email=%s")
      value=(self.var_email.get(),)
      my_cursor.execute(query,value)
      row=my_cursor.fetchone()
      if row !=None:
        messagebox.showerror("Error","User already exist please try another email")
      else:
        my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_fname.get(),
                                                                                self.var_lname.get(),
                                                                                self.var_contact.get(),
                                                                                self.var_email.get(),
                                                                                self.var_SecurityQ.get(),
                                                                                self.var_SecurityA.get(),
                                                                                self.var_pass.get(),
                                                                             ))
      conn.commit()
      conn.close()
      messagebox.showinfo("Sucess","Register Sucessfully")
  
    
if __name__=="__main__":
  main()