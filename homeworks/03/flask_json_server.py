from flask import Flask, request, json

app = Flask(__name__)


@app.route("/get_classifier_result/<int:version>", methods=['GET', 'POST'])
def return_classifier_result(version):
    # TODO прочитать из полученного запроса json-контент
    # В случае, если version==1, то должен вернуться json с версией и
    # полем predict из входящего jsonа {"version":1, "predict":<predict_value>}

    # В случае, если version==0, то должен вернуться json с версией и
    # полем old_predict из входящего jsonа {"version":0, "predict":<old_predict_value>}

    # GET -- получение информации от сервера
    # POST -- сервер принимает данные для хранения

    r = request.get_json()  # вытягивает json-данные из запроса POST
    if version == 1:
        return json.dumps({"version": 1, "predict": r["predict"]})
    return json.dumps({"version": 0, "predict": r["old_predict"]})


@app.route("/")
def hello():
    # TODO должна возвращатьс инструкция по работе с сервером
    instruction = 'POST data to http://127.0.0.1:5000/get_classifier_result/1 to store it with ' \
                 'version:1' + '\n' + 'and to http://127.0.0.1:5000/get_classifier_result/0 to store it with version:0'
    return instruction


if __name__ == "__main__":
    app.run()
