def arithmetic_arranger(problems, show_answers=False):
    # Error: Too many problems.
    if len(problems) > 5:
        return 'Error: Too many problems.'

    topa = []
    bota = []
    dasha = []

    ansa = []

    for index in problems:
        problem = index.split()
        a = problem[0]
        op = problem[1]
        b = problem[2]
        # Error: Operator must be '+' or '-'
        if op not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # Error: Numbers must only contain digits
        if not (a.isdigit() and b.isdigit()):
            return 'Error: Numbers must only contain digits.'

        # Error: Numbers cannot be more than four digits
        if len(a) > 4 or len(b) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        if len(a) > len(b):
            width = int(len(a)) + 2
        else:
            width = int(len(b)) + 2

        topd = "-" * width
        tops = " " * (width - int(len(a))) + a
        bottoms = op + " " * ((width - int(len(b))) - 1) + b

        if op == "+":
            ans = int(a) + int(b)
        else:
            ans = int(a) - int(b)

        anss = " " * (width - len(str(ans))) + str(ans)

        topa.append(tops)
        bota.append(bottoms)
        dasha.append(topd)
        ansa.append(anss)

        topd = bottoms = tops = anss = ""

    f = "    ".join(topa)
    s = "    ".join(bota)
    d = "    ".join(dasha)
    an = "    ".join(ansa)
    if show_answers:
        problems = f + "\n" + s + "\n" + d + "\n" + an
    else:
        problems = f + "\n" + s + "\n" + d

    return problems


print(arithmetic_arranger(["3801 - 2", "123 + 49"], True))
