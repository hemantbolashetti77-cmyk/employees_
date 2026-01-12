from emp import calculate_bonus

def test_bonus_26():
    assert calculate_bonus(26) == 5000

def test_bonus_20():
    assert calculate_bonus(20) == 3000

def test_bonus_15():
    assert calculate_bonus(15) == 1500

def test_bonus_10():
    assert calculate_bonus(10) == 0
