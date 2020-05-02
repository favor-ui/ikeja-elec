from flask import jsonify, request, abort
from app import app, mongo, cur_time_and_date



@app.route('/')
def home():
    try:
        return jsonify(
            {
                "Message":"Welcome",
                "status":1
                }
                )
    except Exception:
        return jsonify({"Message":"Something went wrong Please check"})


@app.route('/ikeja_electic_transaction', methods = ['GET'])
def get_all_transactions():
    """This route gets data from the database by specifying mongo.<dbname>.<collection name>.find_one"""
    try:
        transactions = mongo.db.transactions_
        
        output = []

        for r in transactions.find():
            output.append({
                        'account_number':r['account_number'],
                        'account_type':r['account_type'],
                        'transaction_value':r['transaction_value'],
                        'transaction_ref':r['transaction_ref'],
                        'token':r['token'
                        ]})
        
        return jsonify({'result' : output})
    except Exception:
        return jsonify({"Message":"Something went wrong Please check"})




@app.route('/ikeja_electic_transaction', methods = ['POST'])
def register():
    """This route saves data to database by specifying mongo.<dbname>.<collection name>.insert()"""
    try:
        transactions = mongo.db.transactions_
        request_data = request.get_json()
        account_number1 = request_data['account_number']
        account_number= int(account_number1)
        if not account_number:
            return jsonify({"Error":"Field can not be blank", "status":0})
        
        account_type1 = request_data['account_type']
        account_type = str(account_type1)
        if not account_type:
            return jsonify({"Error":"Field can not be blank", "status":0})
        
        transaction_val = request_data['transaction_value']
        transaction_value = int(transaction_val)
        if not transaction_value:
            return jsonify({"Error":"Field can not be blank", "status":0})
        
        transaction_ref1 = request_data['transaction_ref']
        transaction_ref = str(transaction_ref1)
        if not transaction_ref:
            return jsonify({"Error":"Field can not be blank", "status":0})
        
        token1 = request_data['token']
        token = str(token1)
        if not token:
            return jsonify({"Error":"Field can not be blank", "status":0})
        
        find_reg_id ={'account_number':account_number,
                                    'account_type':account_type,
                                    'transaction_value':transaction_value,
                                    'transaction_ref':transaction_ref,
                                    'token':token}
        
        q = transactions.find_one(find_reg_id) 
    
        if q:
            return jsonify({"Error":"Transaction has been save", "status":0})
        else:
            reg_id = transactions.insert_one(find_reg_id)

        return jsonify({"Message": "Transaction has been saved", "status":1})

    except Exception:
        return jsonify({"Message":"Something went wrong Please check"})




@app.errorhandler(400)
def bad_request__error(exception):
    return jsonify(
        {
            "Message": "Sorry you entered wrong values kindly check and resend!"
        },
        {
            "status":400
        }
    )


@app.errorhandler(401)
def internal_error(error):
    return jsonify(
        {
            "Message": "Acess denied ! please register and login to generate API KEY"
        },
        {
            "status": 401
        }
    )



@app.errorhandler(404)
def not_found_error(error):
    return jsonify(
        {
            "Message":"Sorry the page your are looking for is not here kindly go back"
        },
        {
            "status": 404
        }
    )





@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify(
        {
            "Message": "Sorry the requested method is not allowed kindly check and resend !"
        },
        {
            "status": 405
        }
    )

@app.errorhandler(500)
def method_not_allowed(error):
    return jsonify(
        {
            "Message": "Bad request please check your input and resend !"
        },
        {
            "status": 500
        }
    )