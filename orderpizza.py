print("------------------------------------")
print("----Selamat Datang di Pizza Hut-----")
print("----Silahkan Pilih Topping Anda-----")
print("------------Menu Topping------------")
print("-->        Frankfurter BBQ       <--")
print("-->          Meat Monsta         <--")
print("-->         Super Supreme        <--")
print("-->     Super Supreme Chicken    <--")
print("------------------------------------")
#pseudocode
#pelanggan memilih topping terlebih dahulu


#ToppingPizza
ToppingPizza = str(input("Masukkan Pilihan Topping Anda: "))
if ToppingPizza == "Frankfurter BBQ" :
    print("Harga Pizza Rp.3000 ")
    harga_tiopping_pizza = 3000
elif ToppingPizza == "Meat Monsta" :
    print("Harga Pizza Rp.4000 ")
    harga_topping_pizza = 4000
elif ToppingPizza == "Super Supreme" :
    print("Harga Pizza Rp.5000 ")
    harga_topping_pizza = 5000
elif ToppingPizza == "Super Supreme Chicken" :
    print("Harga Pizza Rp.5500 ")
    harga_topping_pizza = 5500
else :
    print("Maaf Topping Tidak Tersedia dalam daftar ")


#pilihan crust
print("------------------------------------")
print("-------------Menu Crust-------------")
print("-->             Pan              <--")
print("-->      StuffedCrust Cheese     <--")
print("-->      StuffedCrust Sausage    <--")
print("-->         Cheese Bites         <--")
print("-->          Crown Crust         <--")
print("------------------------------------")

CrustPizza = str(input("Masukkan Pilihan Crust Anda: "))
if CrustPizza == "Pan" :
    print("Harga Crust Rp.0")
    harga_crust_pizza = 0
elif CrustPizza == "StuffedCrust Cheese" :
    print("Harga Crust Rp.2000")
    harga_crust_pizza = 2000
elif CrustPizza == "StuffedCrust Sausage " :
    print("Harga Crust Rp.1500")
    harga_crust_pizza = 1500
elif CrustPizza == "Cheese Bites" :
    print("Harga Crust Rp.3000")
    harga_crust_pizza = 3000
elif CrustPizza == "Crown Crust" :
    print("Harga Crust Rp.2000")
    harga_crust_pizza = 2000
else:
    print("Maaf Crust Tidak Tersedia dalam Daftar ")
