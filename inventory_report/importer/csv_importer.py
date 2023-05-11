from inventory_report.importer.importer import Importer
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path: str, type: str) -> str:
        if path.split(".")[-1] != "csv":
            raise ValueError("Arquivo inválido")
        with open(path, "r") as file:
            dict_data = [*csv.DictReader(file)]
            if type == "simples":
                SimpleReport.generate(dict_data)
            elif type == "completo":
                CompleteReport.generate(dict_data)
            else:
                raise ValueError()
