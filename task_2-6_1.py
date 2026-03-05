
pH = float(input("\nВведите значение pH: "))

if pH < 7:
    print("\n\tКислая среда")
elif pH == 7:
    print("\n\tНейтральная среда")
else:
    print("\n\tЩелочная среда")