import json
import random
def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    ret = {
        "code": 0,
        "msg": ""
    }
    if req == "":
        randint = random.randint(0, 65535)
        ret["code"] = 0
        ret["msg"] = randint
        return json.dumps(ret)
    else:
        try:
            req = json.loads(req)
            randint = random.randint(req[1], req[2])
            ret["code"] = 0
            ret["msg"] = randint
            return json.dumps(ret)
        except Exception:
            ret["code"] = -1
            ret["msg"] = "invalid json"
            return json.dumps(ret)
    return json.dumps(ret)