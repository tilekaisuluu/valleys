def counting_valleys(steps):
    valley = 0
    sea_level = 0
    for i in steps:
        if i == 'U':
            sea_level += 1
            if sea_level == 0:
                valley += 1
        else:
            sea_level -= 1
    print(valley, "valley")








steps = list(input("Enter U or D:"))
counting_valleys(steps)
