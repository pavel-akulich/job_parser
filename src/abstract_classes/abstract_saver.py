from abc import ABC, abstractmethod


class GeneralStorage(ABC):
    """
        Abstract class for working with saving and loading data to/from files and performing operations on vacancies.

        This class defines a set of methods that any concrete storage class should implement to provide functionality
        for saving and loading data, as well as performing various operations on job vacancies.

        Methods:
            save_to_file(self): Abstract method to save data to a file.
            load_from_file(self): Abstract method to load data from a file.
            get_vacancies_by_salary(self, criteria): Abstract method to retrieve vacancies based on salary criteria.
            get_vacancies_by_city(self, city_criteria): Abstract method to retrieve vacancies based on city criteria.
            delete_vacancy(self, remove_criteria): Abstract method to delete a vacancy based on criteria.
            top_vacancies(self, top_number): Abstract method to retrieve the top N vacancies.
    """

    @abstractmethod
    def save_to_file(self):
        """
        Saves the data to a file.
        This method should be implemented by subclasses to define how data is saved to a file.
        """
        pass

    @abstractmethod
    def load_from_file(self):
        """
        Loads data from a file.
        This method should be implemented by subclasses to define how data is loaded from a file.
        """
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, criteria):
        """
        Retrieves vacancies based on salary criteria.
        This method should be implemented by subclasses to define how vacancies are retrieved based on salary criteria.

        Args:
            criteria: The salary criteria to filter vacancies.
        """
        pass

    @abstractmethod
    def get_vacancies_by_city(self, city_criteria):
        """
        Retrieves vacancies based on city criteria.
        This method should be implemented by subclasses to define how vacancies are retrieved based on city criteria.

        Args:
            city_criteria: The city criteria to filter vacancies.
        """
        pass

    @abstractmethod
    def delete_vacancy(self, remove_criteria):
        """
        Deletes a vacancy based on criteria.
        This method should be implemented by subclasses to define how a vacancy is deleted based on criteria.

        Args:
            remove_criteria: The criteria to identify the vacancy to be deleted.
        """
        pass

    @abstractmethod
    def top_vacancies(self, top_number):
        """
        Retrieves the top N vacancies.
        This method should be implemented by subclasses to define how the top vacancies are retrieved.

        Args:
            top_number: The number of top N vacancies to retrieve.
        """
        pass
