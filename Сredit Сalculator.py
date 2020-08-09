import math
import sys


def credit_calc(params):
    credit_interest = float(params['interest']) if 'interest' in params else None
    i = credit_interest / 1200 if credit_interest is not None else None
    credit_principal = int(params['principal']) if 'principal' in params else None
    periods = int(params['periods']) if 'periods' in params else None
    annuity_payment = float(params['payment']) if 'payment' in params else None
    current_period = 0
    summa = 0
    if credit_principal is None or periods is None or annuity_payment is None or credit_interest is None or credit_principal < 0 or periods < 0 or annuity_payment < 0 or credit_interest < 0:
        print('Incorrect parameters')
    elif credit_type == 'annuity':
        if credit_principal is not None and periods is not None:  # Annuity Payment
            annuity_payment = math.ceil((credit_principal * i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1))
            print('Your annuity payment = ' + str(annuity_payment) + '!')
            print('Overpayment = ' + str(annuity_payment * periods - credit_principal))
        elif annuity_payment is not None and periods is not None:  # Credit Principal
            credit_principal = math.floor(annuity_payment / ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1)))
            print('Your credit principal = ' + str(credit_principal) + '!')
            print('Overpayment = ' + str(int(annuity_payment * periods - credit_principal)))
        elif credit_principal is not None and annuity_payment is not None:  # Count of Months
            n = math.ceil(math.log(annuity_payment / (annuity_payment - credit_principal * i), 1 + i))
            if n % 12 != 0:
                time_for_pay = 'You need ' + str(n // 12) + ' years and ' + str(n % 12) + ' months to repay this credit!'
                print(time_for_pay)
            else:
                time_for_pay = 'You need ' + str(n // 12) + ' years to repay this credit!'
                print(time_for_pay)
            print('Overpayment = ' + str(int(annuity_payment * n - credit_principal)))
    elif credit_type == 'diff':
        while current_period < periods:
            current_period = current_period + 1
            diff_payment = math.ceil(credit_principal / periods + i * (
                        credit_principal - (credit_principal * (current_period - 1)) / periods))
            summa = summa + diff_payment
            print('Month {}: paid out {}'.format(current_period, diff_payment))
        print()
        print('Overpayment = ' + str(summa - credit_principal))


params = {}
for x in range(1, len(sys.argv)):
    [key, value] = sys.argv[x].split('=')
    params[key[2:]] = value
credit_type = params['type']
if len(sys.argv) < 5:
    print('Incorrect parameters')
elif credit_type != 'diff' and credit_type != 'annuity':
    print('Incorrect parameters')
elif len(sys.argv) == 5:
    credit_calc(params)
