import tabula
import pandas as pd
import os

pdf_file_path = 'C:\All codes\python Project\pdfs\Id3.pdf'  # or the correct path
if os.path.exists(pdf_file_path):
    print("File found!")
else:
    print("File not found, please check the path.")


# Extract tables from the PDF using Tabula
# pages='all' extracts from all pages; specify a page number if needed
tables = tabula.read_pdf(pdf_file_path, pages='all', multiple_tables=True)

# Convert each table to JSON
json_tables = []
for table in tables:
    json_table = table.to_json(orient='records')  # Convert the DataFrame to JSON
    json_tables.append(json_table)

# Print or save the JSON data
for index, json_table in enumerate(json_tables):
    print(f"Table {index+1}:")
    print(json_table)

# Optionally, you can write the JSON data to a file
with open('output.json', 'w') as json_file:
    json_file.write(str(json_tables))
