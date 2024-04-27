import csv
import html

def generate_html_table(csv_file_path):
    html_rows = ''
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:  # Specify UTF-8 encoding
        reader = csv.reader(csvfile)
        next(reader, None)  # Skip the header row
        for row in reader:
            if not any(row):
                continue
            html_rows += '<tr>'
            for cell in row:
                html_rows += f'<td>{html.escape(cell)}</td>'
            html_rows += '</tr>\n'
    return html_rows


def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def assemble_html(table_html):
    header_html = read_html_file('layouts/header.html')
    body_html = read_html_file('layouts/body.html').replace('<!-- Table Placeholder -->', table_html)
    footer_html = read_html_file('layouts/footer.html')

    complete_html = header_html + body_html + footer_html

    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(complete_html)

if __name__ == "__main__":
    table_html = generate_html_table('data/data.csv')
    assemble_html(table_html)
