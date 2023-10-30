#!/usr/bin/env python
# coding: utf-8

# In[1]:


#calculator


from tkinter import *
import tkinter as tk

root =tk.Tk() 
root.title("Calculator")
root.geometry("450x300+100+50")

def add():
    a=int(t1.get())
    b=int(t2.get())
    c=a+b
    l4.config(text=""+str(c))
    
def sub():
    a=int(t1.get())
    b=int(t2.get())
    c=a-b
    l4.config(text=""+str(c))
    
def mul():
    a=int(t1.get())
    b=int(t2.get())
    c=a*b
    l4.config(text=""+str(c))
    
def div():r
    a=int(t1.get())
    b=int(t2.get())
    c=a/b
    l4.config(text=""+str(c))
 
f1=("Arial",20,'bold')
f1=Label(root,text="CALCULATOR",font=f1)
f1.place(x=170,y=10)

l1=Label(root,text="Enter X",font=f1)
l1.place(x=50,y=50)

t1=Entry(root,bd=2,font=f1,width=10)
t1.place(x=200,y=50)


l2=Label(root,text="Enter Y",font=f1)
l2.place(x=50,y=100)

t2=Entry(root,bd=2,font=f1,width=10)
t2.place(x=200,y=100)


l3=Label(root,text="Result",font=f1)
l3.place(x=50,y=150)

l4=Label(root,text="...........",font=f1)
l4.place(x=200,y=150)

b1=Button(root,text="ADD",font=f1,command=add)
b1.place(x=50,y=200)


b2=Button(root,text="SUB",font=f1,command=sub)
b2.place(x=150,y=200)


b3=Button(root,text="MUL",font=f1,command=mul)
b3.place(x=250,y=200)

b4=Button(root,text="DIV",font=f1,command=div)
b4.place(x=350,y=200)
       
root.configure(background="light green")   
root.mainloop()


# In[23]:





# In[7]:


pip install pyperclip


# In[1]:


pip list


# In[6]:


pip install photoimage


# In[24]:





# In[ ]:




