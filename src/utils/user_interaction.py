from src.utils.utils import *


def user_interaction():
    """Function for interacting with the user via the console"""

    vacancies = []

    print('Welcome to the console job search tool')

    while True:
        print("Select an action:")
        print("1 - Vacancy search")
        print("2 - Saving vacancies to a file")
        print("3 - Deleting a vacancy from a file")
        print("4 - Getting a vacancy from file based on salary")
        print("5 - Getting a vacancy from file based on the city")
        print("6 - Getting top N vacancies from a file")
        print("7 - Getting all vacancies from a file")
        print("0 - Completion of the program")

        choice = input("Enter the action number: ")

        if choice == "1":
            vacancies = search_vacancy()

        elif choice == "2":
            if vacancies:
                save_vacancies(vacancies)
            else:
                print("You must first perform a vacancy search (action 1) before saving.")

        elif choice == "3":
            remove_vacancies(vacancies)

        elif choice == "4":
            get_vac_by_salary(vacancies)

        elif choice == "5":
            get_vac_by_city(vacancies)

        elif choice == "6":
            get_top_vac(vacancies)

        elif choice == "7":
            get_all_vacancies(vacancies)

        elif choice == "0":
            print("Exiting the program")
            print("Thank you for using this program, come back again :)")
            exit()
        else:
            print("Wrong choice. Please select an existing option.")
