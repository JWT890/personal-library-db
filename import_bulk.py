import os
import pypyodbc as odbc

def bulk_insert_query(data_file, target_table):
    sql = f"""
    BULK INSERT {target_table}
    FROM '{data_file}'
    WITH (
            FORMAT = 'CSV',
            FIRSTROW = 2,
            FIELDTERMINATOR = ',',
            ROWTERMINATOR = '0x0a',
            FIELDQUOTE = '"',
            TABLOCK
        )
    """
    return sql.strip()

TARGET_TABLE = 'goodreads_library_export'

conn_str = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "Server=LAPTOP-TFL1BJ5M\\SQLEXPRESS;"
    "Database=personal-library;"
    "UID=bulk_import_user;"
    "PWD=StrongPassword123!;"
    "Encrypt=no;"
    "TrustServerCertificate=yes;"
)

try:
    print("Connecting to database...")
    conn = odbc.connect(conn_str)
    cursor = conn.cursor()
    print("Connected Successfully.")

    # UPDATED: Pointing directly to the new public folder
    data_file_folder = r'C:\Data_Import'

    if not os.path.exists(data_file_folder):
        print(f"Error: Folder not found at {data_file_folder}. Please create it and move your CSV there.")
    else:
        files = [f for f in os.listdir(data_file_folder) if f.endswith('.csv')]
        print(f"Found {len(files)} file(s) in {data_file_folder}.")

        for file in files:
            full_path = os.path.join(data_file_folder, file)
            print(f"Processing: {file}...")
            cursor.execute(bulk_insert_query(full_path, TARGET_TABLE))
            print(f"Success: {file} imported.")

        conn.commit()
        print("Data saved successfully.")

except Exception as e:
    print("An error occurred during processing:", e)
finally:
    if 'conn' in locals():
        conn.close()