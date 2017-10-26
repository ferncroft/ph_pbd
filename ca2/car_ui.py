from tkinter import *
from car import *

class rentals:
	
    def clearall(self): 
		# clears the text input areas
        self.e.delete(0,END)
        self.eName.delete(0,END)
        self.pIn.delete(0,END)
        self.pOut.delete(0,END)
        self.dIn.delete(0,END)
        self.dOut.delete(0,END)
        self.eIn.delete(0,END)
        self.eOut.delete(0,END)
        self.hIn.delete(0,END)
        self.hOut.delete(0,END)
        
    def clearname(self):
        self.eName.delete(0,END)
        
    def setall(self):
        # set the current number of vehicles available / out visuals
        self.pIn.insert(0,len(self.petrol_cars_in))
        self.pOut.insert(0,len(self.petrol_cars_out))
        self.dIn.insert(0,len(self.diesel_cars_in))
        self.dOut.insert(0,len(self.diesel_cars_out))
        self.eIn.insert(0,len(self.electric_cars_in))
        self.eOut.insert(0,len(self.electric_cars_out))
        self.hIn.insert(0,len(self.hybrid_cars_in))
        self.hOut.insert(0,len(self.hybrid_cars_out))
        self.eName.insert(0,"Name for new rental")

    def action(self,argi): 
		#pressed button's value is inserted into the end of the text area
        the_name = self.eName.get()
        if the_name == 'Name for new rental':
            if argi[1] == "-":
                the_name = 'Anonymous'
            else:
                the_name = ""

        self.clearall()
        if argi[0]=="P":
            the_type = "Petrol"
        elif argi[0]=="D":
            the_type = "Diesel"
        elif argi[0]=="E":
            the_type = "Electric"
        else:
            the_type = "Hybrid"
            
        if argi[1] == "+":
            the_action = "Return"
        else:
            the_action = "Rental"
#            print('Name = ', the_name)
        
        # actions for petrol cars
        if (the_type == "Petrol"):
            if the_action == "Rental":
                if len(self.petrol_cars_in) > 0:
                    msg = 'Petrol car ' + self.petrol_cars_in[len(self.petrol_cars_in)-1].regno + ' has been rented to '
                    self.petrol_cars_in[len(self.petrol_cars_in)-1].setOutOnHire = True
                    self.petrol_cars_in[len(self.petrol_cars_in)-1].renter_name = the_name
                    self.petrol_cars_out.append(self.petrol_cars_in[len(self.petrol_cars_in)-1])
                    self.petrol_cars_in.pop()
                else:
                    msg = 'No petrol cars available'
            else:
                if len(self.petrol_cars_out) > 0:
                    msg = 'Petrol car ' + self.petrol_cars_out[len(self.petrol_cars_out)-1].regno + ' now returned from '
                    self.petrol_cars_out[len(self.petrol_cars_out)-1].setOutOnHire = False
                    the_name = self.petrol_cars_out[len(self.petrol_cars_out)-1].renter_name
                    self.petrol_cars_in.append(self.petrol_cars_out[len(self.petrol_cars_out)-1])
                    self.petrol_cars_out.pop()
                else:
                    msg = 'No petrol cars rented'

        # actions for diesel cars
        if (the_type == "Diesel"):
            if the_action == "Rental":
                if len(self.diesel_cars_in) > 0:
                    msg = 'Diesel car ' + self.diesel_cars_in[len(self.diesel_cars_in)-1].regno + ' has been rented to '
                    self.diesel_cars_in[len(self.diesel_cars_in)-1].setOutOnHire = True
                    self.diesel_cars_in[len(self.diesel_cars_in)-1].renter_name = the_name
                    self.diesel_cars_out.append(self.diesel_cars_in[len(self.diesel_cars_in)-1])
                    self.diesel_cars_in.pop()
                else:
                    msg = 'No diesel cars available'
            else:
                if len(self.diesel_cars_out) > 0:
                    msg = 'Diesel car ' + self.diesel_cars_out[len(self.diesel_cars_out)-1].regno + ' now returned from '
                    self.diesel_cars_out[len(self.diesel_cars_out)-1].setOutOnHire = False
                    the_name = self.diesel_cars_out[len(self.diesel_cars_out)-1].renter_name
                    self.diesel_cars_in.append(self.diesel_cars_out[len(self.diesel_cars_out)-1])
                    self.diesel_cars_out.pop()
                else:
                    msg = 'No diesel cars rented'

        # actions for electric cars
        if (the_type == "Electric"):
            if the_action == "Rental":
                if len(self.electric_cars_in) > 0:
                    msg = 'Electric car ' + self.electric_cars_in[len(self.electric_cars_in)-1].regno + ' has been rented to '
                    self.electric_cars_in[len(self.electric_cars_in)-1].setOutOnHire = True
                    self.electric_cars_in[len(self.electric_cars_in)-1].renter_name = the_name
                    self.electric_cars_out.append(self.electric_cars_in[len(self.electric_cars_in)-1])
                    self.electric_cars_in.pop()
                else:
                    msg = 'No electric cars available'
            else:
                if len(self.electric_cars_out) > 0:
                    msg = 'Electric car ' + self.electric_cars_out[len(self.electric_cars_out)-1].regno + ' now returned from '
                    self.electric_cars_out[len(self.electric_cars_out)-1].setOutOnHire = False
                    the_name = self.electric_cars_out[len(self.electric_cars_out)-1].renter_name
                    self.electric_cars_in.append(self.electric_cars_out[len(self.electric_cars_out)-1])
                    self.electric_cars_out.pop()
                else:
                    msg = 'No electric cars rented'

        # actions for hybrid cars
        if (the_type == "Hybrid"):
            if the_action == "Rental":
                if len(self.hybrid_cars_in) > 0:
                    msg = 'Hybrid car ' + self.hybrid_cars_in[len(self.hybrid_cars_in)-1].regno + ' has been rented to '
                    self.hybrid_cars_in[len(self.hybrid_cars_in)-1].setOutOnHire = True
                    self.hybrid_cars_in[len(self.hybrid_cars_in)-1].renter_name = the_name
                    self.hybrid_cars_out.append(self.hybrid_cars_in[len(self.hybrid_cars_in)-1])
                    self.hybrid_cars_in.pop()
                else:
                    msg = 'No hybrid cars available'
            else:
                if len(self.hybrid_cars_out) > 0:
                    msg = 'Hybrid car ' + self.hybrid_cars_out[len(self.hybrid_cars_out)-1].regno + ' now returned from '
                    self.hybrid_cars_out[len(self.hybrid_cars_out)-1].setOutOnHire = False
                    the_name = self.hybrid_cars_out[len(self.hybrid_cars_out)-1].renter_name
                    self.hybrid_cars_in.append(self.hybrid_cars_out[len(self.hybrid_cars_out)-1])
                    self.hybrid_cars_out.pop()
                else:
                    msg = 'No hybrid cars rented'

        self.clearall()
        self.setall()
        self.e.insert(END,msg + the_name)
            

    def __init__(self,master):
		#Constructor - create grid and lists
        master.title('Aungier Car Rentals') 
        master.geometry()
        self.e = Entry(master,width=48)
        self.e.grid(row=5,column=0,columnspan=5)
        self.eName = Entry(master,width=36,text='Name')
        self.eName.grid(row=0,column=0,columnspan=3)
