from utils import clear, header
from operations import auth_account, get_options_typed, do_operation
from file import load_bank_data
from bank_account_variables import money_slips, accounts_list


def main():
    load_bank_data()
    print(money_slips)
    print(accounts_list)
    header()
    account_auth = auth_account()

    if auth_account:
        clear()

        header()
        option_typed = get_options_typed(account_auth)
        do_operation(option_typed, account_auth)
    else:
        print('Conta inválida')

if __name__ == '__main__':
    while True:
        main()

        input('Pressione <ENTER> para continuar...')  # pause do programa
