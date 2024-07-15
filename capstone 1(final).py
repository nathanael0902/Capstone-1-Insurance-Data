import math
from tabulate import tabulate

# Variables
insured_data = {
    1001 : {'name' : 'Juan', 'gender' : 'M', 'smoking' : 'Y', 'age' : 24, 'ins_code' : 1, 'ins_type' : 'Basic Life', 'SI' : 1000000000, 'premium' : 0},
    1002 : {'name' : 'Juanita', 'gender' : 'F', 'smoking' : 'N', 'age' : 48, 'ins_code' : 2, 'ins_type' : 'Pro Life', 'SI' : 2500000000, 'premium' : 0},
    1003 : {'name' : 'Anton', 'gender' : 'M', 'smoking' : 'Y', 'age' : 34, 'ins_code' : 2, 'ins_type' : 'Pro Life', 'SI' : 2500000000, 'premium' : 0},
    1004 : {'name' : 'Jessica', 'gender' : 'F', 'smoking' : 'N', 'age' : 65, 'ins_code' : 3, 'ins_type' : 'Pro Max Life', 'SI' : 4000000000, 'premium' : 0},
    1005 : {'name' : 'Sarah', 'gender' : 'F', 'smoking' : 'Y', 'age' : 22, 'ins_code' : 3, 'ins_type' : 'Pro Max Life', 'SI' : 3500000000, 'premium' : 0},
    1006 : {'name' : 'Jeff', 'gender' : 'M', 'smoking' : 'N', 'age' : 36, 'ins_code' : 2, 'ins_type' : 'Pro Life', 'SI' : 2500000000, 'premium' : 0},
    1007 : {'name' : 'Jack', 'gender' : 'M', 'smoking' : 'N', 'age' : 35, 'ins_code' : 4, 'ins_type' : 'Endowment Plan', 'SI' : 2500000000, 'premium' : 0},
    1008 : {'name' : 'Paijo', 'gender' : 'M', 'smoking' : 'Y', 'age' : 33, 'ins_code' : 1, 'ins_type' : 'Basic Life', 'SI' : 2000000000, 'premium' : 0},
    1009 : {'name' : 'Painem', 'gender' : 'F', 'smoking' : 'N', 'age' : 45, 'ins_code' : 2, 'ins_type' : 'Pro Life', 'SI' : 3000000000, 'premium' : 0},
    1010 : {'name' : 'Una', 'gender' : 'F', 'smoking' : 'N', 'age' : 42, 'ins_code' : 4, 'ins_type' : 'Endowment Plan', 'SI' : 3000000000, 'premium' : 0},
    # 1011 : {'name' : 'Sutanto', 'gender' : 'F', 'smoking' : 'Y', 'age' : 43, 'ins_code' : 1, 'ins_type' : 'Basic Life', 'SI' : 1500000000, 'premium' : 0},
    # 1012 : {'name' : 'Sugito', 'gender' : 'M', 'smoking' : 'N', 'age' : 57, 'ins_code' : 3, 'ins_type' : 'Pro Max Life', 'SI' : 3500000000, 'premium' : 0},
    # 1013 : {'name' : 'Triwarto', 'gender' : 'M', 'smoking' : 'Y', 'age' : 38, 'ins_code' : 3, 'ins_type' : 'Pro Max Life', 'SI' : 3500000000, 'premium' : 0},
    # 1014 : {'name' : 'Evelyn', 'gender' : 'F', 'smoking' : 'N', 'age' : 26, 'ins_code' : 4, 'ins_type' : 'Endowment Plan', 'SI' : 4000000000, 'premium' : 0},
    # 1015 : {'name' : 'Rosalyn', 'gender' : 'F', 'smoking' : 'Y', 'age' : 18, 'ins_code' : 1, 'ins_type' : 'Basic Life', 'SI' : 1000000000, 'premium' : 0},
    # 1016 : {'name' : 'I Gede Putut', 'gender' : 'M', 'smoking' : 'N', 'age' : 34, 'ins_code' : 2, 'ins_type' : 'Pro Life', 'SI' : 2500000000, 'premium' : 0},
    # 1017 : {'name' : 'Supri', 'gender' : 'M', 'smoking' : 'Y', 'age' : 38, 'ins_code' : 4, 'ins_type' : 'Endowment Plan', 'SI' : 3000000000, 'premium' : 0},
    # 1018 : {'name' : 'Riyadi', 'gender' : 'M', 'smoking' : 'N', 'age' : 53, 'ins_code' : 1, 'ins_type' : 'Basic Life', 'SI' : 1000000000, 'premium' : 0},
    # 1019 : {'name' : 'Siti', 'gender' : 'F', 'smoking' : 'Y', 'age' : 60, 'ins_code' : 2, 'ins_type' : 'Pro Life', 'SI' : 500000000, 'premium' : 0},
    # 1020 : {'name' : 'Alfonzo', 'gender' : 'M', 'smoking' : 'N', 'age' : 49, 'ins_code' : 2, 'ins_type' : 'Pro Life', 'SI' : 2000000000, 'premium' : 0}
}


tipe_asuransi = {1 : "Basic Life", 2 : "Pro Life", 3 : "Pro Max Life", 4 : "Endowment Plan"}
premi_tipe = {1:0.01, 2 : 0.015, 3 : 0.02, 4 : 0.015}


# Function

