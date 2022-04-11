import requests
import json

grant_type = "client_credential"
appid = "wx30e2b5c266c42f3e"
secret = "595d77f2eb7ad3417ee6201ec5dbdec4"
access_token_url = \
    "https://api.weixin.qq.com/cgi-bin/token?grant_type=%s&appid=%s&secret=%s"

send_template = \
    "https://api.weixin.qq.com/cgi-bin/message/subscribe/send?access_token=%s"

template_id = "PT9dRvi7zLpUIQGPk9S2rsuVSkAoHwLeW5Iwcy8Hg3Y"


def query_token():
    req = requests.get(
        url=access_token_url % (
            grant_type,
            appid,
            secret)
    )
    return req.json()["access_token"]


template_mod = {
    "thing1": {
        "value": ""
    },

    "time3": {
        "value": ""
    },
    "thing2": {
        "value": ""
    }
}


def create_template(a, b, c):
    template = template_mod
    template["thing1"]["value"] = a
    template["time3"]["value"] = b
    template["thing2"]["value"] = c
    # print(template)
    return template


def send_message(access_token,
                 touser,
                 template_data,
                 template_id="PT9dRvi7zLpUIQGPk9S2rsuVSkAoHwLeW5Iwcy8Hg3Y"
                 ):
    print(template_data)
    req = requests.post(
        url=send_template % (access_token,),
        json=
        # {
        #     "touser": "oHEI15X_8YfAhoYXm03R5Z-F05uc",
        #     "template_id": "PT9dRvi7zLpUIQGPk9S2rsuVSkAoHwLeW5Iwcy8Hg3Y",
        #     "page": "index",
        #     "miniprogram_state": "developer",
        #     "lang": "zh_CN",
        #     "data": {
        #         "thing1": {
        #             "value": "请老师前往小程序确认监考"
        #         },
        #
        #         "time3": {
        #             "value": "2020.12.29 21:30"
        #         },
        #         "thing2": {
        #             "value": "计算机网络"
        #         }
        #     }
        # }

        {
            "touser": touser,
            "template_id": template_id,
            "page": "index",
            "miniprogram_state": "developer",
            "lang": "zh_CN",
            "data": template_data
        }
    )
    print(req.text)

# temp = "oHEI15X_8YfAhoYXm03R5Z-F05uc"
# send_message(query_token(), temp, create_template("你好", "2020.12.29 21:30", "操作系统"))
