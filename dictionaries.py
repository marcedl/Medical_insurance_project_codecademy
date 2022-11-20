# Add your code here
medical_costs = {}

medical_costs["Marina"] = 6607.0
medical_costs["Vinay"] = 3225.0

medical_costs.update({"Connie": 8886.0, "Isaac": 16444.0, "Valentina": 6420.0})

print(medical_costs)

medical_costs["Vinay"] = 3325.0
print(medical_costs)

total_cost = 0
for cost in medical_costs.values():
  total_cost += cost

print("Average Insurange Cost: " + str(total_cost))

names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]

ages = [27, 24, 43, 35, 52]

zipped_ages = zip(names, ages)

names_to_ages = {key: value for key, value in zipped_ages}
print(names_to_ages)

marina_age = names_to_ages.get("Marina", None)
print("Marina's age is " + str(marina_age))

medical_records = {}