def calc():
    for x in insured_data:
        insured_data[x]['ins_type'] = tipe_asuransi[insured_data[x]['ins_code']]

        if insured_data[x]['gender'] == 'F': # Premi Gender
            premi_gender = 0.8
        else:
            premi_gender = 1 

        if insured_data[x]['smoking'] == "Y": # Premi Smoking
            premi_smoking = 1.2
        else:
            premi_smoking = 1
        
        if 'endowment' not in insured_data[x]['ins_type'].lower(): # Premi Endow & Faktor Umur
            premi_endow1 = 0
            faktor_umur_endow = 0

            if insured_data[x]['age'] >= 17 and insured_data[x]['age'] <= 30 : # Faktor_Umur
                faktor_umur_as = 0.6
            elif insured_data[x]['age'] > 30 and insured_data[x]['age'] <= 45 :
                faktor_umur_as = 0.8
            elif insured_data[x]['age'] > 45 and insured_data[x]['age'] <= 60 :
                faktor_umur_as = 1
            else:
                faktor_umur_as = 1.2
        else:
            premi_endow1 =  0.7 * insured_data[x]['SI']/(((1.05 ** (65-insured_data[x]['age']))-1)/0.05)

            if insured_data[x]['age'] >= 17 and insured_data[x]['age'] <= 30 : # Faktor_Umur
                faktor_umur_as = 0.5
                faktor_umur_endow = 0.35
            elif insured_data[x]['age'] > 30 and insured_data[x]['age'] <= 45 :
                faktor_umur_as = 0.7
                faktor_umur_endow = 0.5
            elif insured_data[x]['age'] > 45 and insured_data[x]['age'] <= 60 :
                faktor_umur_as = 0.9
                faktor_umur_endow = 0.7
            else:
                faktor_umur_as = 1.2
                faktor_umur_endow = 0.9

        premi_total = insured_data[x]['SI'] * premi_tipe[insured_data[x]['ins_code']] * premi_gender * premi_smoking * faktor_umur_as + premi_endow1 * faktor_umur_endow
        insured_data[x]['premium'] = premi_total

def calc_temp():
    for x in insured_data_temp: 
        insured_data_temp[x]['ins_type'] = tipe_asuransi[insured_data_temp[x]['ins_code']]

        if insured_data_temp[x]['gender'] == 'F': # Premi_Gender
            premi_gender = 0.8
        else:
            premi_gender = 1 

        if insured_data_temp[x]['smoking'] == "Y": # Premi Smoking
            premi_smoking = 1.2
        else:
            premi_smoking = 1
        
        if 'endowment' not in insured_data_temp[x]['ins_type'].lower(): # Premi Endow & Faktor Umur
            premi_endow1 = 0
            faktor_umur_endow = 0

            if insured_data_temp[x]['age'] >= 17 and insured_data_temp[x]['age'] <= 30 : # Faktor_Umur
                faktor_umur_as = 0.6
            elif insured_data_temp[x]['age'] > 30 and insured_data_temp[x]['age'] <= 45 :
                faktor_umur_as = 0.8
            elif insured_data_temp[x]['age'] > 45 and insured_data_temp[x]['age'] <= 60 :
                faktor_umur_as = 1
            else:
                faktor_umur_as = 1.2
        else:
            premi_endow1 =  0.7 * insured_data_temp[x]['SI']/(((1.05 ** (65-insured_data_temp[x]['age']))-1)/0.05)

            if insured_data_temp[x]['age'] >= 17 and insured_data_temp[x]['age'] <= 30 : # Faktor_Umur
                faktor_umur_as = 0.5
                faktor_umur_endow = 0.35
            elif insured_data_temp[x]['age'] > 30 and insured_data_temp[x]['age'] <= 45 :
                faktor_umur_as = 0.7
                faktor_umur_endow = 0.5
            elif insured_data_temp[x]['age'] > 45 and insured_data_temp[x]['age'] <= 60 :
                faktor_umur_as = 0.9
                faktor_umur_endow = 0.7
            else:
                faktor_umur_as = 1.2
                faktor_umur_endow = 0.9

        premi_total = insured_data_temp[x]['SI'] * premi_tipe[insured_data_temp[x]['ins_code']] * premi_gender * premi_smoking * faktor_umur_as + premi_endow1 * faktor_umur_endow
        insured_data_temp[x]['premium'] = premi_total

def confirmation():
    global confirmation_input
    confirmation_input1 = input("Are you sure?(Y/N): ").lower()
    while confirmation_input1 not in ['yes', 'no', 'y', 'n', '1', '0']:
        print('Please input a yes or no')
        confirmation_input1 = input("Are you sure?(Y/N): ").lower()
    if confirmation_input1 in ['yes', 'y', '1']:
        confirmation_input = 'Y'
    else:
        confirmation_input = 'N'

def print_all_data():
    table_data = []
    premium_total = 0
    for uid, details in insured_data.items():
        table_data.append([uid, details['name'], details['gender'], details['smoking'], details['age'], details['ins_code'], details['ins_type'], details['SI'], int(math.floor(details['premium']))])
    print(tabulate(table_data, headers= ['UID', 'name', 'gender', 'smoking', 'age', 'code', 'insurance name', 'SI', 'premium'], tablefmt= 'grid'))
    for x in insured_data:
        premium_total += insured_data[x]['premium']
    print(f"Total Premium received per month: {math.floor(premium_total)}")

def print_1_data():
    while True:
        try:
            data_check1 = int(input("Input the ID: "))
            break
        except ValueError:
            print("Please input a number")
    try:
        table_data = []
        details = insured_data[data_check1]
        table_data.append([data_check1, details['name'], details['gender'], details['smoking'], details['age'], details['ins_code'], details['ins_type'], details['SI'], int(math.floor(details['premium']))])
        print(tabulate(table_data, headers= ['UID', 'name', 'gender', 'smoking', 'age', 'code', 'insurance name', 'SI', 'premium'], tablefmt= 'grid'))
    except KeyError:
        print("Data does not exist")

