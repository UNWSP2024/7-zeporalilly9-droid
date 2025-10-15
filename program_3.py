# Program #3: US_Population
# Author: Zepora Lilly
# Date: 10/14/2025
def main():    # Have the user input (using a loop) various information that contains three pieces of data: 
    # year, name of state, and population.  
    # Store all of this information in a list of lists.  For example it might be stored like this:
    
    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]
    all_entered_values = []
    
    # Now have the user enter a year. 
    
    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year
    print("Enter population data. Type 'done' to stop.")

    while True:
        year_input = input("Enter year (or 'done' to finish): ")
        if year_input.lower() == 'done':
            break
        try:
            year = int(year_input)
            state = input("Enter state name: ")
            population = int(input("Enter population: "))
            all_entered_values.append([year, state, population])
        except ValueError:
            print("Invalid input. Please enter numeric values for year and population.")
    # print the totalled population
    # Ask user for the year to sum
    try:
        year_to_sum = int(input("Enter the year to calculate total population for: "))
        sum_population_for_year(all_entered_values, year_to_sum)
    except ValueError:
        print("Invalid year input.")

def sum_population_for_year(all_entered_values, year_to_sum):
    total = 0
    for entry in all_entered_values:
        if entry[0] == year_to_sum:
            total += entry[2]
    print(f"Total population for {year_to_sum}: {total}")

# Call the main function.
if __name__ == '__main__':  
    main()
