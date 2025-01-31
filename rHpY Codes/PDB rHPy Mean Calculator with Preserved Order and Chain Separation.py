import pandas as pd
import os
from pathlib import Path

def process_pdb_file(input_file):
    """
    Process PDB file to calculate mean rHPy values for each residue by chain.
    
    Parameters:
    input_file (str): Path to input file
    """
    
    # Read the file with whitespace delimiter
    columns = ['PDB', 'Chain_ID', 'Residue_number', 'Residue_name', 
              'Group_Number', 'Group_Name', 'Buried_Fractions', 
              'Total_THpy', 'Hpys', 'rHPy']
    
    # Read the file and treat all columns as strings initially to preserve order
    df = pd.read_csv(input_file, delim_whitespace=True, names=columns, dtype={'Residue_number': str})
    
    # Select only the columns we need in the correct order
    desired_columns = ['PDB', 'Chain_ID', 'Residue_number', 'Residue_name', 'rHPy']
    df_subset = df[desired_columns]
    
    # Process each chain separately
    unique_chains = df_subset['Chain_ID'].unique()
    all_results = []
    
    for chain in unique_chains:
        chain_data = df_subset[df_subset['Chain_ID'] == chain]
        
        # Group by relevant columns and calculate mean of rHPy
        result = (chain_data.groupby(['PDB', 'Chain_ID', 'Residue_number', 'Residue_name'], 
                                   as_index=False)['rHPy']
                 .mean())
        
        # Get unique ordered residues for this chain
        ordered_residues = chain_data[['PDB', 'Chain_ID', 'Residue_number']].drop_duplicates()
        
        # Merge with ordered residues to maintain original order
        chain_result = pd.merge(ordered_residues, result)
        
        # Append to overall results
        all_results.append(chain_result)
    
    # Combine all chain results
    final_result = pd.concat(all_results, ignore_index=True)
    
    # Ensure correct column order
    final_result = final_result[desired_columns]
    
    return final_result

def process_directory(input_dir):
    """
    Process all menv files in the input directory and save results in a new folder.
    
    Parameters:
    input_dir (str): Path to directory containing menv files
    """
    
    # Create output directory
    output_dir = os.path.join(input_dir, "Mean_rHPy_values_3")
    os.makedirs(output_dir, exist_ok=True)
    
    # Get all files in input directory
    input_files = Path(input_dir).glob("*.menv")
    
    processed_count = 0
    for input_file in input_files:
        try:
            # Process the file
            result_df = process_pdb_file(input_file)
            
            # Create separate output files for each chain
            chains = result_df['Chain_ID'].unique()
            for chain in chains:
                chain_data = result_df[result_df['Chain_ID'] == chain]
                output_filename = f"{input_file.stem}_chain_{chain}_mean_rhpy.txt"
                output_path = os.path.join(output_dir, output_filename)
                
                # Save to file with tab separator
                chain_data.to_csv(output_path, sep='\t', index=False)
                
                print(f"Processed {input_file.name} Chain {chain} → {output_filename}")
            
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