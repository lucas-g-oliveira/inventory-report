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
        validate.sort()
        val = ""

        for d in validate:
            if d >= datetime.today().date():
                val = d.strftime("%Y-%m-%d")
                break

        fact = min(factored).strftime("%Y-%m-%d")
        comp = companys.most_common()[0][0]

        result_p1 = f"Data de fabricação mais antiga: {fact}\n"
        result_p2 = f"Data de validade mais próxima: {val}\n"
        result_p3 = f"Empresa com mais produtos: {comp}"

        return result_p1 + result_p2 + result_p3
