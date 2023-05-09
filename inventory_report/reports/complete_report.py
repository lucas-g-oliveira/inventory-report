from simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(array: list):
        smpl = SimpleReport.generate(array)
        complete = "\nProdutos estocados por empresa:"
        prod_per_company = Counter([comp["nome_da_empresa"] for comp in array])
        companys = []

        for i in array:
            if not (i["nome_da_empresa"]) in companys:
                companys.append(i["nome_da_empresa"])

        for comp in companys:
            complete += f"\n- {comp}: {prod_per_company[comp]}"

        return smpl + complete


data = [
    {
        "id": 1,
        "nome_do_produto": "CADEIRA",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2022-05-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar em local fresco",
    },
    {
        "id": 2,
        "nome_do_produto": "CADEIRA",
        "nome_da_empresa": "Toy",
        "data_de_fabricacao": "2012-04-04",
        "data_de_validade": "2023-05-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar em local fresco",
    },
    {
        "id": 3,
        "nome_do_produto": "CADEIRA",
        "nome_da_empresa": "Toy",
        "data_de_fabricacao": "2020-04-04",
        "data_de_validade": "2021-02-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar em local fresco",
    },
]

print(CompleteReport.generate(data))
