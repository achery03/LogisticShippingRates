#Shipping Cost Calculator

##Input package weight and shipping rate
weight = float(input("Enter the package weight in kilogram: "))
rate = float(input("Enter the shipping rate per kilogram: "))

#Calculate shipping cost
shipping_cost = weight*rate

#Display results
print(f"Shipping cost: {shipping_cost} USD")
