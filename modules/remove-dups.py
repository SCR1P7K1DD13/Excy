import pandas as pd
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

def remove_duplicates(input_file, output_file, columns):

    # Remove duplicate rows based on specified columns
    df.drop_duplicates(subset=columns, inplace=True)

    # Write the DataFrame with duplicates removed to a new Excel file
    df.to_excel(output_file, index=False)
    print(Fore.GREEN + f"\nDuplicate entries removed based on columns {columns}. Result saved to {output_file}")

if __name__ == "__main__":
    # Get input and output file names from the user
    input_file = input(Fore.YELLOW + "Enter the path of the input Excel file: ")
    output_file = input(Fore.YELLOW + "Enter the path of the output Excel file: ")
     
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(input_file)
    print(Fore.CYAN + "Columns in the Excel file:")
    print(df.columns.tolist())

    # Get the column(s) for identifying duplicates from the user
    columns = input(Fore.YELLOW + "Enter the column(s) (comma-separated) for identifying duplicates: ").split(',')

    # Call the function to remove duplicates based on specified columns
    remove_duplicates(input_file, output_file, columns)
