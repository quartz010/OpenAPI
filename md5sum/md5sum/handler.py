
import json
import random
import hashlib
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
        ret["code"] = 0
        ret["msg"] = "invalid parameters"
        return json.dumps(ret)
    else:
        try:
            hash = hashlib.md5(req.encode("utf-8")).hexdigest()
            ret["code"] = 0
            ret["msg"] = hash
            return json.dumps(ret)
        except Exception as e:
            ret["code"] = -1
            ret["msg"] = e
            return json.dumps(ret)
    return json.dumps(ret)