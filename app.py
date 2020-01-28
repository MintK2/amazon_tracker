from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/Apple-AirPods-Charging-Latest-Model/dp/B07PXGQC1Q/ref=sr_1_1_sspa?crid=2QOXCDI0L1YQ&keywords=airpods&qid=1580093793&sprefix=airpods%2Caps%2C160&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExMUlTTzFMMU0wUloyJmVuY3J5cHRlZElkPUEwNzI2NzEwMUIzOFFNNDRQRjg4RSZlbmNyeXB0ZWRBZElkPUExMDA0ODcwREJCVUpMV1FWMk9MJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()