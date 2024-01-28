from flask import Flask, render_template, send_file, request
from map import generate_map
from bargraph import create_bar_chart

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<filename>')
def update_content(filename):
    generate_map(filename)
    create_bar_chart(filename)

@app.route('/map-content')
def map_content():
    filename = request.args.get('filename', 'BKW_data.csv')
    map_html = generate_map(filename)
    return map_html

@app.route('/info.csv')
def serve_csv():
    return send_file('info.csv', mimetype='text/csv')

@app.route('/bar-graph-content')
def bar_graph_content():
    filename = request.args.get('filename', 'BKW_data.csv')
    bar_graph_html = create_bar_chart(filename)
    return bar_graph_html

if __name__ == '__main__':
    app.run(debug=True)