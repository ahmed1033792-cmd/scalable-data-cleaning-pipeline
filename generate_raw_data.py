import csv
import random

# Raw messy data containing typical real-world errors
raw_records = [
    {"user_id": "101", "name": "  Alice Smith ", "age": "28", "email": "alice@email.com", "review": "Great product! Would buy again.", "salary": "50000"},
    {"user_id": "102", "name": "bob_jones", "age": "INVALID", "email": "bob.jones#email.com", "review": "Terrible service...", "salary": "60000"},
    {"user_id": "", "name": "Charlie", "age": "35", "email": "charlie@domain.org", "review": "  Very BAD experience!!  ", "salary": "75000"},
    {"user_id": "104", "name": "David  ", "age": "42", "email": "david@company.com", "review": "Average quality, nothing special.", "salary": "NOT_NUMERIC"},
    {"user_id": "105", "name": "EVE", "age": "22", "email": "eve@test.com", "review": "AMAZING! LOVED IT!", "salary": "45000"},
    {"user_id": "101", "name": "  Alice Smith ", "age": "28", "email": "alice@email.com", "review": "Great product! Would buy again.", "salary": "50000"},  # Duplicate entry
]

def create_dirty_csv(filename="raw_data.csv"):
    fieldnames = ["user_id", "name", "age", "email", "review", "salary"]
    
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(raw_records)
        
    print(f"✅ Created dirty dataset successfully: '{filename}'")

if __name__ == "__main__":
    create_dirty_csv()