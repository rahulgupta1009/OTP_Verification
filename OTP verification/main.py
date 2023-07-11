import random
import smtplib
from tkinter import *
from tkinter import messagebox

class otp_verifier(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x400")
        self.resizable(False,False)
        server=smtplib.SMTP('smtp.gmail.com',587)
        #adding TLS security 
        server.starttls()
        #get your app password of gmail ----as directed in the video
        password='snhgheysmzwsocss'
        server.login('rahulgabrumunda1009@gmail.com',password)
        #generate OTP using random.randint() function
    
        self.n=str(self.OTP())
        msg = 'Hello,your OTP is '+self.n
        
        sender='rahulgabrumunda1009@gmail.com'  #write email id of sender
        receiver='ksinghxyz1@gmail.com' #write email of receiver
        #sending
        server.sendmail(sender,receiver,msg)
        server.quit()
    
   
    
        
    def Labels(self):
        self.c = Canvas(self,bg ="grey",width=400, height=280)
        self.c.place(x=50,y=75)
        
        
        
        self.upper_frame = Frame(self , bg = "#4682B4" , width = 1500 , height = 80 )
        self.upper_frame.place ( x = 0 , y = 0 )
        self.picture = PhotoImage (file = "password1.png")
        
        self.picture = PhotoImage (file = "password1.png")
        self.k = Label ( self.upper_frame, image = self.picture , bg = "#4682B4").place(x=80,y=10)
        
        self.Login_Title=Label(self,text="Verify OTP",font="TimesNewRoman,bold 30",bg ="#4682B4",fg="white")
        self.Login_Title.place(x=150,y=20)
        
    def Entry(self):
        self.User_Name = Text(self,font = "calibri 20", borderwidth = 2,wrap = WORD, width = 20 , height = 1 )
        self.User_Name.place(x = 105,y = 100)
        
    def OTP(self):
        return random.randrange(100000,1000000)
        
        
    
    def Buttons(self):
        self.submitButtonImage=PhotoImage(file = "submit.png")
        self.submitButton = Button(self , image=self.submitButtonImage, command = lambda:[self.checkOTP(), self.runTimer()], border = 0 )
        self.submitButton.place(x = 200 ,y = 160)
        
        self.resendOTPImage =PhotoImage(file="resendotp.png")
        self.resendOTP=Button(self ,image= self.resendOTPImage , command = self.resendOTP,  border= 0)
        self.resendOTP.place(x = 180,y = 240)
        
    def resendOTP(self):
        server=smtplib.SMTP('smtp.gmail.com',587)
        #adding TLS security 
        server.starttls()
        #get your app password of gmail ----as directed in the video
        password='snhgheysmzwsocss'
        server.login('rahulgabrumunda1009@gmail.com',password)
        #generate OTP using random.randint() function
        self.n=str(self.OTP())
        msg = 'Hello,your OTP is '+self.n
       
        sender='rahulgabrumunda1009@gmail.com'  #write email id of sender
        receiver='ksinghxyz1@gmail.com' #write email of receiver
        #sending
        server.sendmail(sender,receiver,self.n)
        server.quit()    
        
    def checkOTP(self):
        try:
            self.userInput=int(self.User_Name.get(1.0, "end-1c"))
            if self.userInput == int(self.n):
                messagebox.showinfo ("showinfo", "Verification Successful")
                self.n = "done"
            else:
                messagebox.showinfo("showinfo", "wrong OTP")
        except:
            messagebox.showinfo ("showinfo", "INVALID OTP ")    
            
        
if __name__=="__main__":
    window=otp_verifier()
    window.Labels()
    window.Entry()
    window.OTP()
    window.Buttons()
    window.mainloop()
            