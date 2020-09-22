from sympy import *
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)
expr = 0
var = 0

def sym(expr, var):
    '''Algebra helper when tough times are ahead'''

    if not expr:
        expr = input("Enter equation to solve:\n")
        var = input("What variable you wanna solve for?\n")

    choice = input("What would you like to do with "+expr+"?\n[0]Find x intercepts\n[1]Find y intercept\n[2]Expand\n[3]Factor\n[4]Plot equation\n")
    if choice == "0":
        print("\nFinding x...")
        print(solve(expr, var))
    elif choice == "1":
        print("\nFinding y...")
        yexpr = expr.replace(var, '0')
        print("y = "+yexpr+" = "+str(N(yexpr)))
    elif choice == "2":
        print("\nExpanding...")
        print(expand(expr))
    elif choice == "3":
        print("\nFactoring...")
        print(factor(expr))
    elif choice == "4":
        print("\nGenerating graph...")
        plot(expr, ylim=(-40,40))

    choice = input("\nWhat you wanna do now?\n[0]Quit\n[1]Reset\n[2]Continue\n")
    if choice == "1":
        sym(0,0)
    elif choice == "0":
        print("Goodbye!")
        quit()
    elif choice == "2":
        sym(expr, var)
    else:
        print("Wrong choice..")
        pass
              
if __name__ == "__main__":
    sym(expr, var)
