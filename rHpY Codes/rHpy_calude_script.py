import pandas as pd
import os
from pathlib import Path

def process_pdb_file(input_file):
    """
    Process PDB file to calculate mean rHPy values for each residue while preserving order.
    
    Parameters:
    input_file (str): Path to input file
    """
    
    # Read the file with whitespace delimiter
    columns = ['PDB', 'Chain_ID', 'Residue_number', 'Residue_name', 
              'Group_Number', 'Group_Name', 'Buried_Fractions', 
              'Total_THpy', 'Hpys', 'rHPy']
    
    # Read the file and treat all columns as strings initially to preserve order
    df = pd.read_csv(input_file, delim_whitespace=True, names=columns, dtype={'Residue_number': str})
    
    # Select only the columns we need
    df_subset = df[['PDB', 'Chain_ID', 'Residue_number', 'Residue_name', 'rHPy']]
    
    # Group by relevant columns and calculate mean of rHPy
    # Use as_index=False to prevent automatic reordering
    result = (df_subset.groupby(['PDB', 'Chain_ID', 'Residue_number', 'Residue_name'], 
                               as_index=False)['rHPy']
              .mean())
    
    # Get unique ordered residue numbers from original file
    ordered_residues = df[['Residue_number']].drop_duplicates()
    
    # Merge with ordered residues to maintain original order
    final_result = pd.merge(ordered_residues, result, on='Residue_number')
    
    return final_result

def process_directory(input_dir):
    """
    Process all menv files in the input directory and save results in a new folder.
    
    Parameters:
    input_dir (str): Path to directory containing menv files
    """
    
    # Create output directory
    output_dir = os.path.join(input_dir, "Mean_rHPy_values")
    os.makedirs(output_dir, exist_ok=True)
    
    # Get all files in input directory
    input_files = Path(input_dir).glob("*.menv")
    
    processed_count = 0
    for input_file in input_files:
        try:
            # Process the file
            result_df = process_pdb_file(input_file)
            
            # Create output filename
            output_filename = f"{input_file.stem}_mean_rhpy.txt"
            output_path = os.path.join(output_dir, output_filename)
            
            # Save to file with tab separator
            result_df.to_csv(output_path, sep='\t', index=False)
            
            print(f"Processed {input_file.name} → {output_filename}")
            print(f"Original rows: {len(pd.read_csv(input_file, delim_whitespace=True))}")
            print(f"Processed rows: {len(result_df)}")
            print("-" * 50)
            
            processed_count += 1
            
        except Exception as e:
            print(f"Error processing {input_file.name}: {str(e)}")
    
    print(f"\nProcessing complete!")
    print(f"Total files processed: {processed_count}")
    print(f"Results saved in: {output_dir}")

if __name__ == "__main__":
    # Get the current working directory
    current_dir = os.getcwd()
    
    try:
        print("Starting file processing...")
        process_directory(current_dir)
    except Exception as e:
        print(f"Error: {str(e)}")