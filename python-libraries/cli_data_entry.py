# Import necessary libraries
from rich.console import Console
from rich.table import Table
import pandas as pd
import os

# Create a Console instance
console = Console()
console.print("Here is some Current PGA Tour Player Data", style="bold cyan")

# Create table
table = Table(title="Top PGA Tour Players")

# Define table columns
table.add_column("Player's Name", justify="left", style="blue", no_wrap=True)
table.add_column("Country", justify="left", style="green")
table.add_column("Ranking Points", style="red")

# Add top PGA Tour players data
table.add_row("Scottie Scheffler", "United States", "17.090")
table.add_row("Xander Schauffele", "United States", "10.860")
table.add_row("Rory McIlroy", "Northern Ireland", "8.530")
table.add_row("Collin Morikawa", "United States", "N/A")

# Print the table to the console
console.print(table)

console.print("\n[bold green]Enter Your Favorite Golf Player:[/bold green]")

# Function to get user input
def get_user_input():
    player_name = input("Enter the player's name: ")
    country = input("Enter the player's country: ")
    ranking = input("Enter the player's ranking (or N/A): ")
    return player_name, country, ranking

# Function to confirm data
def confirm_data(player_name, country, ranking):
    console.print(f"\n[bold yellow]Please confirm the data you entered:[/bold yellow]")
    console.print(f"Player Name: {player_name}")
    console.print(f"Country: {country}")
    console.print(f"Ranking: {ranking}")
    return input("\nIs the data correct? (yes/no): ").strip().lower() == 'yes'

# Function to save data to a file
def save_data_to_file(data, filename="golf_data.csv"):
    df = pd.DataFrame(data, columns=["Player Name", "Country", "Ranking"])
    df.to_csv(filename, index=False)
    console.print(f'Data saved to {os.path.abspath(filename)}')

# Main function to run the script
def main():
    golf_data = []
    
    while True:
        player_name, country, ranking = get_user_input()

        if confirm_data(player_name, country, ranking):
            golf_data.append([player_name, country, ranking])
            console.print("\n[bold green]Data added.[/bold green]")
        else:
            console.print("\n[bold red]Please re-enter the data.[/bold red]")
            continue

        if input("\nDo you want to add another player? (yes/no): ").strip().lower() != 'yes':
            break
    
    # Save the data to CSV file
    save_data_to_file(golf_data)

if __name__ == "__main__":
    main()
