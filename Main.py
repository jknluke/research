class Ticket :
    counter = 2000
    
    def __init__(self, creator_name, staff_ID, email, description):
        self.ticket_num = Ticket.counter + 1
        Ticket.counter+=1
        self.creator_name = creator_name
        self.staff_ID = staff_ID
        self.email = email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"

        if description.lower() == "password change":
            generate_password = staff_ID[0:2] + creator_name[0:3]
            self.response = f"New password generated: {generate_password}"
            self.status = "Closed"


def All_Tickets() :
    for t in ticket_list:
        print(f"Ticket Number: {t.ticket_num}")
        print(f"Ticket Creator: {t.creator_name}")
        print(f"Staff ID: {t.staff_ID}")
        print(f"Email Address: {t.email}")
        print(f"Description: {t.description}")
        print(f"Response: {t.response}")
        print(f"Ticket Status: {t.status}")
        print(":---------------------------:")


# Create Show_Statistics() function here

def Display_Ticket(ticket_num) :
    for t in ticket_list:
        if t.ticket_num == int(ticket_num):
            print(f"Ticket Number: {t.ticket_num}")
            print(f"Ticket Creator: {t.creator_name}")
            print(f"Staff ID: {t.staff_ID}")
            print(f"Email Address: {t.email}")
            print(f"Description: {t.description}")
            print(f"Response: {t.response}")
            print(f"Ticket Status: {t.status}")


def Respond(ticket_num) :
    for t in ticket_list:
        if t.ticket_num == int(ticket_num):
            if t.status != "Closed":
                t.response = input("Enter new response: \n > ")
                option = input("Would you like to resolve this ticket? y/n \n > ")
                if option.lower() == "y":
                    t.status = "Resolved"
            else:
                option = input("Would you like to reopen this ticket? y/n \n > ")
                if option.lower() == "y":
                    t.status = "Reopened"
                    t.response = input("Enter new response: \n > ")
            Display_Ticket(t.ticket_num)



# Create Ticket Function
def Create() :
    #Stuff for create here
    input_creator_name = input("Enter creator name: \n > ")
    input_staff_ID = input("Enter Staff ID: \n >")
    input_email = input("Enter email: \n >")
    input_description = input("Enter job description: \n >")
    new_ticket = Ticket(input_creator_name, input_staff_ID, input_email, input_description)
    ticket_list.append(new_ticket)
    Display_Ticket(new_ticket.ticket_num) # - Change to Show_Statistics() method


ticket_list = []
ticket1 = Ticket("Inna", "INNAM", "inna@whitecliffe.co.nz", "My monitor stopped working")
ticket_list.append(ticket1)

ticket2 = Ticket("Maria", "MARIAH", "maria@whitecliffe.co.nz", "Request for a videocamera to conduct webinars")
ticket_list.append(ticket2)

ticket3 = Ticket("John", "JOHNS", "john@whitecliffe.co.nz", "Password change")
ticket_list.append(ticket3)

user_prompt = ""

def main() :
    user_prompt = ""
    while user_prompt.lower() != "e":
        user_prompt = input("What would you like to do? \n Options:" 
                            "\n (C)reate new ticket "
                            "\n (D)isplay a Ticket "
                            "\n (R)espond to a Ticket "
                            "\n Show (A)ll Tickets"
                            " \n (E)xit the program "
                            "\n > ")

        if user_prompt.lower() == "c":
            Create()
        elif user_prompt.lower() == "d":
            ticket_num = input("Enter Ticket Number: \n > ")
            Display_Ticket(ticket_num)
        elif user_prompt.lower() == "r":
            ticket_num = input("Enter Ticket Number: \n > ")
            Respond(ticket_num)
        elif user_prompt.lower() == "a":
            All_Tickets()
        elif user_prompt.lower() == 'e':
            break
        else:
            print("Please enter one of the listed options.")


main()