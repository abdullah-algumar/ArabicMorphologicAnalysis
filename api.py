from flask import Flask, make_response, jsonify
from nlp_naftawayh import nlp_naf

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
@app.route('/morfolojik/<string:sentence>', methods=['GET', 'POST'])
def find_stem(sentence):
    try:
        nlp_result = nlp_naf(sentence)
        result = {'message': 'SUCCESS', 'result': nlp_result}
        return make_response(jsonify(result), 200)
    except:
        print('CALISMADI')
        result = {'message': 'FAILED'}
        return make_response(jsonify(result), 404)


if __name__ == '__main__':
    app.run(debug=True)
