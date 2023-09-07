import csv
import json
from typing import Union

from src.abstract_classes.abstract_saver import GeneralStorage
from src.models.vacancy import Vacancy


class JsonSaver(GeneralStorage):
    """
    Implementation of General Storage class for saving and loading data,
    as well as performing various operations on job vacancies in JSON format.
    """

    def __init__(self, parse_data, file_path: str) -> None:
        """
        Initializes a JsonSaver instance.

        Args:
            parse_data: Data to be saved or loaded.
            file_path: Path to the JSON file.
        """
        self.parse_data = parse_data
        self.path = file_path

    def save_to_file(self):
        """
        Saves the parse_data to a JSON file.
        """
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(self.parse_data, file, indent=4, ensure_ascii=False, default=lambda x: x.to_dict())

    def load_from_file(self) -> list[Vacancy]:
        """
        Loads data from the JSON file.

        Returns:
            Loaded data from the file.
        """
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    def get_vacancies_by_salary(self, sal_criteria: int) -> Union[list[Vacancy], str]:
        """
        Retrieves vacancies based on salary criteria.

        Args:
            sal_criteria: The salary criteria to filter vacancies.
        Returns:
            list: List of matching vacancies or an empty list if no matches found.
        """
        data_get_vac = self.load_from_file()
        matching_vacancies = []
        for vacancy in data_get_vac:
            if vacancy['salary_from'] is not None and vacancy['salary_from'] >= sal_criteria:
                matching_vacancies.append(vacancy)
        if not matching_vacancies:
            return []
        return matching_vacancies

    def get_vacancies_by_city(self, city_criteria: str) -> Union[list[Vacancy], str]:
        """
        Retrieves vacancies based on city criteria.

        Args:
            city_criteria: The city criteria to filter vacancies.
        Returns:
            list: List of matching vacancies or an empty list if no matches found.
        """
        data_city = self.load_from_file()
        matching_vacancies = []
        for vacancy in data_city:
            if city_criteria.title() in vacancy['city']:
                matching_vacancies.append(vacancy)
        if not matching_vacancies:
            return []
        return matching_vacancies

    def delete_vacancy(self, remove_criteria: str):
        """
        Deletes a vacancy from the storage based on criteria and save the updated data to the file.

        Args:
            remove_criteria: Criteria to identify the vacancy to be deleted.
        """
        data_del = self.load_from_file()
        self.parse_data = [vacancy for vacancy in data_del if vacancy['title'] != remove_criteria]
        self.save_to_file()

    def top_vacancies(self, top_number: int) -> list[Vacancy]:
        """
        Retrieves the top N vacancies from the storage.

        Args:
            top_number: The number of top N vacancies to retrieve.
        Returns:
            List of top N vacancies.
        """
        data = self.load_from_file()
        new_data = data[:top_number]

        return new_data


class CSVSaver(GeneralStorage):
    """
    Implementation of General Storage class for saving and loading data,
    as well as performing various operations on job vacancies in CSV format.
    """

    def __init__(self, parse_data, filename: str) -> None:
        """
        Initializes a CSVSaver instance.

        Args:
            parse_data: Data to be saved or loaded.
            filename: Path to the CSV file.
        """
        self.parse_data = parse_data
        self.filename = filename

    def save_to_file(self):
        """
        Saves the parse_data to a CSV file.
        """
        headers = ['title', 'vacancy_url', 'salary_from', 'salary_to', 'employer', 'city', 'requirements']

        with open(self.filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            for vacancy in self.parse_data:
                writer.writerow(vacancy.to_dict())

    def load_from_file(self) -> list[Vacancy]:
        """
        Loads data from the CSV file.

        Returns:
            Loaded data from the file.
        """
        load_data = []

        with open(self.filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                load_data.append(row)

        return load_data

    def get_vacancies_by_salary(self, sal_criteria: int) -> Union[list[Vacancy], str]:
        """
        Retrieves vacancies based on salary criteria.

        Args:
            sal_criteria: The salary criteria to filter vacancies.
        Returns:
            list: List of matching vacancies or an empty list if no matches found.
        """
        data_get_vac = self.load_from_file()
        matching_vacancies = []
        for vacancy in data_get_vac:
            if vacancy['salary_from'].isdigit() and int(vacancy['salary_from']) >= sal_criteria:
                matching_vacancies.append(vacancy)
        if not matching_vacancies:
            return []
        return matching_vacancies

    def get_vacancies_by_city(self, city_criteria: str) -> Union[list[Vacancy], str]:
        """
        Retrieves vacancies based on city criteria.

        Args:
            city_criteria: The city criteria to filter vacancies.
        Returns:
            list: List of matching vacancies or an empty list if no matches found.
        """
        data_city = self.load_from_file()
        matching_vacancies = []
        for vacancy in data_city:
            if city_criteria.title() in vacancy['city']:
                matching_vacancies.append(vacancy)
        if not matching_vacancies:
            return []
        return matching_vacancies

    def delete_vacancy(self, remove_criteria: str):
        """
        Deletes a vacancy from the storage based on criteria and save the updated data to the file.

        Args:
            remove_criteria: Criteria to identify the vacancy to be deleted.
        """
        data_delete = self.load_from_file()
        remaining_vacancies = [vacancy for vacancy in data_delete if vacancy['title'] != remove_criteria]

        headers = ['title', 'vacancy_url', 'salary_from', 'salary_to', 'employer', 'city', 'requirements']

        with open(self.filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(remaining_vacancies)

    def top_vacancies(self, top_number: int) -> list[Vacancy]:
        """
        Retrieves the top N vacancies from the storage.

        Args:
            top_number: The number of top N vacancies to retrieve.
        Returns:
            List of top N vacancies.
        """
        data = self.load_from_file()
        new_data = data[:top_number]

        return new_data
