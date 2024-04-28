import math
def calculate_ci(principal_amount,down_payment,loan_year,interest_percentage,frequency):
    n = 12 if frequency == 'Monthly' else 1
    total_payments = n*loan_year
    interest_rate = interest_percentage/100
    monthly_interest = interest_rate/n
    total_pay_amount = (principal_amount - down_payment)*((1 + (interest_rate / n))**(loan_year*n))
    single_month_installment = (principal_amount-down_payment)*(
                                (monthly_interest*((1+monthly_interest)**total_payments))/
                                (((1+monthly_interest)**total_payments) - 1))
    return(total_pay_amount,single_month_installment)

def Calculate_Downpayment(principal_amount,down_payment_in_percentage):
    return ((principal_amount*down_payment_in_percentage)/100)

total_payment, monthly_installment = calculate_ci(1260000,300000,8,10,"Monthly")
total_payment2, monthly_installment2 = calculate_ci(1260000,0,10,8,"Monthly")
print('1st Total Payment is {} & 1st Monthly Installment is {}'.format(math.ceil(total_payment)
                                                               ,math.ceil(monthly_installment)))
print('2nd Total Payment is {} & 2nd Monthly Installment is {}'.format(math.ceil(total_payment2)
                                                               ,math.ceil(monthly_installment2)))


house_total_payment, house_monthly_installment = calculate_ci(
    principal_amount=800000,
    down_payment=Calculate_Downpayment(
        principal_amount=800000,
        down_payment_in_percentage=25
    ),
    loan_year=6,
    interest_percentage=7,
    frequency="Monthly"
)
bike_total_payment, bike_monthly_installment = calculate_ci(
    principal_amount=60000,
    down_payment=0,
    loan_year=1,
    interest_percentage=12,
    frequency="Monthly"
)
print('Shaun Total Payment is {} & Monthly Installment is {}'.format(math.ceil(house_total_payment+bike_total_payment)
                                                               ,math.ceil(house_monthly_installment+bike_monthly_installment)))