def add_data():
    global insured_data_temp
    print(f"Used keys: {list(insured_data.keys())}")
    list_key_available = []
    for y in range(1001,1100):
        if y not in list(insured_data.keys()):
            list_key_available.append(y)
        if len(list_key_available) == 4:
            break 
    print(f"Recommended keys: {list_key_available}")
    while True:
        try:
            add_key = int(input("Input the key number: "))
            break
        except ValueError:
            print("Please input numbers as the key")
    if add_key in list(insured_data.keys()):
        print('Key already exists')
    elif len(str(add_key)) != 4:
        print("Please input a key with 4 digits")
    else:
        print(f"Used key for data is {add_key}")
        add_name = input("Input the name of the insured: ").capitalize()

        add_gender1 = input("Input the gender of the insured(M/F): ").lower()
        while add_gender1 not in ['male', 'female', 'm', 'f']:
            print("Gender not available")
            add_gender1 = input("Please input the correct gender(M/F): ").lower()
        if add_gender1 in ['male', 'm']:
            add_gender2 = 'M'
        else:
            add_gender2 = 'F'
        
        add_smoking1 = input("Input if the insured is smoking or not(Y/N): ").lower()
        while add_smoking1 not in ['y', 'n', 'yes', 'no', '1',  '0']:
            print('Option not available')
            add_smoking1 = input("Please input if the insured is smoking or not(Y/N): ").lower()
        if add_smoking1 in ['yes', 'y', '1']:
            add_smoking2 = 'Y'
        else:
            add_smoking2 = 'N'

        while True:
            try:
                print("Available insurance type:")
                for x in tipe_asuransi:
                    print(f"{x}: {tipe_asuransi[x]}")
                add_inscode = int(input(f"Input the insurance code available: "))
                break
            except ValueError:
                print("Please input a number")
        while add_inscode < 1 or add_inscode > len(tipe_asuransi):
            print("Please input the available insurance code")
            while True:
                try:
                    print("Available insurance type:")
                    for x in tipe_asuransi:
                        print(f"{x}: {tipe_asuransi[x]}")
                    add_inscode = int(input(f"Input the insurance code available: "))
                    break
                except ValueError:
                    print("Please input a number")

        if 'endowment' in tipe_asuransi[add_inscode].lower():
            while True:
                try:
                    add_age = int(input("Input the age of the insured(17-55): "))
                    break
                except ValueError:
                    print("Please input a number")
            while add_age < 17 or add_age > 55:
                print('The available age for Endowment Plan is 17-55')
                while True:
                    try:
                        add_age = int(input("Input the age of the insured(17-55): "))
                        break
                    except ValueError:
                        print("Please input a number")
        else:
            while True:
                try:
                    add_age = int(input("Input the age of the insured(17-65): "))
                    break
                except ValueError:
                    print("Please input a number")
            while add_age < 17 or add_age > 65:
                print('The available age for the insurance plan is 17-65')
                while True:
                    try:
                        add_age = int(input("Input the age of the insured(17-65): "))
                        break
                    except ValueError:
                        print("Please input a number")
        
        while True:
            try:
                add_SI = int(input("Input the sum insured: "))
                break
            except ValueError:
                print("Please input a number")
        while add_SI < 500000000 or add_SI > 5000000000:
            print("Please input SI between 500,000,000 and 5,000,000,000")
            while True:
                try:
                    add_SI = int(input("Input the sum insured: "))
                    break
                except ValueError:
                    print("Please input a number")
        insured_data_temp = {add_key: {"name" : add_name, "gender" : add_gender2, "smoking" : add_smoking2, "age" : add_age, "ins_code" : add_inscode, "ins_type" : tipe_asuransi[add_inscode], "SI" : add_SI, "premium" : 0}}
        calc_temp()
        table_data = []
        for uid, details in insured_data_temp.items():
            table_data.append([uid, details['name'], details['gender'], details['smoking'], details['age'], details['ins_code'], details['ins_type'], details['SI'], int(math.floor(details['premium']))])

        print(tabulate(table_data, headers= ['UID', 'name', 'gender', 'smoking', 'age', 'code', 'insurance name', 'SI', 'premium'], tablefmt= 'grid'))
        print("Save the insured's data?")
        confirmation()
        if confirmation_input == "N":
            insured_data_temp.clear()
            table_data.clear()
        else:
            insured_data.update(insured_data_temp)
            print_all_data()
            insured_data_temp.clear()
            table_data.clear()

def continue_update():
    global continue_update_input
    calc_temp()
    table_data = []
    for uid, details in insured_data_temp.items():
        table_data.append([uid, details['name'], details['gender'], details['smoking'], details['age'], details['ins_code'], details['ins_type'], details['SI']])
    print(tabulate(table_data, headers= ['UID', 'name', 'gender', 'smoking', 'age', 'insurance code', 'insurance type', 'SI'], tablefmt= 'grid'))
    continue_update_input1 = input("Do you want to continue updating the details?(Y/N): ").lower()
    while continue_update_input1 not in ['yes', 'y', 'no', 'n', '1', '0']:
        print("Please input a yes or no")
        continue_update_input1 = input("Do you want to continue updating the details?(Y/N): ").lower()
    if continue_update_input1 in ['y','yes', '1']:
        continue_update_input = 'Y'
    else:
        continue_update_input = 'N'
       
