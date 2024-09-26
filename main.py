from src import classes
from src import mruv
from src import mru


def mruv_call():
    print("""\n
    |===============: MRUV :===============|
    <><><><><><><><><><><><>><><><><><><><>
    ╔═════════════════════════════════════╗
    ║   Variable Name ---------- Index    ║
    ╠═════════════════════════════════════╣ 
    ║   Final Velocity ----------- VF      ║
    ║   Initial Velocity --------- VI      ║
    ║   Acceleration ------------- A       ║
    ║   Time --------------------- T       ║
    ║   Distance ----------------- X       ║
    ╚═════════════════════════════════════╝\n
    """)

    vF = classes.Variable("Final Velocity", False, None, "VF")
    vI = classes.Variable("Initial Velocity", False, None, "VI")
    a = classes.Variable("Acceleration", False, None, "A")
    t = classes.Variable("Time", False, None, "T")
    x = classes.Variable("Distance", False, None, "X")

    variable_list_mruv = [vF, vI, a, t, x]
    short_name_list_mruv = [var.short_name for var in variable_list_mruv]

    while True:
        index = input("Enter the variable index: ").upper()
        if index in short_name_list_mruv:
            break
        print("Please enter a valid index.")

    for variable in variable_list_mruv:
        if index != variable.short_name: 
            response = input(f"\nDo you have the value for {variable.name}? Yes or No: ").upper()
            if response in ["YES", "SI", "SÍ", "ASIES"]:
                variable.state = True
                while True:
                    try:
                        variable.value = float(input(f"Enter the value of {variable.name}: "))
                        break
                    except ValueError:
                        print("\nPlease enter a valid number.")

    if not classes.is_solvable(variable_list_mruv):
        print("This problem cannot be solved.")
    else:
        result, formula = mruv.solve_missing_variable_mruv(index, variable_list_mruv)
        print(f"""\n
        ╔═══════════════════════════════════════════════════╗ 
        ║                    RESULT                         ║
        ╠═══════════════════════════════════════════════════╣
        ║ The value of the variable <{index}> is: {result}  ║
        ╠═══════════════════════════════════════════════════╣
        ║ The formula used was: {formula}                   ║
        ╚v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v╝\n
        """)

def mru_call():
    print("""\n
    |===============: MRU :===============|
    <><><><><><><><><><><><>><><><><><><><>
    ╔═════════════════════════════════════╗
    ║   Variable Name ---------- Index    ║
    ╠═════════════════════════════════════╣
    ║   Velocity ----------------- V      ║
    ║   Time --------------------- T      ║
    ║   Distance ----------------- X      ║
    ╚═════════════════════════════════════╝\n
    """)

    v = classes.Variable("Velocity", False, None, "V")
    t = classes.Variable("Time", False, None, "T")
    x = classes.Variable("Distance", False, None, "X")

    variable_list = [v, t, x]
    short_name_list = [var.short_name for var in variable_list]

    while True:
        index = input("Enter the variable index: ").upper()
        if index in short_name_list:
            break
        print("Please enter a valid index.")

    for variable in variable_list:
        if index != variable.short_name: 
            response = input(f"\nDo you have the value for {variable.name}? Yes or No: ").upper()
            if response in ["YES", "SI", "SÍ", "ASIES"]:
                variable.state = True
                while True:
                    try:
                        variable.value = float(input(f"Enter the value of {variable.name}: "))
                        break
                    except ValueError:
                        print("\nPlease enter a valid number.")

    if not classes.is_solvable_MRU(variable_list):
        print("This problem cannot be solved.")
    else:
        result, formula = mru.solve_missing_variable_mru(index, variable_list)
        print(f"""\n
        ╔═══════════════════════════════════════════════════╗ 
        ║                    RESULT                         ║
        ╠═══════════════════════════════════════════════════╣
        ║ The value of the variable <{index}> is: {result}  ║
        ╠═══════════════════════════════════════════════════╣
        ║ The formula used was: {formula}                   ║
        ╚v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v╝\n
        """)

def print_header():
    print("\n" + "\n".join(["" for _ in range(3)]))
    print("  ____  _     _           _ _ __  __  ____ ")
    print(" / ___|| |__ (_)_ __     (_(_)  \\/  |/ ___|")
    print(" \\___ \\| '_ \\| | '_ \\ _  | | | |\\/| | |    ")
    print("  ___) | | | | | | | | |_| | | |  | | |___ ")
    print(" |____/|_| |_|_|_| |_|_____|_|_|  |_|\\____|")
    print("\n" + "\n".join(["" for _ in range(2)]))


def main():
    print_header()

    while True:
        try:
            print("""
            |===============: PHYSICS CALCULATOR :===============|
            |                1. Uniformly Rectilinear Motion (MRU)  |
            |                2. Uniformly Accelerated Rectilinear Motion (MRUV) |
            |                3. Exit                                |
            |========================================================|
            """)
            option = input("Select an option: ")

            if option == '1':
                print("You have selected MRU.")
                mru_call()  
            elif option == '2':
                print("You have selected MRUV.")
                mruv_call() 
            elif option == '3':
                print("Exiting the program...")
                break  
            else:
                print("Invalid option, please try again.")

        except Exception as e:
            print(f"An error occurred: {e}")
            break 

if __name__ == "__main__":
    main()
