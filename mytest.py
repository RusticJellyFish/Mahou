for w in range(10):
    row = ""
    for h in range(10):
        if w == 0 or h == 0 or w == 9 or h == 9:
            row += "#"
        else:
            row += "."
        if w < 10:
            row += " "
    print(row)

