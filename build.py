import csv
import html

def generate_html_table(csv_file_path):
    html_rows = ''
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)  # Skip the header row
        for row in reader:
            # Error handling for empty rows
        
            if not any(row):
                continue

            html_rows += '<tr>'
            for cell in row:
                html_rows += f'<td>{html.escape(cell)}</td>'
            html_rows += '</tr>\n'
    return html_rows

if __name__ == "__main__":
    csv_path = 'data.csv'  # Replace with your CSV file path
    table_html = generate_html_table(csv_path)
    
    with open('index.html', 'w') as file:
        file.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Onerank.world</title>
    <link rel="stylesheet" href="style.css">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>

     <!-- Introduction Text -->
     <header>
        <h1>onerank.world</h1>
        <p>Find all university rankings in one place at Onerank.world. It's easy and quick to compare schools without any hassle.</p>
    </header>
    <!-- Search Box -->
    <input type="text" id="searchbox" placeholder="Search by university name...">
    
    <br>

    <table id="universitiesTable">
        <thead>
            <tr><br>
                <th data-sort="name">University</th>
                <th data-sort="qs">QS Ranking</th>
                <th data-sort="shanghai">Shanghai Ranking</th>
                <th data-sort="times">Times Ranking</th>
            </tr>
        </thead>
        <tbody>
            {table_html}
        </tbody>
        
    </table>

    <script src="script.js"></script>
</body>
</html>""")
