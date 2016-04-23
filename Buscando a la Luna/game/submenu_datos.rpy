﻿
label submenu_datos:
    init python:
        import datetime
        import time
        Y, M, D, H, MIN, SEC, DOW, DOY, DST = time.localtime()
        base_lunanueva = datetime.datetime(year=2016, month=4, day=7)
        tiempo_ahora = datetime.datetime(year=Y, month=M, day=D)
        diff =  tiempo_ahora - base_lunanueva
        dias = (((diff.total_seconds() / 60) / 60) / 24) % 28
    
    scene fondonegro

    if dias < 3.5:
        # luna nueva , no pic (lunanueva es todo negro)
        # no tiene luz, queda oscuro
        show lunanueva at truecenter
        with dissolve
        "Hoy, día %(D)d/%(M)d/%(Y)d, el estado de la luna es:\n\n{b}Luna nueva{/b}\nEdad de la luna: {i}%(dias)d días{/i}"
    elif dias < 7:
        # luna nueva visible , 22
        show 22 at truecenter
        with dissolve
        "Hoy, día %(D)d/%(M)d/%(Y)d, el estado de la luna es:\n\n{b}Luna nueva visible{/b}\nEdad de la luna: {i}%(dias)d días{/i}"
    elif dias < 10.5:
        # cuarto creciente , 19
        show 19 at truecenter
        with dissolve
        "Hoy, día %(D)d/%(M)d/%(Y)d, el estado de la luna es:\n\n{b}Luna creciente{/b}\nEdad de la luna: {i}%(dias)d días{/i}"
    elif dias < 14:
        # luna gibosa creciente , 16
        show 16 at truecenter
        with dissolve
        "Hoy, día %(D)d/%(M)d/%(Y)d, el estado de la luna es:\n\n{b}Luna gibosa creciente{/b}\nEdad de la luna: {i}%(dias)d días{/i}"
    elif dias < 17.5:
        # luna llena , 12
        show 12 at truecenter
        with dissolve
        "Hoy, día %(D)d/%(M)d/%(Y)d, el estado de la luna es:\n\n{b}Luna llena{/b}\nEdad de la luna: {i}%(dias)d días{/i}"
    elif dias < 21:
        # luna gibosa menguante , 8
        show 8 at truecenter
        with dissolve
        "Hoy, día %(D)d/%(M)d/%(Y)d, el estado de la luna es:\n\n{b}Luna gibosa menguante{/b}\nEdad de la luna: {i}%(dias)d días{/i}"
    elif dias < 24.5:
        # cuarto menguante , 5
        show 5 at truecenter
        with dissolve
        "Hoy, día %(D)d/%(M)d/%(Y)d, el estado de la luna es:\n\n{b}Cuarto menguante{/b}\nEdad de la luna: {i}%(dias)d días{/i}"
    else:
        # luna menguante , 2
        show 2 at truecenter
        with dissolve
        "Hoy, día %(D)d/%(M)d/%(Y)d, el estado de la luna es:\n\n{b}Luna menguante{/b}\nEdad de la luna: {i}%(dias)d días{/i}"

    return
