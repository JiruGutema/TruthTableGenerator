def truthtable():
    print("--> Enter help for Help!")
    expression = input("please enter expression: ")
    if expression != "help":
        x = 0
        var2 = expression.split(" ")
        for i in var2:
            if len(i) == 1:
                x += 1
        if x == 1:
            print("A", " | ", "negation")
            print("-------")
        elif x == 2:
            print("A", "|", "B", "| ", expression)
            print("----------")
        elif x == 3:
            print("A", "|", "B", "|", "C", "| ", expression)
            print("----------")
        else:
            print("A", "|", "B", "|", "C", "|", "D", "| ", expression)
            print("----------")

        min_term = []  # List to store the minimum terms
        max_term = []  # List to store the maximum terms

        for A in range(2):
            if x == 1:
                result = int(eval(expression))
                print(A, " | ", result)
                if result == 1:
                    min_term.append(f"{'A' if A==1 else 'A̅'}")
                else:
                    max_term.append(f"{'A' if A == 0 else 'A̅'}")
            else:
                for B in range(2):
                    if x == 2:
                        result = int(eval(expression))
                        print(A, "|", B, "|", result)
                        if result == 1:
                            min_term.append(f"{'A' if A == 1 else 'A̅'} {'B' if B == 1 else 'B̅'}")
                        else:
                            max_term.append(f"{'A' if A == 0 else 'A̅'}+{'B' if B == 0 else 'B̅'}")
                    else:
                        for C in range(2):
                            if x == 3:
                                result = int(eval(expression))
                                print(A, "|", B, "|", C, "|", result)
                                if result == 1:
                                    min_term.append(f"{'A' if A == 1 else 'A̅'}{'B' if B == 1 else 'B̅'}{'C' if C == 1 else 'C̅'}")
                                else:
                                    max_term.append(f"{'A' if A == 0 else 'A'}+{'B' if B == 0 else 'B̅'}+{'C' if C == 0 else 'C̅'}")
                            else:
                                for D in range(2):
                                    result = int(eval(expression))
                                    print(A, "|", B, "|", C, "|", D, "|", result)
                                    if result == 1:
                                        min_term.append(f"{'A' if A == 1 else 'A̅'}{'B' if B == 1 else 'B̅'}{'C' if C == 1 else 'C̅'}{'D' if D == 1 else 'D̅'}")
                                    else:
                                        max_term.append(f"{'A' if A == 0 else 'A̅'}+{'B' if B == 0 else 'B̅'}+{'C' if C == 0 else 'C̅'}+{'D' if D == 0 else 'D̅'}")

        print("\nMinimum Term: ", " + ".join(min_term))
        #print(min_term)
        print("Maximum Term: ", " * ".join(max_term))
    else:
        print("""1. Use 'and' for and. \n2. Use 'or' for Or\n3. use '>>' for implication'\n4. Use 'not' for negation\n5. Use '^' exclusive or\n6. use the variables from ABCD\n7. use (A==B) and (B == A) for bi implication.\n8. the expression only supports up to 4 Statements\n9.ex. A and B or C """)
truthtable()
