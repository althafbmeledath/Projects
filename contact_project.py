class Contacts:
    
    def __init__(self):
        self.data={}
        self.helper()
    
    #helper function
    def helper(self):
        print()
        print("Press 1 to add new contacts")
        print("Press 2 to edit existing contacts")
        print("Press 3 to delete an existing contact")
        print("Press 4 to find an existing contacts number")
        print("Press 5 to print all the existing contacts in the database")
        print("Press any number not in this list to quit")
        
        choice=int(input("Enter your choice: "))
        
        if choice==1:
            self.add()
        elif choice==2:
            self.edit()
        elif choice==3:
            self.delete()
        elif choice==4:
            self.find()
        elif choice==5:
            self.list_all()
        else:
            return
                    
    def add(self):
        name=input("Enter the name of the contact: ")
        number=input("Enter the number of the contact: ")
        
        #check if contact already there or not
        if name in self.data.keys():
            print("Contact already exists")
            return self.helper()
        
        #add contact to database
        self.data[name]=number
        print("Contact added successfully")
        return self.helper()
        
        
    def edit(self):
        name_edit=input("Enter the name of the contact you need to edit: ")
        
        #check if contact is there or not
        if name_edit in self.data.keys():
            name1=input("Enter the new name if not enter null: ")
            number1=input("Enter the new number if not enter null: ")
            
            if name1!='null' and number1!='null':
                self.data[name1]=number1
                del self.data[name_edit]
                print("Contact edited successfully")
                return self.helper()
            
            elif name1!='null':
                self.data[name1]=self.data[name_edit]
                del self.data[name_edit]
                print("Contact edited successfully")
                return self.helper()
            
            else:
                self.data[name_edit]=number1
                print("Contact edited successfully")
                return self.helper()
                
        else:
            print("The Contact doesnt exist please add this contact as new contact")
            return self.helper()
        
    
    def delete(self):
        name2=input("Enter the name of the contact you need to delete: ")
        if name2 in self.data.keys():
            del self.data[name2]
            print("Contact deleted successfully")
            return self.helper()
        
        else:
            print("This contact is not in this database")
            return self.helper()
        
    def find(self):
        name3=input("Enter the name of the contact you want to find: ")
        
        for name,number in self.data.items():
            if name==name3:
                print(f'The name is {name} and the number is {number}')
                return self.helper()
        else:
            print("Not Found")
            return self.helper()
        
    def list_all(self):
        for name,number in self.data.items():
            print(f'The name is {name} and the number is {number}')
                
        return self.helper()

    
c=Contacts()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        