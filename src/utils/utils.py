"""Functions for executing the main logic of the program, which are passed to the main function for user interaction"""
from src.api_classes import HeadHunterAPI, SuperJobAPI
from src.file_saver import JsonSaver, CSVSaver
import os

# The path to save files with vacancies
file_path_json = '../job_parser/saved_vacancies/json_vacancies.json'
file_path_csv = '../job_parser/saved_vacancies/csv_vacancies.csv'


def search_vacancy():
    """Function for getting vacancies from platforms"""

    platforms = ['HeadHunter', 'SuperJob']
    hh_site = HeadHunterAPI()
    sj_site = SuperJobAPI()
    print(f'Available platforms: {platforms}')

    input_platform = int(input(f'Choose a platform: 1 - HeadHunter, 2 - SuperJob, 3 - HeadHunter & SuperJob: \n'))

    if input_platform not in [1, 2, 3]:
        print("Incorrect choice of platform. Please choose 1, 2 or 3.")
        return

    name = input("Enter the job title: ")
    salary = int(input("Enter the minimum desired salary in RUB: "))
    quantity = int(input("Enter the number of vacancies to search(max 50): "))

    hh_vacancies = []
    sj_vacancies = []

    if input_platform in [1, 3]:
        vacancies = hh_site.get_vacancies(name, salary, quantity)
        hh_vacancies = hh_site.parse(vacancies)

    if input_platform in [2, 3]:
        vacancies = sj_site.get_vacancies(name, salary, quantity)
        sj_vacancies = sj_site.parse(vacancies)

    all_vacancies = hh_vacancies + sj_vacancies
    if len(all_vacancies) > 0:
        print('Job search completed successfully')
    else:
        print('Job search failed, try changing the request parameters')
    return all_vacancies


def save_vacancies(vacancies):
    """Function for saving vacancies to a file"""

    file_format = int(input('In what format do you want to save the file?\n 1 - JSON, 2 - CSV: '))

    json_save = JsonSaver(vacancies, f'../job_parser/saved_vacancies/json_vacancies.json')
    csv_save = CSVSaver(vacancies, f'../job_parser/saved_vacancies/csv_vacancies.csv')

    if file_format == 1:
        json_save.save_to_file()

    elif file_format == 2:
        csv_save.save_to_file()

    print(f'the file was successfully saved along the path: ../job_parser/saved_vacancies/')


def remove_vacancies(vacancies):
    """Function for deleting a vacancy from a file"""

    json_save = JsonSaver(vacancies, f'../job_parser/saved_vacancies/json_vacancies.json')
    csv_save = CSVSaver(vacancies, f'../job_parser/saved_vacancies/csv_vacancies.csv')

    remove_vac = input('Enter the exact name of the vacancy to delete: ')

    if os.path.isfile(file_path_json):
        json_save.delete_vacancy(remove_vac)
        print('the vacancy was successfully deleted from the JSON file')

    elif os.path.isfile(file_path_csv):
        csv_save.delete_vacancy(remove_vac)
        print('the vacancy was successfully deleted from the CSV file')

    else:
        print('There is no file with vacancies')


def get_vac_by_salary(vacancies):
    """Function for getting a vacancy based on salary"""

    json_save = JsonSaver(vacancies, f'../job_parser/saved_vacancies/json_vacancies.json')
    csv_save = CSVSaver(vacancies, f'../job_parser/saved_vacancies/csv_vacancies.csv')

    vac_by_sal = int(input('Enter salary to get vacancies: '))

    if os.path.isfile(file_path_json):
        vac_sal = json_save.get_vacancies_by_salary(vac_by_sal)
        for vac in vac_sal:
            print(vac)

    elif os.path.isfile(file_path_csv):
        vac_sal = csv_save.get_vacancies_by_salary(vac_by_sal)
        for vac in vac_sal:
            print(vac)

    else:
        print('There is no file with vacancies')


def get_vac_by_city(vacancies):
    """Function for getting a vacancy based on the city"""

    json_save = JsonSaver(vacancies, f'../job_parser/saved_vacancies/json_vacancies.json')
    csv_save = CSVSaver(vacancies, f'../job_parser/saved_vacancies/csv_vacancies.csv')

    vac_by_city = input('Enter the name city to get vacancies: ')

    if os.path.isfile(file_path_json):
        vac_city = json_save.get_vacancies_by_city(vac_by_city)
        for vac in vac_city:
            print(vac)

    elif os.path.isfile(file_path_csv):
        vac_city = csv_save.get_vacancies_by_city(vac_by_city)
        for vac in vac_city:
            print(vac)

    else:
        print('There is no file with vacancies')


def get_top_vac(vacancies):
    """Function for getting top N vacancies"""

    json_save = JsonSaver(vacancies, f'../job_parser/saved_vacancies/json_vacancies.json')
    csv_save = CSVSaver(vacancies, f'../job_parser/saved_vacancies/csv_vacancies.csv')

    top_num = int(input(
        'Enter the number of vacancies to display the top N vacancies\n'
        'If you enter a number greater than the vacancies in the file, all vacancies will be displayed:\n'))

    if os.path.isfile(file_path_json):
        vac_top = json_save.top_vacancies(top_num)
        for vac in vac_top:
            print(vac)

    elif os.path.isfile(file_path_csv):
        vac_top = csv_save.top_vacancies(top_num)
        for vac in vac_top:
            print(vac)

    else:
        print('There is no file with vacancies')


def get_all_vacancies(vacancies):
    """Function for getting all vacancies"""

    json_save = JsonSaver(vacancies, f'../job_parser/saved_vacancies/json_vacancies.json')
    csv_save = CSVSaver(vacancies, f'../job_parser/saved_vacancies/csv_vacancies.csv')

    if os.path.isfile(file_path_json):
        vac_all = json_save.load_from_file()
        for vac in vac_all:
            print(vac)

    elif os.path.isfile(file_path_csv):
        vac_all = csv_save.load_from_file()
        for vac in vac_all:
            print(vac)

    else:
        print('There is no file with vacancies')
