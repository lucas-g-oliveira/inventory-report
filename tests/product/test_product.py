import pytest
import datetime
from inventory_report.inventory.product import Product


@pytest.xfail
def test_cria_produto():

    prod1 = Product(
        1,
        "bol",
        "magic toys",
        datetime.now(),
        datetime.date(2100, 5, 15),
        "1223356648899",
        "armazene em lugar arejado com temperatura até 60Cº",
    )

    attributes = [
        "nome_da_empresa",
        "nome_do_produto",
        "data_de_fabricacao",
        "data_de_validade",
        "numero_de_serie",
        "instrucoes_de_armazenamento",
    ]

    assert type(prod1.id) == int

    for attr in attributes:
        assert type(prod1[attr]) == str
