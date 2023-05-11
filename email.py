### --- OOP Email Simulator --- ###

# --- Email Class --- #
class Email:
    has_been_read = False

    def __init__(self, email_address, subject_line, email_content):
        # Initialise the instance variables for emails.
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content 
    
    # method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True


# --- Lists --- #

# Initialise an empty list to store the email objects.
inbox = []

# --- Functions --- #

def populate_inbox():
    # Create 3 sample emails and add it to the Inbox list. 
    email1 = Email("tdog@gmail.com",
                   "check out these new shoes!",
'''We have brand new shoes in stock at half price!
Check out our new brand now! by clicking the link
www.tdogshoes.com.

Happy shopping
Tdog Shoes! '''
                   )
    inbox.append(email1)
    email2 = Email("bob@gmail.com",
                   "Pub Friday?!",
'''Lets hit the town friday! drinks are on me!

Thanks 
Bob'''
                   )
    inbox.append(email2)
    email3 = Email("jimjaguers@gmail.com",
                   "Exotic animal just for you!",
'''Have you ever wanted to own your very own exotic
cat??? Today is your lucky day, hit the link,
www.myexoticcat.com to see our stock of exotic cats,
from lions to jaguers find your new friend for life today!
                    
Happy Catting
Jim'''
                   )
    inbox.append(email3)
    
    

#function which prints the email’s subject_line, along with a corresponding number
def list_emails():
    for count, email in enumerate(inbox):
        print(count, email.subject_line)

# function which displays a selected email.
def read_email(index): 
    if 0 <= index < len(inbox):
        email = inbox[index]
        print(f"\nEmail from: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"Message says: \n\n{email.email_content}")

        #set email to read = true
        email.mark_as_read()
        print(f"\nEmail '{email.subject_line}' has been marked as read!")
    else:
        print("Invalid input")

# --- Email Program --- #

#call populate inbox, to create the inbox.
populate_inbox()

menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        list_emails() #call the list first so the user can choose the email to read.
        index = int(input("\nEnter the number of the email you wish to read: "))
        read_email(index)
    elif user_choice == 2:
        for email in inbox:
            print(email.subject_line)
    elif user_choice == 3:
        exit()
    else:
        print("Oops - incorrect input.")

