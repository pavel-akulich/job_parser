from abc import ABC, abstractmethod


class GeneralAPI(ABC):
    """Abstract class for working with the API"""

    @abstractmethod
    def get_vacancies(self, name: str, salary: int, quantity: int) -> dict:
        """
        Fetches job vacancies from the API.

        :param name: Name of the job vacancy.
        :param salary: Desired salary for the vacancy.
        :param quantity: Number of vacancies to retrieve.
        :return: Dictionary containing job vacancy data.
        """
        pass

    @abstractmethod
    def parse(self, data: dict) -> list:
        """
        Parses raw API data into a structured format.

        :param data: Raw data from the API.
        :return: List of parsed and structured Vacancy objects.
        """
        pass