#        self.eName.focus(self.clearname(self))
        self.l1 = Label(master,width=6, text = "In")
        self.l1.grid(row=0, column=4)
        self.l1 = Label(master,width=6, text = "Out")
        self.l1.grid(row=0, column=5)
#        self.e.focus_set() #Sets focus on the input text area
        self.pIn = Entry(master, width=6,justify=RIGHT)
        self.pIn.grid(row=1,column=4)
        self.pOut = Entry(master, width=6,justify=RIGHT)
        self.pOut.grid(row=1,column=5)
        self.dIn = Entry(master, width=6,justify=RIGHT)
        self.dIn.grid(row=2,column=4)
        self.dOut = Entry(master, width=6,justify=RIGHT)
        self.dOut.grid(row=2,column=5)
        self.eIn = Entry(master, width=6,justify=RIGHT)
        self.eIn.grid(row=3,column=4)
        self.eOut = Entry(master, width=6,justify=RIGHT)
        self.eOut.grid(row=3,column=5)
        self.hIn = Entry(master, width=6,justify=RIGHT)
        self.hIn.grid(row=4,column=4)
        self.hOut = Entry(master, width=6,justify=RIGHT)
        self.hOut.grid(row=4,column=5)
        self.electric_cars_in = []
        self.petrol_cars_in   = []
        self.diesel_cars_in   = []
        self.hybrid_cars_in   = []
        self.electric_cars_out = []
        self.petrol_cars_out   = []
        self.diesel_cars_out   = []
        self.hybrid_cars_out   = []


		#Generating Buttons
        Button(master,text="Petrol",  width=10).grid(row=1, column=0)
        Button(master,text="Rent",    width=8,command=lambda:self.action('P-')).grid(row=1, column=1)
        Button(master,text="Return",  width=8,command=lambda:self.action('P+')).grid(row=1, column=2)
        
        Button(master,text="Diesel",  width=10).grid(row=2, column=0)
        Button(master,text="Rent",    width=8,command=lambda:self.action('D-')).grid(row=2, column=1)
        Button(master,text="Return",  width=8,command=lambda:self.action('D+')).grid(row=2, column=2)
        
        Button(master,text="Electric",width=10).grid(row=3, column=0)
        Button(master,text="Rent",    width=8,command=lambda:self.action('E-')).grid(row=3, column=1)
        Button(master,text="Return",  width=8,command=lambda:self.action('E+')).grid(row=3, column=2)
        
        Button(master,text="Hybrid",  width=10).grid(row=4, column=0)
        Button(master,text="Rent",    width=8,command=lambda:self.action('H-')).grid(row=4, column=1)
        Button(master,text="Return",  width=8,command=lambda:self.action('H+')).grid(row=4, column=2)

    def create_current_stock(self):
        # sets up the RegNo lists and applies them to the fleets lists
        eCars = ["E001","E002","E003","E004"]
        dCars = ["D001","D002","D003","D004","D005","D006","D007","D008"]
        hCars = ["H001","H002","H003","H004","H005","H006","H007","H008"]
        pCars = ["P001","P002","P003","P004","P005","P006","P007","P008","P009","P010","P011","P012","P013","P014","P015","P016","P017","P018","P019","P020"]

        for i in range(4):
           self.electric_cars_in.append(ElectricCar())
           self.electric_cars_in[i].regno = eCars[i]
        for i in range(20):
           self.petrol_cars_in.append(PetrolCar())
           self.petrol_cars_in[i].regno = pCars[i]
        for i in range(8):
           self.diesel_cars_in.append(DieselCar())
           self.diesel_cars_in[i].regno = dCars[i]
        for i in range(8):
           self.hybrid_cars_in.append(HybridCar())
           self.hybrid_cars_in[i].regno = hCars[i]
           
        self.clearall()
        self.setall()
           

#Main
root = Tk()
obj=rentals(root) #object instantiated
rentals.create_current_stock(obj)
root.mainloop()