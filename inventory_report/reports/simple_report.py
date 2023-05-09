from datetime import datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(array: list):
        def toDate(string: str):
            return datetime.strptime(string, "%Y-%m-%d").date()

        factored = [toDate(date["data_de_fabricacao"]) for date in array]
        validate = [toDate(date["data_de_validade"]) for date in array]
        companys = Counter([comp["nome_da_empresa"] for comp in array])

        fact = min(factored).strftime("%Y-%m-%d")
        val = max(validate).strftime("%Y-%m-%d")
        comp = companys.most_common()[0]

        return f"""
        Data de fabricação mais antiga: {fact}
        Data de validade mais próxima: {val}
        Empresa com mais produtos: {comp}"""
