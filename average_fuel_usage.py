from statistics import *

kms_list = []
fuel_list = []
fuel_eff = []


def main():
    while True:
        kms = float(input("Enter the number of kilometers travelled: "))
        fuel = float(input("Enter the amount of fuel filled in liters: "))
        kms_list.append(kms)
        fuel_list.append(fuel)
        efficiency = round((fuel / kms * 100), 1)
        fuel_eff.append(efficiency)
        print(f"Efficiency for this fillup: {efficiency}L/100kms")
        status = input("Are you done? Yes/No: ")
        if status.lower() == "yes":
            break
    total_fuel = sum(fuel_list)
    total_kms = sum(kms_list)
    total_eff = total_fuel / total_kms * 100
    mean_kms = sum(kms_list) / len(kms_list)
    median_kms = median(kms_list)
    min_kms = min(kms_list)
    max_kms = max(kms_list)
    print(f"Overall efficiency: {round(total_eff, 1)}L/100kms\n"
          f"Mean number of kms: {mean_kms}kms\n"
          f"Median number of kms: {median_kms}kms\n"
          f"Max number of kms: {max_kms}kms\n"
          f"Min number of kilometers: {min_kms}kms")


if __name__ == '__main__':
    main()
