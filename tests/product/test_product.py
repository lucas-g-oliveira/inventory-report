from inventory_report.inventory.product import Product


def test_cria_produto():
    values = [
        1,
        "bol",
        "magic toys",
        "2022-02-22",
        "2023-07-30",
        "1223356648899",
        "armazene em lugar arejado com temperatura até 60Cº",
    ]

    prod = Product(*values)

    assert values[0] is prod.id
    assert values[1] is prod.nome_do_produto
    assert values[2] is prod.nome_da_empresa
    assert values[3] is prod.data_de_fabricacao
    assert values[4] is prod.data_de_validade
    assert values[5] is prod.numero_de_serie
    assert values[6] is prod.instrucoes_de_armazenamento
