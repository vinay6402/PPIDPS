from flask import Flask, request
import csv

app = Flask(__name__)

@app.route('/append_csv', methods=['POST'])
def append_csv():
    my_list = request.get_json()['my_list']

    with open('webapp/my_list.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        for row in my_list:
            writer.writerow(row)

    return 'CSV file appended successfully.'

if __name__ == '__main__':
    app.run(host='192.168.24.12')
