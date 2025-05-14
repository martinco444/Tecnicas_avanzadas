pylifrom abc import ABC, abstractmethod
import copy
from typing import Dict

from abstract_document import AbstractDocument

# Prototipo concreto: Reporte
class Report(AbstractDocument):
    def __init__(self, source=None):
        self.report_data = None
        self.department = None
        self.number_of_pages = 0
        
        # Inicializar atributos de la clase padre
        super().__init__()
        
        # Si se proporciona una fuente, copiar sus atributos
        if source:
            self.__init_copy__(source)
            self.report_data = source.report_data
            self.department = source.department
            self.number_of_pages = source.number_of_pages

    # Getters y setters
    def get_report_data(self):
        return self.report_data

    def set_report_data(self, report_data):
        self.report_data = report_data

    def get_department(self):
        return self.department

    def set_department(self, department):
        self.department = department

    def get_number_of_pages(self):
        return self.number_of_pages

    def set_number_of_pages(self, number_of_pages):
        self.number_of_pages = number_of_pages

    def clone(self):
        return Report(self)

    def print(self):
        print("---- REPORTE ----")
        print(f"Titulo: {self.get_title()}")
        print(f"Autor: {self.get_author()}")
        print(f"Fecha de creacion: {self.get_creation_date()}")
        print(f"Departamento: {self.department}")
        print(f"Paginas: {self.number_of_pages}")
        print(f"Datos: {self.report_data}")
        print("--------------")

    def __str__(self):
        return f"Report [title={self.get_title()}, author={self.get_author()}, " \
               f"department={self.department}, pages={self.number_of_pages}]"

