import pandas as pd
from fuzzywuzzy import process
import re

def normalize_name(name):
    if isinstance(name, str):
        # Lowercase and remove extra spaces
        name = name.lower().strip()
        name = ' '.join(name.split())
        # Remove special characters except for letters, digits, and spaces
        name = re.sub(r'[^a-zA-Z0-9\s]', '', name)
    return name

# Read the CSV file into a DataFrame with UTF-8 encoding
df = pd.read_csv('test.csv', encoding='utf-8')

# Normalize the university names
df['qs_name_normalized'] = df['qs_name'].apply(normalize_name)
df['times_name_normalized'] = df['times_name'].apply(normalize_name)

# Create a new DataFrame to store matches
matched_df = pd.DataFrame(columns=['qs_name', 'qs_rank', 'times_name_best_match', 'times_rank', 'score'])

# Set the maximum number of rows to process
max_rows_to_process = 604  # Change this value to your desired limit

# Perform the fuzzy matching and print rows as progress
for index, row in df.iterrows():
    if isinstance(row['qs_name_normalized'], str):
        match_result = process.extractOne(row['qs_name_normalized'], df['times_name_normalized'])
        best_match, score = match_result[0], match_result[1]
        if best_match is not None:
            times_rank = df.loc[df['times_name_normalized'] == best_match, 'times_rank'].values[0]
            matched_df = matched_df.append({
                'qs_name': row['qs_name'],
                'qs_rank': row['qs_rank'],
                'times_name_best_match': best_match,
                'times_rank': times_rank,
                'score': score
            }, ignore_index=True)
        # Print the row number as progress
        print(f"Processed row {index + 1}/{len(df)}")

        # Check if the maximum number of rows to process has been reached
        if index + 1 >= max_rows_to_process:
            break  # Exit the loop if the limit is reached

# Save the matched DataFrame to a new CSV file with UTF-8 encoding for review
matched_df.to_csv('matched_university_rankings_times.csv', index=False, encoding='utf-8')
# Print completion message
print("Fuzzy matching completed.")
