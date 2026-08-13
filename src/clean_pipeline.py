import pandas as pd
import re
import os

def clean_file_path(path_str):
    """Removes PowerShell prefix '&', single/double quotes, and trailing whitespace."""
    if not path_str:
        return ""
    path_str = path_str.strip()
    # Remove leading PowerShell '&' command prefix if present
    if path_str.startswith('&'):
        path_str = path_str[1:].strip()
    # Remove surrounding single or double quotes
    path_str = path_str.strip("'\"")
    return path_str

def clean_data_pipeline(input_file, output_file="cleaned_data.csv"):
    # Strip invalid path artifacts from Terminal/PowerShell drag & drop
    input_file = clean_file_path(input_file)
    
    print(f"\n🚀 Starting Data Cleaning Pipeline on: '{input_file}'...\n")
    
    if not os.path.exists(input_file):
        print(f"❌ Error: File '{input_file}' not found. Please check the path and try again.")
        return None
    
    # 1. Ingest Data
    df = pd.read_csv(input_file)
    print(f"📊 Initial Rows Loaded: {len(df)}")
    
    # 2. Drop Exact Duplicates
    df = df.drop_duplicates()
    print(f"✔️ Removed duplicates. Remaining rows: {len(df)}")
    
    # 3. Handle Missing / Invalid user_id if column exists
    if 'user_id' in df.columns:
        df = df.dropna(subset=['user_id'])
        df['user_id'] = pd.to_numeric(df['user_id'], errors='coerce')
        df = df.dropna(subset=['user_id'])
        df['user_id'] = df['user_id'].astype(int)
    
    # 4. Clean Text Fields (strip spaces & fix casing)
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype(str).str.strip()
    
    if 'name' in df.columns:
        df['name'] = df['name'].str.title()
    
    # 5. Safely handle numeric fields (like age or salary)
    for num_col in ['age', 'salary']:
        if num_col in df.columns:
            df[num_col] = pd.to_numeric(df[num_col], errors='coerce')
            median_val = df[num_col].median()
            df[num_col] = df[num_col].fillna(median_val)
    
    # 6. Validate Email Syntax if column exists
    if 'email' in df.columns:
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        valid_email_mask = df['email'].astype(str).str.match(email_regex)
        invalid_emails = df[~valid_email_mask]['email'].tolist()
        if invalid_emails:
            print(f"⚠️ Flagged invalid emails: {invalid_emails}")
            df.loc[~valid_email_mask, 'email'] = "invalid_email@flagged.com"
        
    # 7. Export Clean Dataset
    df.to_csv(output_file, index=False)
    print(f"\n✅ Pipeline Complete! Clean dataset saved as '{output_file}'")
    return output_file

if __name__ == "__main__":
    user_file = input("📁 Enter the path or filename of your raw CSV file: ")
    clean_data_pipeline(user_file)