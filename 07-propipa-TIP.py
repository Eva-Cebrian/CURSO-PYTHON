print("Wellcome to the TIP calculator!")
total_Bill = float(input("Write total bill: "))
tip = int((input("Write the tip: 10, 12 or 15%: ")))
people = int(input("How many people split the bill: "))
tip = (((total_Bill*tip)/100)+total_Bill)/people
tip_con_dos_decimales = round(tip, 2)
print(f"La propina es {tip_con_dos_decimales}$")
