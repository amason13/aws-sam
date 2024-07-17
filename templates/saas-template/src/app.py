def handler(event, context):
    response_object = {}
    response_object["isBase64Encoded"]=False
    response_object["statusCode"] = 200
    response_object["headers"] = {}
    response_object["headers"]["Content-Type"]="application/json"
    response_object["headers"]["Access-Control-Allow-Origin"]="*"
    response_object["multiValueHeaders"] = {}
    response_object["body"] = "Success! Authenticated API call from coginito user and pw."

    return response_object