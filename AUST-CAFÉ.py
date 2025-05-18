### ICT250 FINAL PROJECT FALL 2021-2022 ###

from tkinter import*
import random

#POS TITLE
        
root=Tk()
root.geometry("1600x8000")
root.resizable(width=True, height=True)
root.title("AUST CAFÉ")
Tops = Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)
f1 = Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)
titleInfo = Label(Tops,font=('helvetica',30,'bold'),text="AUST CAFÉ",fg="#00BFFF",bd=10,anchor='w')
titleInfo.grid(row=0,column=0)

#Declarations 
rand = StringVar()
coffe = StringVar()
tea = StringVar()
nescaffe = StringVar()
pepsi = StringVar()
mankushe = StringVar()
subTotal = StringVar()
total = StringVar()
vat = StringVar()
cost = StringVar()

#functionalities# 
def count():
    x=random.randint(10,50)
    randomRef=str(x)
    rand.set(randomRef)

    if (coffe.get()== ""):
        coffeCost = 0
    else:
        coffeCost  = float(coffe.get())

    if (tea.get()==""):
        teaCost = 0
    else:
        teaCost = float(tea.get())

    if (nescaffe.get() == ""):
        nescaffeCost = 0
    else:
        nescaffeCost = float(nescaffe.get())

    if (pepsi.get() == ""):
        pepsiCost = 0
    else:
        pepsiCost = float(pepsi.get())
     
    if (mankushe.get() == ""):
        mankusheCost = 0
    else:
        mankusheCost = float(mankushe.get())
                
    costOfCoffe = coffeCost * 5000
    costOfTea = teaCost * 7000
    costOfNescaffe = nescaffeCost * 10000
    costOfPepsi = pepsiCost * 11000
    costOfMankushe = mankusheCost * 15000
    costOfMeal = "LBP", str ('%.2f' % (costOfCoffe + costOfTea + costOfNescaffe + costOfPepsi + costOfMankushe))
    payVat = ((costOfCoffe + costOfTea + costOfNescaffe + costOfPepsi + costOfMankushe) * 0.11)
    totalCost = (costOfCoffe + costOfTea + costOfNescaffe + costOfPepsi + costOfMankushe)
    overAllCost = "LBP", str ('%.2f' % (payVat + totalCost))
    paidVat = "LBP", str ('%.2f' % payVat)
    cost.set(costOfMeal)
    vat.set(paidVat)
    subTotal.set(costOfMeal)
    total.set(overAllCost)

    def show():
        roo = Tk()
        roo.geometry("200x120")
        roo.title("")
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Check Your Bill", fg="black", bd=5)
        lblinfo.grid(row=0, column=0)
        bxVat = Label(roo, font=('aria', 15, 'bold'), textvariable=cost.get(costOfMeal), fg="black", bd=5)
        bxVat.grid(row=2,column=0)
        roo.mainloop()
    show()
    
def qExit():
    root.destroy()

def reset():
    rand.set("") 
    coffe.set("")
    tea.set("")
    nescaffe.set("")
    pepsi.set("")
    mankushe.set("")
    subTotal.set("")
    vat.set("")
    cost.set("")
    total.set("")
 

#CAFE MENU LIST
coffeLabel = Label(f1, font=('arial', 16, 'bold'),text="Coffee", bd=16,anchor="w")
coffeLabel.grid(row=1, column=0)
bxCoffe = Entry(f1, font=('arial',16,'bold'),textvariable = coffe, bd=10, insertwidth=4,bg="#00BFFF",justify='right')
bxCoffe.grid(row=1,column=1)
nescaffeLabel = Label(f1, font=('arial', 16, 'bold'),text="Nescaffe",bd=16,anchor="w")
nescaffeLabel.grid(row=2, column=0)
bxNescaffe = Entry(f1, font=('arial',16,'bold'),textvariable=nescaffe,bd=10,insertwidth=4,bg="#00BFFF",justify='right')
bxNescaffe.grid(row=2,column=1)
teaLabel = Label(f1, font=('arial', 16, 'bold'),text="Tea",bd=16,anchor="w")
teaLabel.grid(row=3, column=0)
bxTea = Entry(f1, font=('arial',16,'bold'),textvariable=tea,bd=10,insertwidth=4,bg="#00BFFF",justify='right')
bxTea.grid(row=3,column=1)
pepsiLabel = Label(f1, font=('arial', 16, 'bold'),text="Pepsi",bd=16,anchor="w")
pepsiLabel.grid(row=4, column=0)
bxPepsi = Entry(f1, font=('arial',16,'bold'),textvariable=pepsi,bd=10,insertwidth=4,bg="#00BFFF",justify='right')
bxPepsi.grid(row=4,column=1)
mankusheLabel = Label(f1, font=('arial', 16, 'bold'),text="Mankushe",bd=16,anchor="w")
mankusheLabel.grid(row=5, column=0)
bxMankushe = Entry(f1, font=('arial',16,'bold'),textvariable=mankushe,bd=10,insertwidth=4,bg="#00BFFF",justify='right')
bxMankushe.grid(row=5,column=1)

