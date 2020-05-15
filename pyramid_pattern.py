# Pyramid pattern!!!
for i in range(1, 6):
    sp = ""
    pj = 0
    pl = 0
    for k in range(6, i, -1):
        sp += " "
    for j in range(1, i+1):
        pj = (pj * 10) + j
    for l in range(i-1, 0, -1):
        pl = (pl * 10) + l
    if pl < 1:
        pl = ""
    print(f"{sp}{pj}{pl}")
