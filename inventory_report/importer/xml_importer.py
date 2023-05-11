from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if path.split(".")[-1] != "xml":
            raise ValueError("Arquivo inválido")
        file = ET.parse(path)
        root = file.getroot()
        o_i = 0
        dict_data = []
        for i in root:
            k_i = 0
            obj_temp = {}
            for _key in i:
                obj_temp[root[o_i][k_i].tag] = root[o_i][k_i].text
                k_i += 1
            dict_data.append(obj_temp)
            o_i += 1
        return dict_data
