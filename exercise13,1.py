from flask import Flask

app = Flask(__name__)

@app.route('/prime_number/<int:number>')
def check_prime(number):

    if number <= 1:
        isPrime = False
    else:
        isPrime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                isPrime = False
                break

    return {
        "Number": number,
        "isPrime": isPrime
    }


if __name__ == '__main__':
    app.run(debug=True)