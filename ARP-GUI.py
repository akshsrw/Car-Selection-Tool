from tkinter import *
import numpy as np
import matplotlib.pyplot as plt


MyGui=Tk()

MyGui.title("VEHICLE DECISION TOOL")
MyGui.geometry("700x350+50+50")    




def enter():
    

    enter.sel= clicked.get()
    M = text2.get()
    enter.B = text3.get()
    enter.F= text4.get()
    enter.x=int(M)
    
    
    
    


def result():
    print(enter.x)
    mileage=np.arange(0,enter.x+1000,1000)
    budget= int(enter.B)
    f= int(enter.F)


    if enter.sel == "Compact":
        cost_ice = budget + mileage*4.7*0.0153
        co2_ice= 8 + 120*mileage*0.000001
        
        cost_bev = budget + 0.3*mileage*0.15
        co2_bev = 12 + mileage*0.15*321*0.000001
        
        cost_phev= budget + 405*f + (mileage-9000*f)*0.08415
        co2_phev= 10.9 + 60*mileage*0.000001
        
        fig, (ax1,ax2) = plt.subplots(nrows=2,ncols=1)

        ax1.plot(mileage,cost_ice,label="ICE")
        ax1.plot(mileage,cost_bev,label="BEV")
        ax1.plot(mileage,cost_phev,label="PHEV")

        ax1.legend()

        ax1.set_title("COST VS MILEAGE")
        ax1.set_xlabel("MILEAGE")
        ax1.set_ylabel("COST")



        ax2.plot(mileage,co2_ice,label="ICE")
        ax2.plot(mileage,co2_bev,label="BEV")
        ax2.plot(mileage,co2_phev,label="PHEV")

        ax2.legend()

        ax2.set_title("CO2 VS MILEAGE")
        ax2.set_xlabel("MILEAGE")
        ax2.set_ylabel("CO2 Emission")


        plt.tight_layout()
        plt.show(block=False)
        
        
        
    elif enter.sel == "Mid-Range":
        cost_ice = budget + mileage*5.5*0.0153
        co2_ice= 9.2 + 135*mileage*0.000001
        
        cost_bev = budget + 0.3*mileage*0.17
        co2_bev = 14.6 + mileage*0.17*321*0.000001
        
        cost_phev= budget + 612*f + (mileage-12000*f)*0.09945
        co2_phev= 12.9 + 68*mileage*0.000001
        
        fig, (ax1,ax2) = plt.subplots(nrows=2,ncols=1)

        ax1.plot(mileage,cost_ice,label="ICE")
        ax1.plot(mileage,cost_bev,label="BEV")
        ax1.plot(mileage,cost_phev,label="PHEV")

        ax1.legend()

        ax1.set_title("COST VS MILEAGE")
        ax1.set_xlabel("MILEAGE")
        ax1.set_ylabel("COST")



        ax2.plot(mileage,co2_ice,label="ICE")
        ax2.plot(mileage,co2_bev,label="BEV")
        ax2.plot(mileage,co2_phev,label="PHEV")

        ax2.legend()

        ax2.set_title("CO2 VS MILEAGE")
        ax2.set_xlabel("MILEAGE")
        ax2.set_ylabel("CO2 Emission")




        plt.tight_layout()
        plt.show(block=False)
        
    
    else:
        cost_ice = budget + mileage*6.6*0.0153
        co2_ice= 10.2 + 167*mileage*0.000001
        
        cost_bev = budget + 0.3*mileage*0.2
        co2_bev = 15 + mileage*0.2*321*0.000001
        
        cost_phev= budget + 990*f + (mileage-16500*f)*0.1071
        co2_phev= 13.9 + 75*mileage*0.000001
        
        fig, (ax1,ax2) = plt.subplots(nrows=2,ncols=1)

        ax1.plot(mileage,cost_ice,label="ICE")
        ax1.plot(mileage,cost_bev,label="BEV")
        ax1.plot(mileage,cost_phev,label="PHEV")

        ax1.legend()

        ax1.set_title("COST VS MILEAGE")
        ax1.set_xlabel("MILEAGE")
        ax1.set_ylabel("COST")



        ax2.plot(mileage,co2_ice,label="ICE")
        ax2.plot(mileage,co2_bev,label="BEV")
        ax2.plot(mileage,co2_phev,label="PHEV")

        ax2.legend()

        ax2.set_title("CO2 VS MILEAGE")
        ax2.set_xlabel("MILEAGE")
        ax2.set_ylabel("CO2 Emission")




        plt.tight_layout()
        plt.show(block=False)
    



myLabel1=Label(text="Enter Vehicle Specifications",fg='black',font=20).place(x=50,y=25)

myname1= Label(text="Select Car Size: ",fg='black',bg='white', font=15).place(x=50,y=70)
myname2= Label(text="Annual Mileage (in km): ",fg='black',bg='white',font=15).place(x=50,y=110)
myname3= Label(text="Budget (in Euros)  : ",fg='black',bg='white',font=15).place(x=50,y=150)
myname4= Label(text="Charging frequency(for PHEV) per Day: ",fg='black',bg='white',font=15).place(x=50,y=190)

options= ["Compact", "Mid-Range","Luxury/SUV"]
clicked = StringVar()
clicked.set(options[2])


chooseCar= OptionMenu(MyGui,clicked, *options).place(x=420,y= 70)

text2=Entry(font=15)
text2.place(x=420,y= 110)
text3=Entry(font=15)
text3.place(x=420,y= 150)
text4=Entry(font=15)
text4.place(x=420,y= 190)

button1=Button(text="Enter_Values",font=15,command= enter).place(x=30,y=250)

button2=Button(text="View Result",font=15,command=result).place(x=250,y=250)




MyGui.mainloop()

################################################################################################################################









