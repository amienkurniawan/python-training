try :
    
    number = int(input("masukan angka :"))
    print(number)
except ValueError as err:
    print(err)
except ZeroDivisionError as err:
    print(err)