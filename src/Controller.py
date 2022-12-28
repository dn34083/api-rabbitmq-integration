import os
from flask import Flask, jsonify, make_response, request
import services.Rabbit as Rabbit

app = Flask(__name__)
app.config["DEBUG"] = False


UPLOAD_DIRECTORY = "/opt/rabbitFiles"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

@app.route('/rabbit/post/<filename>', methods=['POST'])
def postMessageRabbit(filename):  
    if "/" in filename:
            # Return 400 BAD REQUEST
        return make_response(
                jsonify(
                    {"message": "File not found"}
                ),
                400,
        )

    try:
        with open(os.path.join(UPLOAD_DIRECTORY, filename), "wb") as fp:
            fp.write(request.data)
    except Exception as e:
        return make_response(
                jsonify(
                    {"message": "Erro saving file",
                    "Exception":e}
                ),
                403,
        )

    retorno = Rabbit.postMessage(request.headers['host'],request.headers['user'],request.headers['password'],request.headers['vh'],request.headers['queue'],UPLOAD_DIRECTORY+'/'+filename)

    return make_response(
                jsonify(
                    {"message": retorno}
                ),
                200,
    )  


app.run(host='0.0.0.0',port=5000)   