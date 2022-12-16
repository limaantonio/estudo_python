from utils import clear, header
from operations import auth_account, get_options_typed, do_operation


def main():
    header()
    account_auth = auth_account()

    if auth_account:
        clear()

        header()
        option_typed = get_options_typed(account_auth)
        do_operation(option_typed, account_auth)
    else:
        print('Conta inválida')

while True:
    main()

    input('Pressione <ENTER> para continuar...')  # pause do programa
