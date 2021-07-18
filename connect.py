#import MySQLdb
import random

"""
host = 'localhost'
user = 'thirdParty'
password = 'admin'
db = 'bands'
port = 3306
"""

#con = MySQLdb.connect(host='localhost', user='thirdParty', password='admin', db='bands', port=3306)
#cursor = con.cursor()

entry_mistake_list = ['I\'m sorry, I didn\'t get that\n', 'That\'s not a valid input\n', 'Something\'s wrong with your input\n']

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


        #cursor.execute(query)

        #print(cursor.fetchall())


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
            insertion += 'band VALUES(default, \'' + band_name + '\');'


        elif option == '2':

            member_name = input('What\'s their name?\n::')
            while member_name == '':
                print(entry_mistake_list[random.randint(0,2)])
                member_name = input('What\'s their name?\n::')

            member_year = int(input('What year were they born?\n::'))
            while 0 > member_year:
                print(entry_mistake_list[random.randint(0,2)])
                member_year = int(input('What year were they born?\n::'))

            member_month = int(input('Which month? (Enter the number not the name)\n::'))
            while 1 > member_month or member_month > 12:
                print(entry_mistake_list[random.randint(0,2)])
                member_month = int(input('Which month? (Enter the number not the name)\n::'))

            member_day = int(input('What about the day?\n::'))
            while 1 > member_day or member_day > 31:
                print(entry_mistake_list[random.randint(0,2)])
                member_day = int(input('What about the day?\n::'))

            nickname = input('Do they have a nickname?(yes/no)\n::')
            if nickname == 'yes':
                nickname = input('And what would that be?\n::')
            else:
                nickname = ''

            insertion += 'member VALUES(default, ' + member_name + ', ' + str(member_year) + '-' + str(member_month) + '-' + str(member_day) + ', ' + nickname + ');'

            print(insertion)

        elif option == '3':
            insertion += 'album'

        elif option == '4':
            insertion += 'song'

        elif option == '5':
            insertion += 'instrument'

        elif option == '6':
            insertion += 'record_label'


        #cursor.execute(insertion)
        #con.commit()

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