def update_menu():
    global insured_data_temp
    global continue_update_input
    continue_update_input = "Y"
    print_all_data()
    while True:
        try:
            update_key = int(input("Input the ID that for the details to be changed: "))
            break
        except ValueError:
            print("Please input a number")
    if update_key not in list(insured_data.keys()):
        print("The data you are looking for does not exist")
    else:
        insured_data_temp = {update_key : insured_data[update_key]}

        while continue_update_input == "Y":
            table_data = []
            for uid, details in insured_data_temp.items():
                table_data.append([uid, details['name'], details['gender'], details['smoking'], details['age'], details['ins_code'], details['ins_type'], details['SI'], int(math.floor(details['premium']))])
            print(tabulate(table_data, headers= ['UID', 'name', 'gender', 'smoking', 'age', 'code', 'insurance name', 'SI', 'premium'], tablefmt= 'grid'))
            print("""
    Update Menu
    1. Name
    2. Gender
    3. Smoking
    4. Age
    5. Insurance Type
    6. Sum Insured              
            """)
            while True:
                try:
                    update_menu_input = int(input("Input the number for detail to be changed: "))
                    break
                except ValueError:
                    print("Please input a number")
            while update_menu_input < 1 or update_menu_input > 6:
                print("The menu does not exist")
                while True:
                    try:
                        update_menu_input = int(input("Input the number for detail to be changed: "))
                        break
                    except ValueError:
                        print("Please input a number")
            if update_menu_input == 1:
                new_name = input("Input the updated name of the insured: ").capitalize()
                insured_data_temp[update_key]['name'] = new_name
                continue_update()
            if update_menu_input == 2:
                new_gender1 = input("Input the new gender of the insured(M/F): ").lower()
                while new_gender1 not in ['male', 'female', 'm', 'f']:
                    print("Gender not available")
                    new_gender1 = input("Please input the correct gender(M/F): ").lower()
                if new_gender1 in ['male', 'm']:
                    new_gender2 = 'M'
                else:
                    new_gender2 = 'F'
                insured_data_temp[update_key]['gender'] = new_gender2
                continue_update()
            if update_menu_input == 3:
                new_smoking1 = input("Input the new smoking status of the insured(Y/N): ").lower()
                while new_smoking1 not in ['yes', 'y', 'no', 'n', '1', '0']:
                    print("Please enter a yes or no")
                    new_smoking1 = input("Input the new smoking status of the insured(Y/N): ").lower()
                if new_smoking1 in ['yes', 'y', '1']:
                    new_smoking2 = 'Y'
                else:
                    new_smoking2 = 'N'
                insured_data_temp[update_key]['smoking'] = new_smoking2
                continue_update()
            if update_menu_input == 4:
                if 'endowment' in insured_data_temp[update_key]['ins_type'].lower() :
                    while True:
                        try:
                            new_age = int(input("Input the new age(17-55): "))
                            break
                        except ValueError:
                            print("Input a number")
                    while new_age < 17 or new_age > 55:
                        print("For endowment insured, available age is 17-55")
                        while True:
                            try:
                                new_age = int(input("Input the new age(17-55): "))
                                break
                            except ValueError:
                                print("Input a number")
                else:
                    while True:
                        try:
                            new_age = int(input("Input the new age(17-65): "))
                            break
                        except ValueError:
                            print("Input a number")
                    while new_age < 17 or new_age > 65:
                        print("The available age is 17-65")
                        while True:
                            try:
                                new_age = int(input("Input the new age(17-65): "))
                                break
                            except ValueError:
                                print("Input a number")
                insured_data_temp[update_key]['age'] = new_age
                continue_update()
            if update_menu_input == 5:
                if insured_data_temp[update_key]['age'] > 55:
                    print("The available insurance types are:")
                    tipe_asuransi_temp = {key: value for key, value in tipe_asuransi.items() if 'endowment' not in value.lower()}
                    for x in tipe_asuransi_temp:
                        print(f"{x}: {tipe_asuransi[x]}")
                    while True:
                        try:
                            new_code = int(input("Input the new insurance type code: "))
                            break
                        except ValueError:
                            print("Please input a number")
                    while new_code not in list(tipe_asuransi_temp.keys()):
                        print("The available insurance types are only on above choices")
                        while True:
                            try:
                                new_code = int(input("Input the new insurance type code: "))
                                break
                            except ValueError:
                                print("Please input a number")
                else:
                    print("The available insurance types are:")
                    for x in tipe_asuransi:
                        print(f"{x}: {tipe_asuransi[x]}")
                    while True:
                        try:
                            new_code = int(input("Input the new insurance type code: "))
                            break
                        except ValueError:
                            print("Please input a number")
                    while new_code not in list(tipe_asuransi.keys()):
                        print("The available insurance types are only on above choices")
                        while True:
                            try:
                                new_code = int(input("Input the new insurance type code: "))
                                break
                            except ValueError:
                                print("Please input a number")
                insured_data_temp[update_key]['ins_code'] = new_code
                insured_data_temp[update_key]['ins_type'] = tipe_asuransi[new_code]
                continue_update()
            if update_menu_input == 6:
                while True:
                    try:
                        new_SI = int(input("Input new sum insured: "))
                        break
                    except ValueError:
                        print("Please input a number")
                while new_SI < 500000000 or new_SI > 5000000000:
                    print("Sum Insured can only be between 500,000,000 and 5,000,000,000")
                    while True:
                        try:
                            new_SI = int(input("Input new sum insured: "))
                            break
                        except ValueError:
                            print("Please input a number")
                insured_data_temp[update_key]['SI'] = new_SI
                continue_update()
        calc_temp()
        table_data = []
        for uid, details in insured_data_temp.items():
            table_data.append([uid, details['name'], details['gender'], details['smoking'], details['age'], details['ins_code'], details['ins_type'], details['SI'], int(math.floor(details['premium']))])
        print()
        print(tabulate(table_data, headers= ['UID', 'name', 'gender', 'smoking', 'age', 'code', 'insurance name', 'SI', 'premium'], tablefmt= 'grid'))
        print("Save the changes?")
        confirmation()
        if confirmation_input == 'N':
            insured_data_temp.clear()
        else:
            insured_data.update(insured_data_temp)
            print('Data successfully updated')
            insured_data_temp.clear()

