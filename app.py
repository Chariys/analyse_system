
from flask import Flask, render_template
import pandas as pd

data = pd.read_excel(r'E:\python project\analyze\就业情况数据.xls')

guangdong_sum = 0
other_sum = 1
site = data['生源地']
for i in site:
    if i.startswith('广东省'):
        guangdong_sum += 1
    else:
        other_sum += 1
data_sum = {}
data_sum[guangdong_sum] = guangdong_sum
data_sum[other_sum] = other_sum
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('/index.html')


if __name__ == '__main__':
    app.run(debug=True)
