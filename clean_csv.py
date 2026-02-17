import csv
import re

# Input and output file paths
input_file = r'c:\Users\azizh\OneDrive\Bureau\MedCareAI\ModelReco.ipynb\data_reco.csv'
output_file = r'c:\Users\azizh\OneDrive\Bureau\MedCareAI\ModelReco.ipynb\data_reco_cleaned.csv'

def clean_text(text):
    """
    Remove excessive spaces (more than 2 consecutive spaces) from text.
    Also strip leading and trailing spaces from each field.
    """
    # Replace multiple spaces (3 or more) with a single space
    text = re.sub(r' {3,}', ' ', text)
    # Strip leading and trailing spaces
    text = text.strip()
    return text

# Read the CSV file and clean it
with open(input_file, 'r', encoding='utf-8', newline='') as infile:
    reader = csv.reader(infile)
    
    cleaned_rows = []
    for row in reader:
        # Clean each cell in the row
        cleaned_row = [clean_text(cell) for cell in row]
        cleaned_rows.append(cleaned_row)

# Write the cleaned data to a new CSV file
with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(cleaned_rows)

print(f"✓ CSV file cleaned successfully!")
print(f"  Input:  {input_file}")
print(f"  Output: {output_file}")
print(f"  Total rows processed: {len(cleaned_rows)}")