def delete_menu():
    global insured_data_temp
    global confirmation_input
    print_all_data()
    while True:
        try:
            delete_key = int(input("Input the ID of the data to be deleted: "))
            break
        except ValueError:
            print("Please input a number")
    if delete_key not in list(insured_data.keys()):
        print("The data you are looking for does not exist")
    else:
        insured_data_temp = {delete_key: insured_data[delete_key]}
        table_data = []
        for uid, details in insured_data_temp.items():
            table_data.append([uid, details['name'], details['gender'], details['smoking'], details['age'], details['ins_code'], details['ins_type'], details['SI'], int(math.floor(details['premium']))])
        print(tabulate(table_data, headers= ['UID', 'name', 'gender', 'smoking', 'age', 'code', 'insurance name', 'SI', 'premium'], tablefmt= 'grid'))
        print("Delete this data")
        confirmation()
        if confirmation_input == 'N':
            pass
        else:
            del insured_data[delete_key]
        insured_data_temp.clear()
        table_data.clear()

def ins_type_add():
    global confirmation_input
    global tipe_asuransi
    print("Already available insurance types:")
    tipe_asuransi = dict(sorted(tipe_asuransi.items()))
    for x in tipe_asuransi:
        print(f"{x}: {tipe_asuransi[x]}, {premi_tipe[x]*100}% of SI")
    print("For endowment is normal life insurance + 50% of sum insured to be returned at retirement age of 65")
    while True:
        try:
            print(f"Insurance type keys already used: {list(tipe_asuransi.keys())}")
            type_add_key = int(input("Input the key of the new insurance type: "))
            break
        except ValueError:
            print("Please input a number")
    if type_add_key in list(tipe_asuransi.keys()):
        print("Key already exists")
    else:
        print(f"Used key for insurance type is {type_add_key}")
        type_name = input("Input the insurance type name: ")
        if type_name in list(tipe_asuransi.values()):
            print("Insurance type already exists")
        else:
            pass
        while True:
            try:
                print("The percentage must be below 5%")
                type_SI = float(input("Input the % of SI to be used in calculation: "))
                break
            except ValueError:
                print("Please input a number")
        while type_SI <= 0 or type_SI > 5:
            print("The percentage must be between 0 - 5")
            while True:
                try:
                    print("The percentage must be below 5%")
                    type_SI = float(input("Input the % of SI to be used in calculation: "))
                    break
                except ValueError:
                    print("Please input a number")
        ins_type_temp = {type_add_key : type_name}
        premium_type_temp = {type_add_key : round((type_SI / 100), 3)}
        print(f"""
    New Insurance type:
        {type_add_key}: {type_name}, {float(type_SI)}% of the sum insured
    """)
        print('Save to data?')
        confirmation()
        if confirmation_input == 'N':
            ins_type_temp.clear()
            premium_type_temp.clear()
        else:
            tipe_asuransi.update(ins_type_temp)
            premi_tipe.update(premium_type_temp)
            ins_type_temp.clear()
            premium_type_temp.clear()

def ins_type_update():
    global confirmation_input
    while True:
        try:
            print("""Available option for change
    1. Name of the insurance type
    2. percentage of sum insured for calculation
            """)
            update_menu_input = int(input("Input the number for detail to be changed: "))
            break
        except ValueError:
            print("Please input a number")
    if update_menu_input not in [1,2]:
        print("Option not available")
    else:
        print("Available insurance types to be updated:")
        for x in tipe_asuransi:
            print(f"{x}: {tipe_asuransi[x]}, {premi_tipe[x]*100}% of SI")
        while True:
            try:
                update_key = int(input("Input the key for insurance type to be updated: "))
                break
            except ValueError:
                print("Please input a number")
        if update_key not in list(tipe_asuransi.keys()):
            print("The selected insurance type key does not exist")
        else:
            if update_menu_input == 1:
                update_name = input("Input the new name of the insurance type: ")
                print(f"The updated insurance type will be {update_key}: {update_name}, {premi_tipe[update_key]*100}% of SI")
                print("Save the data?")
                confirmation()
                if confirmation_input == 'N':
                    pass
                else:
                    tipe_asuransi[update_key] = update_name
            else:
                while True:
                    try:
                        update_SI = float(input("Input the new percentage of SI used: "))
                        break
                    except ValueError:
                        print("Please input a number")
                if update_SI < 0 or update_SI > 5:
                    print("Percentage must be above 0 and under 5")
                else:
                    print(f"The updated insurance type will be {update_key}: {tipe_asuransi[x]}, {update_SI}% of SI")
                    print("Save the data?")
                    confirmation()
                    if confirmation_input == 'N':
                        pass
                    else:
                        premi_tipe[update_key] = (update_SI / 100)

def ins_type_del():
    global confirmation_input
    type_del_list = []
    type_del_dict = {}
    for y in insured_data:
        type_del_list.append(insured_data[y]['ins_code'])
    for x in tipe_asuransi:
        if x in type_del_list:
            type_del_dict.update({x : f"{tipe_asuransi[x]} (has data)"})
        else:
            type_del_dict.update({x : f"{tipe_asuransi[x]} (can be deleted)"})
    print("Insurance types:")
    for a in type_del_dict:
        print(f"{a}: {type_del_dict[a]}")
    while True:
        try:
            type_del_key = int(input("Input the key to be deleted: "))
            break
        except ValueError:
            print("Please input a number")
    if type_del_key not in list(tipe_asuransi.keys()):
        print("Please input keys of available insurance types")
    else:
        if type_del_key in type_del_list:
            print("The insurance type cannot be deleted as it has data using it")
        else:
            print(f"Delete the insurance type {type_del_key}: {tipe_asuransi[type_del_key]}?")
            confirmation()
            if confirmation_input == 'N':
                pass
            else:
                del tipe_asuransi[type_del_key]

