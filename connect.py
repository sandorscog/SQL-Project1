import MySQLdb

"""
host = 'localhost'
user = 'thirdParty'
password = 'admin'
db = 'bands'
port = 3306
"""

con = MySQLdb.connect(host='localhost', user='thirdParty', password='admin', db='bands', port=3306)
cursor = con.cursor()

def select():

    query = 'SELECT * FROM '

    print('Choose a query:\n1- Bands\n2- Band members\n3- Albuns\n4- Songs\n5- Instruments\n6- Labels0- To exit')
    option = input('::')
    while option != '0':

        if option == '1':
            query += 'band'

        elif option == '2':
            query += 'member'

        elif option == '3':
            query += 'album'

        elif option == '4':
            query += 'song'

        elif option == '5':
            query += 'instrument'

        elif option == '6':
            query += 'record_label'


        cursor.execute(query)

        print(cursor.fetchall())


        print('Choose a query:\n1- Bands\n2- Band members\n3- Albuns\n4- Songs\n5- Instruments\n6- Labels0- To exit')
        option = input('::')

    return

def insert():

    insertion = 'INSERT INTO '

    print('Choose a query:\n1- Bands\n2- Band members\n3- Albuns\n4- Songs\n5- Instruments\n6- Labels0- To exit')
    option = input('::')
    while option != '0':

        if option == '1':
            band_name = input('what\'s the name of the band?\n::')
            insertion += 'band VALUES(default, \'' + band_name + '\')'


        elif option == '2':
            insertion += 'member VALUES(default, )'

        elif option == '3':
            insertion += 'album'

        elif option == '4':
            insertion += 'song'

        elif option == '5':
            insertion += 'instrument'

        elif option == '6':
            insertion += 'record_label'


        cursor.execute(insertion)
        con.commit()

        print('Choose a query:\n1- Bands\n2- Band members\n3- Albuns\n4- Songs\n5- Instruments\n6- Labels\n0- To exit')
        option = input('::')



    return

def update():
    return

def delete():
    return





def menu():


    print('Choose an action:\n1- Select\n2- Insert\n3- Update\n4- Delete\n0- To exit')
    option = input('::')
    while option != '0':

        if option == '1':
            select()

        elif option == '2':
            insert()

        elif option == '3':
            update()

        elif option == '4':
            delete()


        print('Choose an action:\n1- Select\n2- Insert\n3- Update\n4- Delete\n0- To exit')
        option = input('::')



def main():
    menu()

main()
