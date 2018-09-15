def code(w):
    w= str(w)
    rr = w[1:3]
    yy = w[3:5]
    xx = w[5:7]
    r =0
    y = 0
    x = 0
    if len(w) == 7:
        if rr[0] == "0" and yy[0] == "0" and xx[0] == "0":
            r = rr[1]
            y = yy[1]
            x = xx[1]
        elif rr[0] != "0" and yy[0] == "0" and xx[0] == "0":
            r = rr
            y = yy[1]
            x = xx[1]
        elif rr[0] == "0" and yy[0] != "0" and xx[0] == "0":
            r = rr[1]
            y = yy
            x = xx[1]
        elif rr[0] == "0" and yy[0] == "0" and xx[0] != "0":
            r = rr[1]
            y = yy[1]
            x = xx
        elif rr[0] != "0" and yy[0] != "0" and xx[0] == "0":
            r = rr
            y = yy
            x = xx[1]
        elif rr[0] != "0" and yy[0] == "0" and xx[0] != "0":
            r = rr
            y = yy[1]
            x = xx
        elif rr[0] == "0" and yy[0] != "0" and xx[0] != "0":
            r = rr[1]
            y = yy
            x = xx
        elif rr[0] != "0" and yy[0] != "0" and xx[0] != "0":
            r = rr
            y = yy
            x = xx




