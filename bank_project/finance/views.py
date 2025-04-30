from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def emi_calculator(request):
    result = None
    if request.method == 'POST':
        principal = float(request.POST['principal'])
        rate = float(request.POST['rate'])
        tenure = int(request.POST['tenure'])

        monthly_rate = rate / (12 * 100)
        months = tenure * 12
        emi = principal * monthly_rate * ((1 + monthly_rate) ** months) / (((1 + monthly_rate) ** months) - 1)
        result = round(emi, 2)

    return render(request, 'finance_tools/emi_calculator.html', {'result': result})

def sip_calculator(request):
    result = None
    if request.method == 'POST':
        monthly_investment = float(request.POST['monthly_investment'])
        rate = float(request.POST['rate'])
        years = int(request.POST['years'])

        monthly_rate = rate / (12 * 100)
        months = years * 12
        maturity = monthly_investment * (((1 + monthly_rate) ** months - 1) * (1 + monthly_rate)) / monthly_rate
        result = round(maturity, 2)

    return render(request, 'finance/sip_calculator.html', {'result': result})


def rd_calculator(request):
    result = None
    if request.method == 'POST':
        monthly_investment = float(request.POST['monthly_investment'])
        rate = float(request.POST['rate'])
        years = int(request.POST['years'])

        tenure_months = years * 12
        monthly_rate = rate / (100 * 12)

        maturity = monthly_investment * tenure_months + \
                   monthly_investment * (tenure_months * (tenure_months + 1) / 2) * monthly_rate

        result = round(maturity, 2)

    return render(request, 'finance/rd_calculator.html', {'result': result})


def retirement_savings_view(request):
    result = None
    if request.method == 'POST':
        current_savings = float(request.POST['current_savings'])
        monthly_contribution = float(request.POST['monthly_contribution'])
        annual_rate = float(request.POST['annual_rate'])
        years_until_retirement = int(request.POST['years_until_retirement'])

        monthly_rate = annual_rate / (12 * 100)
        months = years_until_retirement * 12
        future_value = current_savings * ((1 + monthly_rate) ** months) + \
                       monthly_contribution * (((1 + monthly_rate) ** months - 1) * (1 + monthly_rate)) / monthly_rate

        result = round(future_value, 2)

    return render(request, 'finance/retirement_calculator.html', {'result': result})


def calculate_credit_card_balance(balance, annual_rate, months, min_payment_rate=0.05):

   
    
    if balance <= 0 or annual_rate < 0 or months <= 0:
        raise ValueError("Invalid input values")

    monthly_rate = annual_rate / 12 / 100
    for _ in range(months):
        min_payment = balance * min_payment_rate
        interest = balance * monthly_rate
        balance = balance - min_payment + interest
    return round(balance, 2)


def credit_card_calculator_view(request):
    result = None
    if request.method == 'POST':
        try:
            balance = float(request.POST['balance'])
            annual_rate = float(request.POST['annual_rate'])
            months = int(request.POST['months'])
            result = calculate_credit_card_balance(balance, annual_rate, months)
        except (ValueError, KeyError):
            result = "Invalid input. Please enter valid numbers."
    return render(request, 'finance/credit_card_calculator.html', {'result': result})

def calculate_taxable_income(gross_income, deductions=50000):
    """
    Calculate taxable income after standard deduction.

    Parameters:
    gross_income (float): Total gross income
    deductions (float): Deduction amount (default ₹50,000)

    Returns:
    float: Taxable income
    """
    if gross_income < 0 or deductions < 0:
        raise ValueError("Income and deductions must be non-negative")

    taxable_income = gross_income - deductions
    return round(max(taxable_income, 0), 2)

def plan_budget(income, fixed_expenses, variable_expenses):
    """
    Plan a simple budget based on income and expenses.

    Parameters:
    income (float): Monthly income
    fixed_expenses (float): Total fixed expenses
    variable_expenses (float): Total variable expenses

    Returns:
    dict: Summary of savings and suggestions
    """
    if income <= 0 or fixed_expenses < 0 or variable_expenses < 0:
        raise ValueError("Invalid input values")

    total_expenses = fixed_expenses + variable_expenses
    savings = income - total_expenses
    suggestion = "Increase savings" if savings < 0.2 * income else "Good saving habit"
    return {
        "Total Expenses": round(total_expenses, 2),
        "Savings": round(savings, 2),
        "Suggestion": suggestion
    }

def taxable_income_view(request):
    result = None
    if request.method == 'POST':
        try:
            gross_income = float(request.POST['gross_income'])
            deductions = float(request.POST.get('deductions', 50000))  # default 50,000
            result = calculate_taxable_income(gross_income, deductions)
        except (ValueError, KeyError):
            result = "Invalid input. Please enter valid numbers."
    return render(request, 'finance/taxable_income.html', {'result': result})


def budget_planner_view(request):
    result = None
    if request.method == 'POST':
        try:
            income = float(request.POST['income'])
            fixed_expenses = float(request.POST['fixed_expenses'])
            variable_expenses = float(request.POST['variable_expenses'])
            result = plan_budget(income, fixed_expenses, variable_expenses)
        except (ValueError, KeyError):
            result = "Invalid input. Please enter valid numbers."
    return render(request, 'finance/budget_planner.html', {'result': result})

def calculate_net_worth(assets: dict, liabilities: dict):
    """
    Calculate net worth from assets and liabilities.

    Parameters:
    assets (dict): Dictionary of asset values
    liabilities (dict): Dictionary of liability values

    Returns:
    float: Net worth
    """
    if not isinstance(assets, dict) or not isinstance(liabilities, dict):
        raise TypeError("Assets and liabilities must be dictionaries")

    total_assets = sum(assets.values())
    total_liabilities = sum(liabilities.values())

    if total_assets < 0 or total_liabilities < 0:
        raise ValueError("Asset and liability values must be non-negative")

    return round(total_assets - total_liabilities, 2)

def net_worth_view(request):
    result = None
    if request.method == 'POST':
        try:
            assets = {
                'cash': float(request.POST['cash']),
                'investments': float(request.POST['investments']),
                'property': float(request.POST['property'])
            }
            liabilities = {
                'loans': float(request.POST['loans']),
                'credit_cards': float(request.POST['credit_cards']),
                'other_debts': float(request.POST['other_debts'])
            }
            result = calculate_net_worth(assets, liabilities)
        except (ValueError, KeyError):
            result = "Invalid input. Please enter valid numbers."
    return render(request, 'finance/net_worth.html', {'result': result})