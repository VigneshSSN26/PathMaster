from flask import Flask, render_template, request
from tsp.dynamic_programming import solve_tsp_dp
from tsp.nearest_neighbour import solve_tsp_nn

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        cities = request.form.getlist('cities')
        distances = [[int(x) for x in row.split(',')] for row in request.form.getlist('distances')]
        method = request.form['method']
        if method == 'dp':
            result = solve_tsp_dp(distances)
        else:
            result = solve_tsp_nn(distances)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