def sort_main():
    global insured_data
    global tipe_asuransi
    global premi_tipe
    insured_data = dict(sorted(insured_data.items()))
    tipe_asuransi = dict(sorted(tipe_asuransi.items()))
    premi_tipe = dict(sorted(premi_tipe.items()))

def sort_SI():
    sorted_insured_data = dict(sorted(insured_data.items(), key= lambda item : item[1]['SI'], reverse=True))
    table_data=[]
    for uid, details in sorted_insured_data.items():
        table_data.append([uid, details['name'], details['gender'], details['smoking'], details['age'], details['ins_code'], details['ins_type'], details['SI'], int(math.floor(details['premium']))])
    print("Sorted according to: Sum Insured")
    print(tabulate(table_data, headers= ['UID', 'name', 'gender', 'smoking', 'age', 'code', 'insurance name', 'SI', 'premium'], tablefmt= 'grid'))
    premium_total = 0
    for x in insured_data:
        premium_total += insured_data[x]['premium']
    print(f"Total Premium received per month: {math.floor(premium_total)}")

def sort_premium():
    sorted_insured_data = dict(sorted(insured_data.items(), key= lambda item : item[1]['premium'], reverse=True))
    table_data=[]
    for uid, details in sorted_insured_data.items():
        table_data.append([uid, details['name'], details['gender'], details['smoking'], details['age'], details['ins_code'], details['ins_type'], details['SI'], int(math.floor(details['premium']))])
    print("Sorted according to: Premium")
    print(tabulate(table_data, headers= ['UID', 'name', 'gender', 'smoking', 'age', 'code', 'insurance name', 'SI', 'premium'], tablefmt= 'grid'))
    premium_total = 0
    for x in insured_data:
        premium_total += insured_data[x]['premium']
    print(f"Total Premium received per month: {math.floor(premium_total)}")

def sort_age():
    sorted_insured_data = dict(sorted(insured_data.items(), key= lambda item : item[1]['age'], reverse=True))
    table_data=[]
    for uid, details in sorted_insured_data.items():
        table_data.append([uid, details['name'], details['gender'], details['smoking'], details['age'], details['ins_code'], details['ins_type'], details['SI'], int(math.floor(details['premium']))])
    print("Sorted according to: Premium")
    print(tabulate(table_data, headers= ['UID', 'name', 'gender', 'smoking', 'age', 'code', 'insurance name', 'SI', 'premium'], tablefmt= 'grid'))
    premium_total = 0
    for x in insured_data:
        premium_total += insured_data[x]['premium']
    print(f"Total Premium received per month: {math.floor(premium_total)}")

def filter_gender():
    filter_gender_list = []
    for y in insured_data:
        filter_gender_list.append(insured_data[y]['gender'])
    while True:
        try:
            for a, b in enumerate(['M', 'F']):
                if b in filter_gender_list:
                    print(f"{a+1}: {'Male' if b == 'M' else 'Female'}")
            filter_key = int(input("Input the number of option to be displayed: "))
            break
        except ValueError:
            print("Please input a number")
    if filter_key not in [1,2]:
        print("Please input number between 1 and 2")
    else:
        filtered_insured_data = {}
        if filter_key == 1:
            for x in insured_data:
                if insured_data[x]['gender'] == 'M':
                    filtered_insured_data.update({x : insured_data[x]})
            table_data = []
            for uid, details in filtered_insured_data.items():
                table_data.append([uid, details['name'], details['gender'], details['smoking'], details['age'], details['ins_code'], details['ins_type'], details['SI'], int(math.floor(details['premium']))])
            print(f"Sorted According to: Male")
            print(tabulate(table_data, headers= ['UID', 'name', 'gender', 'smoking', 'age', 'code', 'insurance name', 'SI', 'premium'], tablefmt= 'grid'))
            total_premium = 0
            for z in filtered_insured_data:
                total_premium += filtered_insured_data[z]['premium']
            print(f"Total premium received per month for male is: {int(total_premium)}")
        else:
            for x in insured_data:
                if insured_data[x]['gender'] == 'F':
                    filtered_insured_data.update({x : insured_data[x]})
            table_data = []
            for uid, details in filtered_insured_data.items():
                table_data.append([uid, details['name'], details['gender'], details['smoking'], details['age'], details['ins_code'], details['ins_type'], details['SI'], int(math.floor(details['premium']))])
            print(f"Sorted According to: gender(Female)")
            print(tabulate(table_data, headers= ['UID', 'name', 'gender', 'smoking', 'age', 'code', 'insurance name', 'SI', 'premium'], tablefmt= 'grid'))
            total_premium = 0
            for z in filtered_insured_data:
                total_premium += filtered_insured_data[z]['premium']
            print(f"Total premium received per month for female is: {int(total_premium)}")

