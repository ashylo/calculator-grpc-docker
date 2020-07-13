import calculator


def test_add():
   assert calculator.add(16, 3) == 19
   assert calculator.add(23, 58) == 81
   assert calculator.add(9, 7) == 16


def test_substract():
   assert calculator.substract(16, 3) == 13
   assert calculator.substract(23, 58) == -35
   assert calculator.substract(9, 7) == 2


def test_calc_addition():
   assert calculator.calc(16, 3, '+') == 19
   assert calculator.calc(23, 58, '+') == 81
   assert calculator.calc(9, 7, '+') == 16


def test_calc_substraction():
   assert calculator.calc(16, 3, '-') == 13
   assert calculator.calc(23, 58, '-') == -35
   assert calculator.calc(9, 7, '-') == 2


def test_calc_wrong_operation():
   assert calculator.calc(16, 3, '?') == None
   assert calculator.calc(16, 3, 'hello') == None
   assert calculator.calc(16, 3, '') == None