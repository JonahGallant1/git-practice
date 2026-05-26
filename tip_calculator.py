def calculate_tip(bill_amount, tip_percent, num_people=1):
    tip = bill_amount * (tip_percent / 100)
    total = bill_amount + tip
    per_person = total / num_people
    return {
        "tip": round(tip, 2),
        "total": round(total, 2),
        "per_person": round(per_person, 2),
    }


if __name__ == "__main__":
    bill = float(input("Enter bill amount ($): "))
    tip_pct = float(input("Tip percentage (%): "))
    people = int(input("Number of people splitting: "))

    result = calculate_tip(bill, tip_pct, people)

    print(f"\nTip:        ${result['tip']}")
    print(f"Total:      ${result['total']}")
    print(f"Per person: ${result['per_person']}")
