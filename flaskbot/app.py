from flask import Flask,render_template, request


from chatBotRaw.mainn import *

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('indext.html')



@app.route('/process',methods=['POST'])
def process():
    while True:
        user_input = request.form['user_input']
        if user_input.lower() == "bye":
            break
        bot_response = str(chat(user_input))
        print("shondesh: " + bot_response)
        return render_template('indext.html', user_input=user_input,
                               bot_response=bot_response
                               )



if __name__ == '__main__':
    app.run(debug=True)