#TOTAL COST
orderLabel = Label(f1, font=('arial', 16, 'bold'),text="Order No",bd=16,anchor="w")
orderLabel.grid(row=1, column=4)
bxOrder = Entry(f1, font=('arial',16,'bold'),textvariable=rand, bd=10, insertwidth=4, bg="#00BFFF",justify='right')
bxOrder.grid(row=1,column=5)
costLabel = Label(f1, font=('arial', 16, 'bold'),text="Cost of Order",bd=16,anchor="w")
costLabel.grid(row=2, column=4)
bxCost = Entry(f1, font=('arial',16,'bold'),textvariable=cost,bd=10,insertwidth=4,bg="#00BFFF",justify='right')
bxCost.grid(row=2,column=5)
vatLabel = Label(f1, font=('arial', 16, 'bold'),text="11% Vat",bd=16,anchor="w")
vatLabel.grid(row=3, column=4)
bxVat = Entry(f1, font=('arial',16,'bold'),textvariable=vat,bd=10,insertwidth=4,bg="#00BFFF",justify='right')
bxVat.grid(row=3,column=5)
subTotalLabel = Label(f1, font=('arial', 16, 'bold'),text="Sub Total",bd=16,anchor="w")
subTotalLabel.grid(row=4, column=4)
bxSubTotal = Entry(f1, font=('arial',16,'bold'),textvariable=subTotal,bd=10,insertwidth=4,bg="#00BFFF",justify='right')
bxSubTotal.grid(row=4,column=5)
totalCostLabel = Label(f1, font=('arial', 16, 'bold'),text="Total Cost",bd=16,anchor="w")
totalCostLabel.grid(row=5, column=4)
bxTotalCost = Entry(f1, font=('arial',16,'bold'),textvariable=total,bd=10,insertwidth=4,bg="#00BFFF",justify='right')
bxTotalCost.grid(row=5,column=5)

#TEST MENU
'''
lblTest= Label(f1, font=('arial', 16, 'bold'),text="Drinks",bd=16,anchor="w")
lblTest.grid(row=5, column=4)
'''

#INTERACTIVE BUTTONS
btnTotal = Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="#1E90FF",command=count).grid(row=7,column=2)
btnReset = Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="#98F5FF",command=reset).grid(row=7,column=3)
btnExit = Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="#1E90FF",command=qExit).grid(row=7,column=4)

#MENU PRICING
def price():
    roo = Tk()
    roo.geometry("600x220")
    roo.title("Price List")

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Food&Drinks", fg="steel blue", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="           ", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Price", fg="#F44336", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Mankushe", fg="#F44336", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="15000 LBP", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Nescaffe", fg="#F44336", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="10000 LBP", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pepsi", fg="#F44336", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="11000 LBP", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Tea", fg="#F44336", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="7000 LBP", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Coffee", fg="#F44336", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="5000 LBP", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    roo.mainloop()

igm = PhotoImage(file="menulogo.png")
btnprice = Button(root, image=igm, command=price).pack()

#PICTURES
imgpath = "banner-logo.png"
img = PhotoImage(file=imgpath)
panel = Label(root, image = img)
panel.place(x = 676, y = 50)
root.mainloop()