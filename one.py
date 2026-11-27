# 1. EMI nikalne ka function
def calculate_emi(principal, annual_rate, tenure_months):
    if annual_rate == 0:
        # Agar interest 0% hai toh simple divide karo
        emi = principal / tenure_months
    else:
        # Monthly interest rate nikalo
        r = annual_rate / 12 / 100
        # Formula: P * r * (1+r)^n / ((1+r)^n - 1)
        power = (1 + r) ** tenure_months
        emi = (principal * r * power) / (power - 1)

    # EMI ko 2 decimal places tak round karo
    return round(emi, 2)


# 2. Total payable amount nikalne ka function
def calculate_total_payable(emi, tenure_months):
    total = emi * tenure_months
    return round(total, 2)


# 3. Total interest nikalne ka function
def calculate_total_interest(total_payable, principal):
    interest = total_payable - principal
    return round(interest, 2)


# 4. Eligibility check karne ka function (EMI <= 40% of monthly income)
def check_eligibility(emi, monthly_income):
    max_emi = round(monthly_income * 0.40, 2)
    if emi <= max_emi:
        return True, max_emi
    else:
        return False, max_emi


# 5. Input sahi hai ya galat, yeh check karne ka function
def validate_inputs(principal, annual_rate, tenure_months, monthly_income):
    if principal <= 0:
        return "Invalid loan amount. Enter a positive amount."
    if annual_rate < 0 or annual_rate > 30:
        return "Invalid annual interest rate. Enter a value between 0 and 30."
    if tenure_months < 1 or tenure_months > 360:
        return "Invalid tenure. Enter a value between 1 and 360 months."
    if monthly_income <= 0:
        return "Invalid monthly income. Enter a positive amount."
    return None


# Main program yahan se start hota hai
print("=== Bank Loan Calculator ===")

# User se values lena
principal = float(input("Enter Principal Amount: "))
annual_rate = float(input("Enter Annual Interest Rate (%): "))
tenure_months = int(input("Enter Tenure (in months): "))
monthly_income = float(input("Enter Monthly Income: "))

# Pehle input validate karo
error = validate_inputs(principal, annual_rate, tenure_months, monthly_income)

if error is not None:
    print(error)
else:
    # Sab calculations call karo
    emi = calculate_emi(principal, annual_rate, tenure_months)
    total_payable = calculate_total_payable(emi, tenure_months)
    total_interest = calculate_total_interest(total_payable, principal)
    eligible, max_emi = check_eligibility(emi, monthly_income)

    # Result print karo
    print("\n--- Loan Summary ---")
    print(f"EMI: Rs. {emi:.2f} | Total Payable: Rs. {total_payable:.2f}")
    print(f"Total Interest: Rs. {total_interest:.2f} | Eligible: {'Yes' if eligible else 'No'}")

    if not eligible:
        print(f"Maximum allowed EMI (40% of income): Rs. {max_emi:.2f}")
        print("Loan not eligible: EMI exceeds the allowed limit.")
