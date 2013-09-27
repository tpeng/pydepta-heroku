from flask import Flask, request, render_template
from pydepta import Depta

app = Flask(__name__)

@app.route('/')
def pydepta():
    url = request.args.get('url')
    print url
    if url:
        depta = Depta()
        regions = depta.extract(url=url)
        tables = [[i, region.as_html_table().decode('utf-8')] for i, region in enumerate(regions)]
        return render_template('tables.html', tables=tables)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()