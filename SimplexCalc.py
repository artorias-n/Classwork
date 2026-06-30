#imports
from tkinter import *
import math as m
import pulp as p
from tkinter import messagebox
from PIL import ImageTk,Image
#set up tkinter
root=Tk()
root.title("Simplex Calculator")

def help_page():
    help_page = Toplevel()
    help_page.title("Help Page")

    # Create a canvas and a scrollbar
    canvas = Canvas(help_page)
    scrollbar = Scrollbar(help_page, orient=VERTICAL, command=canvas.yview)
    scroll_frame = Frame(canvas)

    # Configure the canvas
    scroll_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Place canvas and scrollbar in the help_page window
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Store images as attributes of help_page to prevent garbage collection
    help_page.max_img = ImageTk.PhotoImage(Image.open("Maximize.png"))
    maximize = Label(scroll_frame, image=help_page.max_img)
    maximize.pack(pady=10)

    help_page.min_img = ImageTk.PhotoImage(Image.open("Minimize.png"))
    minimize = Label(scroll_frame, image=help_page.min_img)
    minimize.pack(pady=10)

    help_page.mix_img = ImageTk.PhotoImage(Image.open("mix.png"))
    mix = Label(scroll_frame, image=help_page.mix_img)
    mix.pack(pady=10)

    

def create_problem():
    try:
        #get user input
        var=int(e1.get())
        con=int(e2.get())
        max_or_min=clicked.get()
        
        #create second window
        top=Toplevel()
        
        ofc=Label(top, text="Objective Function Constaint")
        ofc.grid(row=0, column=0, columnspan=var+1, padx=10, pady=10)
        
        #objective function entries
        variables={}
        for i in range(var):
            variables[f'var{i+1}']=Entry(top, width=10, borderwidth=5)
            variables[f'var{i+1}'].grid(row=1, column=(i), padx=10, pady=10)

        constraints=Label(top, text="Constaints")
        constraints.grid(row=2, column=0, columnspan=5, padx=10, pady=10)
        
        #constraints entries
        constraints=[]
        drops={}

        for i in range(con):
            variables1={}
            for x in range(var+2):
                if x<var:
                    e=Entry(top, width=10, borderwidth=5)
                    e.grid(row=i+3, column=(x), padx=10, pady=10)
                    variables1[f'var{x+1}']=e
                elif x==var:
                    drops[f'drop+menu{i+1}']=StringVar()
                    drops[f'drop+menu{i+1}'].set("<=")
                    drop1=OptionMenu(top, drops[f'drop+menu{i+1}'],">=","<=","=")
                    drop1.grid(row=i+3, column=x, padx=5, pady=5)
                    variables1["inequality"]=drops[f'drop+menu{i+1}']
                    
                else:
                    e=Entry(top, width=10, borderwidth=5)
                    e.grid(row=i+3, column=(x), padx=10, pady=10)
                    variables1["rhs"]=e
                
            constraints.append(variables1)
        #solution button
        solution=Button(top, text="solve", command=lambda:solve(var, con, max_or_min, variables, constraints))
        solution.grid(row=con+4, column=0, columnspan=var+2, pady=10)
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid input for the problem.")

def solve(var, con, max_or_min, variables, constraints):
    try:
        # Create the Problem
        if max_or_min == "Maximize":
            Lp_prob = p.LpProblem("Primal_Problem", p.LpMaximize)
        else:
            Lp_prob = p.LpProblem("Primal_Problem", p.LpMinimize)

        # Create Decision Variables for the Primal
        xs = {f'x{i+1}': p.LpVariable(f'x{i+1}', lowBound=0) for i in range(var)}

        # Initialize the Objective Function
        obj_func = sum(float(variables[f'var{i+1}'].get()) * xs[f'x{i+1}'] for i in range(var))
        Lp_prob += obj_func  # Adding the objective function to the problem

        # Add Constraints
        for i in range(con):
            # Initialize the left-hand side of the constraint (lhs)
            lhs = sum(float(constraints[i][f'var{x+1}'].get()) * xs[f'x{x+1}'] for x in range(var))
            rhs = float(constraints[i]['rhs'].get())  # Right-hand side (rhs)
            inequality = constraints[i]['inequality'].get()  # Inequality (<=, >=, =)

            # Add the constraint to the problem based on the inequality type
            if inequality == ">=":
                Lp_prob += lhs >= rhs
            elif inequality == "<=":
                Lp_prob += lhs <= rhs
            else:
                Lp_prob += lhs == rhs

        # Solve the Primal Problem
        Lp_prob.solve()

        # Extract the Primal solution
        primal_solution = {var.name: p.value(var) for var in xs.values()}
        primal_value = p.value(Lp_prob.objective)

        # Display Results
        result_message = f"Solution\n"
        for var, value in primal_solution.items():
            result_message += f"{var} = {value}\n"
        result_message += f"Objective Value: {primal_value}\n"

        messagebox.showinfo("Solution", result_message)
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid input for the problem.")

#window 1

#drop down box
my_img= ImageTk.PhotoImage(Image.open("C_Logo.png"))
logo=Label(image=my_img)
logo.grid(row=0, column=1)

dropL=Label(root, text="Created by Noah Jones")
dropL.grid(row=0, column=0)

dropL=Label(root, text="What type of problem?")
dropL.grid(row=1, column=0)

clicked=StringVar()
clicked.set("Maximize")
drop=OptionMenu(root, clicked, "Maximize","Minimize")
drop.grid(row=1, column=1)

#entry fields
e1=Entry(root)
e1.grid(row=3, column=0,)

e2=Entry(root)
e2.grid(row=3, column=1, padx=10, pady=10)

#labels
e1L=Label(root, text="How many variables?")
e1L.grid(row=2, column=0)

e2L=Label(root, text="How many constraints?")
e2L.grid(row=2, column=1)

#button
create_button=Button(root, text="Create Problem", command=create_problem)
create_button.grid(row=4, column=0)

help_button=Button(root, text="Help Page", command=help_page)
help_button.grid(row=4, column=1)
#end of window 1

root.mainloop()  
# help from tkinter video seiries from codemy
#and help with fixing bugs from Chat GPT