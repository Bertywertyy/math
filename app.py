from flask import Flask, render_template, request
import statistics

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        numbers = request.form.getlist('numbers')
        numbers = [float(num) for num in numbers if num]
        
        if len(numbers) > 0:
            stats = {
                'mean': statistics.mean(numbers),
                'median': statistics.median(numbers),
                'mode': statistics.mode(numbers) if len(set(numbers)) != len(numbers) else '無',
                'stdev': statistics.stdev(numbers),
                'variance': statistics.variance(numbers),
                'pstdev': statistics.pstdev(numbers),
                'pvariance': statistics.pvariance(numbers)
            }
            return render_template('results.html', stats=stats, numbers=numbers)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
