import pandas as pd
from colorama import Fore, Style

def search_and_save_results():
    # Ask the user for file paths
    file1_path = input("Enter the path of the first Excel file: ")
    file2_path = input("Enter the path of the second Excel file: ")
    output_file_path = input("Enter the path for the output Excel file (press Enter for default): ")

    # Load the Excel files into DataFrames
    df_search = pd.read_excel(file1_path)
    df_data = pd.read_excel(file2_path)

    # Print headings for user identification
    print("\n" + Fore.GREEN + "Headings in the first Excel file:" + Style.RESET_ALL)
    print(list(df_search.columns))

    print("\n" + Fore.GREEN + "Headings in the second Excel file:" + Style.RESET_ALL)
    print(list(df_data.columns))

    # Ask the user for the column to search
    search_column = input("\n" + Fore.GREEN + "Enter the column name from the first Excel file for search:" + Style.RESET_ALL + " ")

    # Perform the search
    result_df = df_data[df_data[search_column].isin(df_search[search_column])]

    # Save the results to the output Excel file
    if not output_file_path:
        output_file_path = "output_results.xlsx"

    result_df.to_excel(output_file_path, index=False)

    print(f"\nResults saved to {Fore.RED}{output_file_path}{Style.RESET_ALL}")

# Example usage
search_and_save_results()
