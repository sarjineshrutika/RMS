#!/usr/bin/env python
# coding: utf-8

# In[12]:


class RMS:

    def __init__(self,restaurant_name,restaurant_menu):
        self.user_bill=0
        self.menu=restaurant_menu
        self.user_order=''
        self.user_pay=0
        self.rest_name=restaurant_name
        self.user_rep=''
    def welcome_user(self):
        #welcome user
        print("welcome to",self.rest_name)
    
    def display_menu(self):
        # Dispaly menu
        print("menu:")
        for i in self.menu:
            print(i.title(),self.menu[i])
    
    def take_order(self):
        self.user_order=input("please place your order here:")
    
    def preparing_order(self):
        print("preparing order",self.user_order)
        import time
        time.sleep(1)
        self.user_bill=self.user_bill+self.menu[self.user_order.lower()]
    
    def serve_order(self):
        print("you order is ready",self.user_order)
        print("Please enjoy your order",self.user_order.title())
    
    def display_bill(self):
        #user_bill=menu(user_order.lower())
        print("total bill:",self.user_bill)
    
    def verify_bill(self):
        self.user_pay=int(input("please pay your bill here:"))
        while self.user_pay<self.user_bill:
            print("unsuccessfull payment")
            self.user_bill=self.user_bill-self.user_pay
            print("please pay your remaining payment:",self.user_bill)
            self.user_pay=int(input("Please pay your bill here"))
        if self.user_pay>self.user_bill:
            print("Payment successfull")
            print("take your remaining change:",self.user_pay-self.user_bill)
        else:
            print("payment Successfull!")
    
    def thank_user(self):
        #thank user
        print(" Thanks for visiting",self.rest_name)
        
    def order_process(self):
        self.display_menu()
        self.take_order()
        if self.user_order.lower() in self.menu:
            self.preparing_order()
            self.serve_order()
            self.user_rep=input("Do you want to order anything else?")
            while self.user_rep.lower()=='yes':
                self.repeat_order()
                self.user_rep=input("Do you want to order anything else?")
            self.display_bill()
            self.verify_bill()
            self.thank_user()
        else:
            print("Invalid order")
            self.order_process()
    
    def repeat_order(self):
        self.display_menu()
        self.take_order()
        if self.user_order.lower() in self.menu:
            self.preparing_order()
            self.serve_order()
        else:
            print('Invalid Order')
            self.repeat_order()
    


# In[14]:


if __name__=='__main__':   

    
    moonlight_rm={"cold coffee":100,"latte coffee":120,"drip coffee":200}
    moonlight_rn='Moonlight Cafe'                           
    
    moonlight_rest=RMS(moonlight_rn,moonlight_rm)
    
    import tkinter as tk

    window=tk.Tk()
    
    window.title("Shrutika")
    
    window.geometry("400x400")
    
    # label
    tk.Label(window, text="Moonlight Cafe",font=("arial black",25)).place(x=75,y=50)
    
    tk.Button(window, text="START ORDER",command=moonlight_rest.order_process,width=20).place(x=130,y=115)
    
    window.mainloop()
    
    


# In[ ]:





# In[ ]:





# In[ ]:




