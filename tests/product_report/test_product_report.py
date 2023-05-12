from inventory_report.inventory.product import Product


def test_relatorio_produto():
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

    assert str(prod) == (
        f"O produto {values[1]}"
        f" fabricado em {values[3]}"
        f" por {values[2]} com validade"
        f" até {values[4]}"
        f" precisa ser armazenado {values[6]}."
    )
