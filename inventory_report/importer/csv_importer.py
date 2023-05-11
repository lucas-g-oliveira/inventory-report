from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if path.split(".")[-1] != "csv":
            raise ValueError("Arquivo inválido")
        with open(path, "r") as file:
            dict_data = [*csv.DictReader(file)]
            return dict_data
