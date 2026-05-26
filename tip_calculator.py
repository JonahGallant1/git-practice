TIP_PRESETS = {"low": 15, "standard": 18, "generous": 20, "excellent": 25}


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

    print("Tip presets: " + ", ".join(f"{k} ({v}%)" for k, v in TIP_PRESETS.items()))
    tip_input = input("Tip % or preset name: ").strip().lower()
    tip_pct = TIP_PRESETS.get(tip_input, float(tip_input))

    people = int(input("Number of people splitting: "))

    result = calculate_tip(bill, tip_pct, people)

    print(f"\nTip:        ${result['tip']}")
    print(f"Total:      ${result['total']}")
    print(f"Per person: ${result['per_person']}")
