import csv
import html
import shutil
import os

def generate_html_table(csv_file_path):
    html_rows = ''
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        # Specify UTF-8 encoding
        reader = csv.reader(csvfile)
        next(reader, None)  # Skip the header row
        for row in reader:
            if not any(row):
                continue
            html_rows += '<tr>'
            for cell in row:
                html_rows += f'<td><span>{html.escape(cell)}</span></td>'
            html_rows += '</tr>\n'
    return html_rows


def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def copy_directory(source_dir, destination_dir):
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)  # Delete the existing destination directory and its contents
    shutil.copytree(source_dir, destination_dir)

def copy_files(source_dir, destination_dir):
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        destination_item = os.path.join(destination_dir, item)
        if os.path.isfile(source_item):
            shutil.copy(source_item, destination_item)

def assemble_html(table_html):
    # Copy specific directories from the root directory to the "public" directory
    copy_directory('icons', 'public/icons')
    copy_directory('js', 'public/js')
    copy_directory('css', 'public/css')
    copy_files('pages', 'public')

    # Continue with assembling HTML as before
    header_html = read_html_file('layouts/header.html')
    body_html = read_html_file('layouts/body.html').replace('<!-- Table Placeholder -->', table_html)
    footer_html = read_html_file('layouts/footer.html')

    complete_html = header_html + body_html + footer_html

    with open('public/index.html', 'w', encoding='utf-8') as file:
        file.write(complete_html)

if __name__ == "__main__":
    table_html = generate_html_table('data/data.csv')
    assemble_html(table_html)
