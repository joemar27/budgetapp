# Income Table
INCOME_TABLE_NAME = 'income'
INCOME_TABLE_COLUMNS = '(id int PRIMARY KEY, pay_schedule text, pay real, active int)'

# Expenses Table
EXPENSES_TABLE_NAME = 'expenses'
EXPENSES_TABLE_COLUMNS = '(id int PRIMARY KEY, item text, amount real, date text, occurances text, active int)'

# Balance Sheet Table
BALANCE_TABLE_NAME = 'running_balance'
BALANCE_TABLE_COLUMNS = '(id int PRIMARY KEY, item, amount real, date text)'

# Xmas Savings Table
XMAS_TABLE_NAME = 'xmas_buget'
XMAS_TABLE_COLUMNS = '(id int PRIMARY KEY, person text, gross_buget int, sales_tax int, notes text)'

# Sales Tax Table
SALES_TAX_TABLE_NAME = 'sales_tax'
SALES_TAX_TABLE_COLUMN = '(id int PRIMARY KEY, tax real, year int)'
