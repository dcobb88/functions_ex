def rent_calculator(rent, electric, roommates):
    portion = (rent + electric) / roommates
    return portion










def main():
    rent = 800
    electric = 200
    roommates = 4
    portion = rent_calculator(rent, electric, roommates)

    print(f"Each person needs to pay ${portion} for rent and electric for this month.")

main ()