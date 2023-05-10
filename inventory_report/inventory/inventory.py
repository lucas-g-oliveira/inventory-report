from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import xml.etree.ElementTree as ET
import csv
import json


class Inventory:
    @staticmethod
    def __from_csv(path):
        with open(path, "r") as file:
            return [*csv.DictReader(file)]

    @staticmethod
    def __from_xml(path):
        file = ET.parse(path).getroot()
        data = {}
        for i in file:
            data[i.tag] = i.text
        return data

    @staticmethod
    def __from_json(path):
        with open(path) as file:
            return json.load(file)

    @classmethod
    def import_data(cls, path, type_report):
        report = {
            "simples": SimpleReport.generate,
            "completo": CompleteReport.generate,
        }
        type_file = {
            "json": cls.__from_json,
            "xml": cls.__from_xml,
            "csv": cls.__from_csv,
        }
        file = type_file[path.split('.')[-1]](path)
        return report[type_report](file)


csv_p1 = "/home/lucas/Documentos/1-Trybe/3-Projetos-Trybe/30 - "
csv_p2 = "Inventory Report/sd-024-b-inventory-report"
csv_p3 = "/inventory_report/data/inventory.csv"

# print(Inventory.import_data(f"{csv_p1}{csv_p2}{csv_p3}", "simples"))
print(Inventory.import_data(f"{csv_p1}{csv_p2}{csv_p3}", "completo"))
