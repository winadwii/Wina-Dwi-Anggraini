gender = input("jenis kelamin (Pria/Wanita): ").lower()
tinggi = int(input("tinggi badan(cm): "))
berat = int(input("berat badan(kg): "))

if gender == "Pria":
    P_ideal = (tinggi - 100) - ((tinggi - 100) * (10/100))
    print(f"berat badan ideal kamu {P_ideal} kg")
    print(f"yok bisa yok kurangi {berat - P_ideal} kg lagi")

elif gender == "wanita": 
    w_ideal = (tinggi - 100) - ((tinggi - 100) * (15/100))
    print(f"berat badan ideal kamu {w_ideal} kg")
    print(f"yok bisa yok kurangi {berat - w_ideal} kg lagi")

else:
    print("invalid")