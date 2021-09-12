screens = ['entrance']
curent = 'entrance'
back = ''
while True:
    choice = input('enter choice')
    lenth = screens.__len__() - 1
    print(lenth)
    print(f'current = {screens[lenth]}')
    print(f'screens{screens}')
    if choice == 's':
        scrn = input("screen name")
        screens.append(scrn)
        lengh = len(screens) - 1
        curent = screens[lengh]
    else:
        if len(screens) != 0:
            lent = screens.__len__() - 1
            last = screens[lent]
            screens.remove(last)


