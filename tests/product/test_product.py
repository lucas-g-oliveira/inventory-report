from inventory_report.inventory.product import Product


def test_cria_produto():

    p1 = Product(
        1,
        "bol",
        "magic toys",
        "2022-02-22",
        "2023-07-30",
        "1223356648899",
        "armazene em lugar arejado com temperatura até 60Cº",
    )

    keys = [
        'nome_da_empresa',
        'nome_do_produto',
        'data_de_fabricacao',
        'data_de_validade',
        'numero_de_serie',
        'instrucoes_de_armazenamento'
        ]

    assert type(p1.id) is int
    for key in keys:
        assert type(p1[key]) is str
