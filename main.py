import conection as con
def print_logo():
    print('░██████╗')
    print('██╔════╝')
    print('╚█████╗░')
    print('░╚═══██╗')
    print('██████╔╝')
    print('╚═════╝░')

    print('...')


def inicial_func(option):
    if int(option) == 1:
        print("You picked new sale (1):")
        print("You need to type the information as required: ")
        print(" Product name ,Seller name,Costumer name,Sale value ")
        product = input("Product name: ")
        seller = input("Seller name: ")
        costumer = input("Costumer name: ")
        value = input("Sale Value: ")
        clas_stor = con.Storage()
        seller_id = clas_stor.get_seller(seller)
        if seller_id == []:
            print("Error seller: {} is not a valid seller".format(seller))
            inicial_func(option)
        seller_id = seller_id[0][0]
        #
        print(seller_id)
        if seller_id:
            result = clas_stor.populate(product, seller_id, costumer, float(value))
            print(result)
        else:
            print("Error seller: {} is not a valid seller".format(seller))
            inicial_func(option)
    elif int(option) == 2:
        print("You choose ranking of sales (2):")
        result = con.Storage().show_ranking_sales()
        for x in result:
            print(x)
    elif int(option) == 3:
        print("Delete sale...")
        know = input("Do you know the sale id(y/n)?")
        if know == "y":
            sale_id = input("Type the sale_id here: ")
            con.Storage.delete(sale_id)
        else:
            print("You can find your sale on the ranking down here:")
            ranking = con.Storage.show_ranking_sales()
            for x in ranking:
                print(x)
            sale_id = input("Type the sale_id here: ")
            con.Storage.delete(sale_id)
    else:
        print("you have to pick a valid option number !")

if __name__ == '__main__':
    print('Welcome to our sales sistem!!')
    print_logo()
    print("You got a few options here:")
    print("Register a new Sale(1)")
    print("Ranking of sales (2)")
    print("delete sale (3)")
    option = input("Type your number option here: ")
    inicial_func(option)



