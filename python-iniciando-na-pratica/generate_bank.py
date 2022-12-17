from utils import header
from file import open_file_bank, write_money_slips, white_banks_account


def main():
    header()
    make_money_slips('w')
    file = open_file_bank('a')
    file.write('\n')
    file.close()
    make_bank_accounts('a')



def make_money_slips(mode):
    file = open_file_bank(mode)
    write_money_slips(file)
    file.close()
    print('cedulas gravada com sucesso')


def make_bank_accounts(mode):
    file = open_file_bank(mode)
    white_banks_account(file)
    file.close()
    print('contas gravadas com sucesso')

main()