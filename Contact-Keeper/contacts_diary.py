storage={
    "Swiss": ['23145000425','2546531200'],
    "Jenny": ['12345'],
    "Santa": ['5321','14523']
}
def show_contacts():
    global storage

    print('Name      Phone-Nos.')
    for key in sorted(storage):
        print('{}    {}\n'.format(key, storage[key]))


def srch_name(key):
    res= [k for k,v in storage.items() if k.startswith(key)]
    if not res:
        print('Does not exist\n')
    else:
        print(str(res))
        a = input("Now enter the complete Name to get contact details\n").capitalize()
        if a not in storage.keys():
            print('Does not exist\n')
        else:
            result = storage[a]
            print(result)

def srch_num(val):
    key_list = [(k,storage[k]) for k, v in storage.items() if val in v]
    if not key_list:
        print("Not found\n")
    else:
        print("The Name and Contact Number(s) :\n",key_list)


def add_contact():
    print("---------------Enter all the numbers one after another to check if they already exists-----------\n")
    while 1:
        a = input("Enter number to check \nor type 0, if you have checked all the numbers and want to proceed.\n")
        if a=='0':
            break
        else:
            key_list1 = [v for k, v in storage.items() if a in v]
            if key_list1:
                print("Number already exists!! \n")

            else:
                print("Number can be added!!!\n")

    key = str(input("Enter the New Contact Name\n")).capitalize()
    val = input("Enter phone no(s) separated by comma(in case of multiple numbers)\n").split(',')
    storage[key]= val
    print("Contact Added Successfully\n")

def update_contact():
    a = input("Enter the Name of the contact to update/change\n").capitalize()
    if a not in storage.keys():
        print("Not found !! Retry!!")
    else:
        key = str(input("Enter the updated Name(if any) or else enter the same name\n")).capitalize()
        val = input("Enter the updated phone no(s)(separated by comma in case of multiple numbers)\n").split(',')
        storage.pop(a)
        storage.update({key:val})
        print('Contact Updated\n')


def delete_contact(key):
    if key not in storage.keys():
        print("Error!! Contact not found. Retry.\n")
    else:
        storage.pop(key)
        print("Contact Deleted\n")

###########################################################
############################################################




print("\n--------------WELCOME TO THE CONTACTS DIARY---------------\n")
while True:
    x=int(input("Choose your action:\n"
                "1. Type 1 : view all contacts\n"
                "2. Type 2 : search for a contact using Name.\n"
                "3. Type 3 : search using Number.\n"
                "4. Type 4 : add a new contact\n"
                "5. Type 5 : update a contact\n"
                "6. Type 6 : delete a contact\n"
                "7. Enter 7 : quit program or EXIT\n"))

    if x==1:
        show_contacts()

    elif x==2:
        y=input("Enter the initials to search all names: ")
        srch_name(y.capitalize())
    elif x==3:
        z = input("Enter a single phone number to search: ")
        srch_num(z)
    elif x==4:
        add_contact()
    elif x==5:

        update_contact()
    elif x==6:
        z = str(input("Enter the Contact Name to delete\n")).capitalize()
        delete_contact(z)

    elif x==7:
        break
    else:
        print("-------------Invalid choice !!. Choose only from the given options.--------------------------\n")




