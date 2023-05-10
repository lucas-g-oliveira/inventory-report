from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(array: list):
        smpl = SimpleReport.generate(array)
        complete = "Produtos estocados por empresa:\n"
        prod_per_company = Counter([comp["nome_da_empresa"] for comp in array])
        companys = []

        for i in array:
            """ print(i['nome_da_empresa']) """
            if not (i["nome_da_empresa"]) in companys:
                companys.append(i["nome_da_empresa"])

        for comp in companys:
            complete += f"- {comp}: {prod_per_company[comp]}\n"

        """ print(companys) """

        return f"""{smpl}
{complete}"""