def filter_smoking():
    filter_gender_list = []
    for y in insured_data:
        filter_gender_list.append(insured_data[y]['smoking'])
    while True:
        try:
            for a, b in enumerate(['N', 'Y']):
                if b in filter_gender_list:
                    print(f"{a}: {'No' if b == 'N' else 'Yes'}")
            filter_key = int(input("Input the number of option to be displayed: "))
            break
        except ValueError:
            print("Please input a number")
    if filter_key not in [0,1]:
        print("Please input number between 0 and 1")
    else:
        filtered_insured_data = {}
        if filter_key == 0:
            for x in insured_data:
                if insured_data[x]['smoking'] == 'N':
                    filtered_insured_data.update({x : insured_data[x]})
            table_data = []
            for uid, details in filtered_insured_data.items():
                table_data.append([uid, details['name'], details['gender'], details['smoking'], details['age'], details['ins_code'], details['ins_type'], details['SI'], int(math.floor(details['premium']))])
            print(f"Sorted According to: smoking(N)")
            print(tabulate(table_data, headers= ['UID', 'name', 'gender', 'smoking', 'age', 'code', 'insurance name', 'SI', 'premium'], tablefmt= 'grid'))
            total_premium = 0
            for z in filtered_insured_data:
                total_premium += filtered_insured_data[z]['premium']
            print(f"Total premium received per month for not smoking insureds is: {int(total_premium)}")
        else:
            for x in insured_data:
                if insured_data[x]['smoking'] == 'Y':
                    filtered_insured_data.update({x : insured_data[x]})
            table_data = []
            for uid, details in filtered_insured_data.items():
                table_data.append([uid, details['name'], details['gender'], details['smoking'], details['age'], details['ins_code'], details['ins_type'], details['SI'], int(math.floor(details['premium']))])
            print(f"Sorted According to: smoking (Y)")
            print(tabulate(table_data, headers= ['UID', 'name', 'gender', 'smoking', 'age', 'code', 'insurance name', 'SI', 'premium'], tablefmt= 'grid'))
            total_premium = 0
            for z in filtered_insured_data:
                total_premium += filtered_insured_data[z]['premium']
            print(f"Total premium received per month for smoking insureds is: {int(total_premium)}")

def filter_age():
    while True:
        try:
            age_lower = int(input("Input minimum age to be filtered(17-100): "))
            break
        except ValueError:
            print("Please input a number")
    if age_lower < 17 or age_lower >= 100:
        print("Age must be between 17 - 99")
    else:
        while True:
            try:
                age_upper = int(input("Input maximum age to be filtered(17-100): "))
                break
            except ValueError:
                print("Please input a number")
        if age_upper < age_lower or age_upper > 100:
            print("Age must be above minimum or below 100")
        else:
            sorted_insured_data = dict(sorted(insured_data.items(), key= lambda item : item[1]['age'], reverse=True))
            sorted_insured_data2 = {}
            for num in sorted_insured_data:
                if sorted_insured_data[num]['age'] >= age_lower and sorted_insured_data[num]['age'] <= age_upper:
                    sorted_insured_data2.update({num : sorted_insured_data[num]})
            table_data=[]
            for uid, details in sorted_insured_data2.items():
                table_data.append([uid, details['name'], details['gender'], details['smoking'], details['age'], details['ins_code'], details['ins_type'], details['SI'], int(math.floor(details['premium']))])
            print(f"Insured data with age between {age_lower} and {age_upper}")
            print(tabulate(table_data, headers= ['UID', 'name', 'gender', 'smoking', 'age', 'code', 'insurance name', 'SI', 'premium'], tablefmt= 'grid'))
            premium_total = 0
            for x in insured_data:
                premium_total += insured_data[x]['premium']
            print(f"Total Premium received per month: {math.floor(premium_total)}")

def filter_ins_type():
    while True:
        try:
            filter_type_list = []
            for y in insured_data:
                filter_type_list.append(insured_data[y]['ins_code'])
            print("Available insurance type: ")
            for x in tipe_asuransi:
                if x in filter_type_list:
                    print(f"{x}: {tipe_asuransi[x]}")
            filter_key = int(input("Input the insurance type key to be displayed: "))
            break
        except ValueError:
            print("Please enter a number")
    if filter_key not in filter_type_list:
        print("Insurance type is not available for display")
    else:
        filtered_insured_data = {}
        for x in insured_data:
            if insured_data[x]['ins_code'] == filter_key:
                filtered_insured_data.update({x : insured_data[x]})
        table_data = []
        for uid, details in filtered_insured_data.items():
            table_data.append([uid, details['name'], details['gender'], details['smoking'], details['age'], details['ins_code'], details['ins_type'], details['SI'], int(math.floor(details['premium']))])
        print(f"Sorted According to: Insurance Type({tipe_asuransi[filter_key]})")
        print(tabulate(table_data, headers= ['UID', 'name', 'gender', 'smoking', 'age', 'code', 'insurance name', 'SI', 'premium'], tablefmt= 'grid'))
        total_premium = 0
        for z in filtered_insured_data:
            total_premium += filtered_insured_data[z]['premium']
        print(f"Total premium received per month for this insurance type is: {int(total_premium)}")

        

# Menu Function

def main_menu():
    global menu_input
    calc()
    print("""
    Main Menu
    1. Display Insurance Policy Details
    2. Add new Insurance Policy
    3. Update Insurance Policy Details
    4. Delete Insurance Policy
    5. Insurance Type menu
    6. Sort Menu
    7. Filter Menu
    8. Exit Program
          """)
    while True:
        try:
            menu_input = int(input("Input menu number: "))
            break
        except ValueError:
            print("Please input a number")
    while menu_input < 1 or menu_input > 8:
        print("Please input a number between 1-8")
        while True:
            try:
                menu_input = int(input("Input menu number: "))
                break
            except ValueError:
                print("Please input a number")

def menu_1():
    global menu_input_1
    sort_main()
    print("""
    Insurance Policy Details
    1. Display All Data
    2. Display details of an insured
    3. Exit to Main Menu
          """)
    while True:
        try:
            menu_input_1 = int(input("Input menu number: "))
            break
        except ValueError:
            print("Please input a number")
    while menu_input_1 < 1 or menu_input_1 > 3:
        print("Please input a number between 1-3")
        while True:
            try:
                menu_input_1 = int(input("Input menu number: "))
                break
            except ValueError:
                print("Please input a number")

