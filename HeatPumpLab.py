try:
    from CoolProp.CoolProp import PropsSI
except ModeleNotFoundError:
    print("You do not have Coolprop configured properly")

from tkinter import Tk, Button, Entry, Label, Text, ttk, StringVar

# Make a Python GUI to input different modules
# Lab 2 has no homework. All analysis is completed in class.

fluid = 'R134a'
"""
NOTE! r-134a values correspond to the ASHRAE values of 200kJ offset for enthalpy and 1kj/kg-k offset for 
entropy. Textbook values are standard reference states. 
"""

# Dictionary holding CoolProp compatible values
helper = {
    "": "",  # Randomly requires a blank to iterate during optionmenu
    "Temperature": "T",
    "Pressure": "P",
    "Quality": "Q",
    "Specific Heat": "C",
    "Entropy": "S",
    "Enthalpy": "H",
    "Density": "D",
}

units = {
    "Temperature": "K",
    "Pressure": "kPa",
    "Quality": "%",
    "Specific Heat": "kJ/kg*K",
    "Entropy": "kJ/kg*K",
    "Enthalpy": "kJ/kg",
    "Density": "kg/m3",
}


def prop(value, p1, v1, p2, v2):
    ''' Input the value of '''
    answer = PropsSI(value, p1, v1, p2, v2, fluid)
    return round(answer, 3)


def submit_button(*args):
    ''' Calculates values, erases old data, updates text with new data. Removes text from old data '''
    # Gets new values
    v1 = parameter_1_entry.get()
    v2 = parameter_2_entry.get()
    p1 = p1_var.get()
    p2 = p2_var.get()
    des = des_var.get()

    # Calculates property and writes answer with units, name, and value to text widget
    var1 = str(prop(helper[des], helper[p1], float(v1), helper[p2], float(v2)))
    answer = des + " = " + var1 + " " + units[des]
    results_text.delete(0.0, "end")
    results_text.insert(0.0, answer)
    pass


def write_values():
    count = 0
    '''Writes all values and attempts to a csv file.'''
    with open("results.txt","w") as master:
        master.write()
        master.close()


# Constructor for the interface 
root = Tk()
root.geometry('500x400')

fluid_label = Label(root, text="Fluid: R-134a").grid(row=0, column=0, sticky="w")

# Parameter 1 information
parameter_1_label = Label(root, text="Parameter 1").grid(row=1, column=0, sticky="w")
p1_var = StringVar(root)
p1_var.set('Pressure')  # set the default option
parameter_1_menu = ttk.OptionMenu(root, p1_var, *helper.keys())
parameter_1_menu.grid(row=1, column=1)

parameter_1_entry = Entry(root, width=15)
parameter_1_entry.grid(row=1, column=2)

# Parameter 2 information
parameter_2_label = Label(root, text="Parameter 2").grid(row=2, column=0, sticky="w")
p2_var = StringVar(root)
p2_var.set('Temperature')  # set the default option
parameter_2_menu = ttk.OptionMenu(root, p2_var, *helper.keys())
parameter_2_menu.grid(row=2, column=1)
parameter_2_entry = Entry(root, width=15)
parameter_2_entry.grid(row=2, column=2)

# Desired value to obtain.
des_label = Label(root, text="Desired Value").grid(row=3, column=0, sticky="w")
des_var = StringVar(root)
des_var.set('Enthalpy')  # set the default opti# on
des_menu = ttk.OptionMenu(root, des_var, *helper.keys())
des_menu.grid(row=3, column=1)

# Submit button
calculate_button = Button(root, text="Submit", command=submit_button)
calculate_button.grid(row=4, column=1)

# Results section
results_text = Text(root, width=50, height=8, selectborderwidth=2)
results_text.grid(row=5, columnspan=4, sticky='w')
results_label = Label(root, text="Results").grid(row=4, column=0)

root.mainloop()
