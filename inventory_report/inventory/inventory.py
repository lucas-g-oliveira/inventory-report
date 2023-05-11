from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import json
import xml.etree.ElementTree as ET
import csv


class Inventory:
    def __from_csv(path):
        with open(path, "r") as file:
            return [*csv.DictReader(file)]

    def __from_xml(path):
        file = ET.parse(path)
        root = file.getroot()
        o_i = 0
        data = []
        for i in root:
            k_i = 0
            obj_temp = {}
            for _key in i:
                obj_temp[root[o_i][k_i].tag] = root[o_i][k_i].text
                k_i += 1
            data.append(obj_temp)
            o_i += 1
        return data

    def __from_json(path):
        with open(path) as file:
            return json.load(file)

    __report = {
        "simples": SimpleReport.generate,
        "completo": CompleteReport.generate,
    }

    __type_file = {
        "json": __from_json,
        "xml": __from_xml,
        "csv": __from_csv,
    }

    @classmethod
    def import_data(cls, path, type_report):
        file = cls.__type_file[path.split(".")[-1]](path)
        return cls.__report[type_report](file)
