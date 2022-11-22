from flask import Flask
from pyspark.sql import SparkSession

app = Flask("App_Name")


@app.route('/myFirstApi', methods=['GET'])
def factorial():
    n = 4
    mul = 1
    for i in range(1, n + 1):
        mul = mul * i

    return str(mul)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
