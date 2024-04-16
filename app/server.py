from flask import Flask
from flask import render_template
from html import escape
from faker import Faker
from tabulate import tabulate

app = Flask(__name__)

@app.route("/")
def frontpage():
    message= "Hello, Dev!"
    html_table = generate_html_table(num_rows=5)
    return render_template('frontpage.html', message=message, table=html_table)

def generate_html_table(num_rows=5):
    faker = Faker()
    data = []
    for _ in range(num_rows):
        name = escape(faker.name())
        email = escape(faker.email())
        phone = escape(faker.phone_number())
        data.append([name, email, phone])
    headers = ["Nome", "Email", "Telefone"]
    return tabulate(data, headers=headers, tablefmt="html")