import price_info

def test_total_cost_shopping():
    result = 0
    total_cost = 46.75
    result = price_info.total_cost_shopping()

    assert (result == total_cost)

def test_cost_of_fruits():
    result = 0
    fruit_type = 'watermelon'
    quantity = 1

    result = price_info.cost_of_fruits(fruit_type,quantity)
    assert result == 6.5