def menu_2():
    global menu_input_2
    sort_main()
    print("""
    Add a new Policy
    1. Add a new data
    2. Exit to Main Menu    
    """)
    while True:
        try:
            menu_input_2 = int(input("Input menu number: "))
            break
        except ValueError:
            print("Please input a number")
    while menu_input_2 < 1 or menu_input_2 > 2:
        print("Please input a number between 1-2")
        while True:
            try:
                menu_input_2 = int(input("Input menu number: "))
                break
            except ValueError:
                print("Please input a number")

def menu_3():
    global menu_input_3
    sort_main()
    print("""
    Update a policy details
    1. Update a detail
    2. Exit to Main Menu
    """)
    while True:
        try:
            menu_input_3 = int(input("Input menu number: "))
            break
        except ValueError:
            print("Please input a number")
    while menu_input_3 < 1 or menu_input_3 > 2:
        print("Please input a number between 1-2")
        while True:
            try:
                menu_input_3 = int(input("Input menu number: "))
                break
            except ValueError:
                print("Please input a number")

def menu_4():
    global menu_input_4
    sort_main()
    print("""
    Delete a policy menu
    1. Delete a policy
    2. Exit to Main Menu
    """)
    while True:
        try:
            menu_input_4 = int(input("Input menu number: "))
            break
        except ValueError:
            print("Please input a number")
    while menu_input_4 < 1 or menu_input_4 > 2:
        print("Please input a number between 1-2")
        while True:
            try:
                menu_input_4 = int(input("Input menu number: "))
                break
            except ValueError:
                print("Please input a number")

def menu_5():
    global menu_input_5
    sort_main()
    print("""
    Insurance type menu
    1. Display insurance types details
    2. Add new insurance type
    3. Update insurance type details
    4. Delete an insurance type (must have no data using the type)
    5. Exit to Main Menu
    """)
    while True:
        try:
            menu_input_5 = int(input("Input menu number: "))
            break
        except ValueError:
            print("Please input a number")
    while menu_input_5 < 1 or menu_input_5 > 5:
        print("please input a number between 1-5")
        while True:
            try:
                menu_input_5 = int(input("Input menu number: "))
                break
            except ValueError:
                print("Please input a number")

def menu_6():
    global menu_input_6
    sort_main()
    print("""
    Sort Menu
    1. Sum Insured
    2. Premium
    3. Age
    4. Exit to Main Menu
    """)
    while True:
        try:
            menu_input_6 = int(input("Input menu number: "))
            break
        except ValueError:
            print("Please input a number")
    while menu_input_6 < 1 or menu_input_6 > 4:
        print("please input a number between 1-4")
        while True:
            try:
                menu_input_6 = int(input("Input menu number: "))
                break
            except ValueError:
                print("Please input a number")

def menu_7():
    global menu_input_7
    sort_main()
    print("""
    Sort Menu
    1. Gender
    2. Smoking
    3. Age (Range)
    4. Insurance Types
    5. Exit to Main Menu
    """)
    while True:
        try:
            menu_input_7 = int(input("Input menu number: "))
            break
        except ValueError:
            print("Please input a number")
    while menu_input_7 < 1 or menu_input_7 > 5:
        print("please input a number between 1-5")
        while True:
            try:
                menu_input_7 = int(input("Input menu number: "))
                break
            except ValueError:
                print("Please input a number")


# Main Program

main_menu()
while menu_input == menu_input:
    while menu_input == 1:
        menu_1()
        if insured_data == None:
            print("Data does not exist")
        else:
            if menu_input_1 == 1:
                print_all_data()
            elif menu_input_1 == 2:
                print_1_data()
            else:
                confirmation()
                if confirmation_input == "N":
                    pass
                else:
                    main_menu()
            
    while menu_input == 2:
        menu_2()
        if menu_input_2 == 1:
            add_data()
        else:
            confirmation()
            if confirmation_input == "N":
                pass
            else:
                main_menu()

    while menu_input == 3:
        menu_3()
        if menu_input_3 == 1:
            update_menu()
        else:
            confirmation()
            if confirmation_input =="N":
                pass
            else:
                main_menu()

    while menu_input == 4:
        menu_4()
        if menu_input_4 == 1:
            delete_menu()
        else:
            confirmation()
            if confirmation_input == 'N':
                pass
            else:
                main_menu()

    while menu_input == 5:
        menu_5()
        if menu_input_5 == 1:
            print("Available Insurance types:")
            for x in tipe_asuransi:
                print(f"{x}: {tipe_asuransi[x]}, {premi_tipe[x]*100}% of SI")
        elif menu_input_5 == 2:
            ins_type_add()
        elif menu_input_5 == 3:
            ins_type_update()
        elif menu_input_5 == 4:
            ins_type_del()
        else:
            confirmation()
            if confirmation_input == 'N':
                pass
            else:
                main_menu()

    while menu_input == 6:
        menu_6()
        if menu_input_6 == 1:
            sort_SI()
        elif menu_input_6 == 2:
            sort_premium()
        elif menu_input_6 == 3:
            sort_age()
        else:
            confirmation()
            if confirmation_input == 'N':
                pass
            else:
                main_menu()
    
    while menu_input == 7:
        menu_7()
        if menu_input_7 == 1:
            filter_gender()
        elif menu_input_7 == 2:
            filter_smoking()
        elif menu_input_7 == 3:
            filter_age()
        elif menu_input_7 == 4:
            filter_ins_type()
        else:
            confirmation()
            if confirmation_input == 'N':
                pass
            else:
                main_menu()

    while menu_input == 8:
        print("Exit the program?")
        confirmation()
        if confirmation_input == 'N':
            main_menu()
        else:
            exit()
