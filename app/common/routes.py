from flask import Blueprint, render_template, request, jsonify
import json
import ast
from app.models import Bank_Branches
default = Blueprint('default', __name__)

@default.route('/search', methods=['GET'])
def search():
    search_dict = {}
    search_dict["bank_name"] = request.args.get('bank_name')
    search_dict["city"] = request.args.get('city')
    search_dict["page"] = request.args.get('page')
    if search_dict["page"]:
        try:
            search_dict["page"] = int(search_dict["page"])
        except Exception:
            search_dict["page"] = 0
    else:
        search_dict["page"] = 0            
    
    print search_dict
    result = Bank_Branches.search(**search_dict)
    result = ast.literal_eval(str(result))
    # result = [ast.literal_eval(str(r)) for r in result]
    # for r in result:
    #     print type(r)
    json_result = {}
    json_result["result"] = result
    # print json_result
    return jsonify(json_result),200

@default.route('/search/<ifsc_code>/', methods=['GET'])
def search_by_ifsc(ifsc_code):
    result = Bank_Branches.search_by_ifsc(ifsc_code)
    result = ast.literal_eval(str(result))
    # json_result = {}
    # json_result["result"] = result
    # print json_result
    return jsonify(result),200