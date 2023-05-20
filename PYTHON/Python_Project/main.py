import csv
import datetime

# Get the current date and time
current_date = datetime.datetime.now().strftime("%d%m%Y")

# Create a temporary file to store the contact data
current_working_file = f"Contact book_{current_date}.csv"

# Get the path to the original contact file
original_file = 'Contact Book.csv'


# This function prompts the user to select an action, such as creating, updating, or deleting a contact.
def user_selection():
    selection = int(input(
        "Please Select What Do You Want To Do. If 1 : Create A Contact, If 2 : Update A Contact, If 3 : Delete A Contact"))

    if selection == 1:  # Check if the user wants to create a contact.
        user_input()
    elif selection == 2:  # Check if the user wants to update a contact.
        update_contact()
    elif selection == 3:  # Check if the user wants to delete a contact.
        delete_contact()
    else:  # Validating the user's input if it is from the choices
        print("Wrong Choice, Please Enter 1, 2 or 3")


# This function collects the user's input for a new contact, such as their name, email address, phone number, and address.
def user_input():
    flag = 0
    contact_name = input("Please Enter Contact Name")  # Get the contact's name
    contact_mail = input("Please Enter Contact Mail")  # Get the contact's mail
    while flag == 0:
        contact_no = input("Please Enter Contact Number")  # Get the contact's number
        # Validating the user's input
        if contact_no.isdigit():
            flag = 1
        else:
            print("Please Enter Correct Number")
            flag = 0

    contact_addr = input("Please Enter Contact Address")  # Get the contact's address
    insert_date = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')  # Get date and time of the moment
    # Return the contact's information to a save function
    save_inputs(contact_name, contact_mail, contact_no, contact_addr, insert_date)
    print("You Contact Has Been Added Successfully")
    another_req()  # Ask the user if they want to continue using the system


# This function writes the user's input to a CSV file.
def save_inputs(contact_name, contact_mail, contact_no, contact_addr, insert_date):
    with open('Contact Book.csv', 'a', newline='') as file:  # Open the CSV file for writing
        adder = csv.writer(file)  # Create a CSV writer object
        # Write the contact information to the file
        adder.writerow([contact_name, contact_mail, contact_no, contact_addr, insert_date])
        print("Your Contact Has Been Saved Successfully")
    import_original_data()  # Import the original contact data
    export_updated_data()  # Export the updated data to the original file
    another_req()  # Ask the user if they want to continue using the system


# This function updates an existing contact in a CSV file.
def update_contact():
    import_original_data()  # Import the original contact data
    # Get which field user wants to update
    inf = int(input(
        "Please Enter The Info You Want To Update If Contact Name 1, If Contact Mail 2, If Contact Number 3, If Contact Address 4 : "))

    if 0 < inf < 5:
        # Get the name of the contact the user wants to update
        contact_name = input("Enter The Contact Name You Want To Update : ")
        new_value = input("Please Enter New Value: ")  # Adding the new value to the wanted field
        with open(current_working_file, 'r') as file:  # Get the contact's information from the CSV file
            reader = csv.reader(file)
            rows = list(reader)
        for row in rows:
            if row[0] == contact_name:  # Find the contact in the CSV file
                if inf == 1:
                    row[0] = new_value  # Update the contact's name if it is required
                elif inf == 2:
                    row[1] = new_value  # Update the contact's mail if it is required
                elif inf == 3:
                    row[2] = new_value  # Update the contact's number if it is required
                elif inf == 4:
                    row[3] = new_value  # Update the contact's address if it is required
        # Write the updated contact information to the CSV file
        with open(current_working_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("Contact updated successfully!")
        export_updated_data()  # Export the updated data to the original file
        another_req()  # Ask the user if they want to continue using the system
    else:  # Validating user's input
        print("Please Enter Correct Input")
        update_contact()  # Call the function to update the contact


# This function prompts the user to continue using the contact management system.
def another_req():
    YN = input("Do You Want To Do Anything Else ?! (Y/N)")
    if (YN == "Y") | (YN == "y") | (YN == "yes") | (YN == "Yes"):
        # The user wants to continue using the system, so call the `user_selection()` function again.
        user_selection()
    elif (YN == "N") | (YN == "n") | (YN == "no") | (YN == "No"):
        # The user does not want to continue using the system, so print a message and exit.
        print("Thanks For Using Our Contact Book")
        exit()


# This function deletes a contact from a CSV file.
def delete_contact():
    import_original_data()  # Import the original contact data
    contact_name = input("Enter The Contact Name You Want To Remove: ")  # Get contact's name user want to remove

    # Get the contact's information from the CSV file
    with open(current_working_file, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    # Find the contact in the CSV file
    for row in rows:
        if row[0] == contact_name:
            rows.remove(row)  # Remove the contact from the CSV file
    # Write the updated contact information to the CSV file
    with open(current_working_file, 'w', newline='') as file:
        adder = csv.writer(file)
        adder.writerows(rows)

    print("Contact Has Been Deleted Successfully")
    export_updated_data()  # Export the updated data to the original file
    another_req()  # Ask the user if they want to continue using the system


# This function imports the original contact data from a CSV file.
def import_original_data():
    with open(original_file, 'r') as input_file:  # Open the original contact file for reading
        reader = csv.reader(input_file)  # Create a CSV reader object
        # Create a temporary file to store the imported data
        with open(current_working_file, 'w', newline='') as output_file:
            adder = csv.writer(output_file)  # Create a CSV writer object
            for row in reader:  # Write the contact information to the temporary file
                adder.writerow(row)


# This function exports the updated contact data to a CSV file.
def export_updated_data():
    with open(current_working_file, 'r') as input_file:  # Open the temporary contact file for reading
        reader = csv.reader(input_file)  # Create a CSV reader object
        with open(original_file, 'w', newline='') as output_file:  # Open the original contact file for writing
            adder = csv.writer(output_file)  # Create a CSV writer object
            for row in reader:  # Write the contact information to the original file
                adder.writerow(row)


user_selection()  # Call this function to start
