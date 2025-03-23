#Initialize Variables
notes_values = [500,100,50,20,10,5,2,1]
n_counts = {}
n_count = 0
amounts = 0

#Get the amount from the user
amounts = float(input("Enter your amount (but less than 1000) -: "))

#Loop through the list of note values
for notes_value in notes_values:
    n_counts[notes_value] = amounts // notes_value
    amounts %= notes_value 
    
print("Number of different notes values")
for notes_value, count in n_counts.items():
    if count > 0:
        print(f"{notes_value} note: {count}")


