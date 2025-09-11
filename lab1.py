import sys

def get_coef(index, prompt):
    try:
        coef_str = sys.argv[index]
        coef = float(coef_str)
        return coef
    except:
        while True:
            coef_str = input(prompt)
            if coef_str.isdigit() or (coef_str.startswith('-') and coef_str[1:].isdigit()):
                coef = float(coef_str)
                return coef
            else:
                print("Введите число!")

def calculate_roots(a, b, c):
    square_roots = []
    roots = [True]

    D = b**2 - 4*a*c

    if (a == 0):
        square_root = -c/b
        if (square_root < 0):
            roots[0] = False
        elif (square_root == 0):
            roots.append(0)
        else:
            root1 = square_root**0.5
            root2 = -square_root**0.5
            roots.append(root1)
            roots.append(root2)
            return roots

    if (D < 0):
        roots[0] = False
    else:
        t1 = (-b + D**0.5) / (2*a)
        t2 = (-b - D**0.5) / (2*a)
        square_roots.append(t1)
        square_roots.append(t2)

        for t in square_roots:
            if (t == 0):
                roots.append(0)
            elif (t > 0):
                root1 = t**0.5
                root2 = -t**0.5
                roots.append(root1)
                roots.append(root2)
    return roots

def main():
    a = get_coef(1, "Введите кэффициент A: ")
    b = get_coef(2, "Введите кэффициент B: ")
    c = get_coef(3, "Введите кэффициент C: ")
    print()

    roots = calculate_roots(a, b, c)
    if (roots[0] == True):
        for i in range(1, len(roots)):
            print(f"x {i} = ", roots[i])
    else:
        print("Нет действительных корней!")

if __name__ == "__main__":
    main()
