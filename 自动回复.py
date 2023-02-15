import json
from sanic import Sanic

app = Sanic('qqbot')
base_path = "C:/Users/Administrator/Desktop/project01/project01/"


@app.websocket('/qqbot')
async def qqbot(request, ws):
    """QQ机器人"""
    while True:
        data = await ws.recv()
        data = json.loads(data)
        print(json.dumps(data, indent=4, ensure_ascii=False))
        # if 判断是群消息且文本消息不为空
        if data.get('message_type') == 'group' and data.get('raw_message'):
            raw_message = data['raw_message']
            if raw_message == "/1":
                with open(base_path + "1.txt", encoding="utf8") as f:
                    msg = f.read()
                ret = {
                        'action': 'send_group_msg',
                        'params': {
                            'group_id': data['group_id'],
                            'message': {
                                "type": "image",
                                "data": {
                                    "file" : "2.jpg",

                                }
                            },
                        }
                    }
                await ws.send(json.dumps(ret))
            elif raw_message == "你觉得我群魅魔怎么样":
                with open(base_path + "2.txt", encoding="utf8") as f:
                    msg = f.read()
                ret = {
                        'action': 'send_group_msg',
                        'params': {
                            'group_id': data['group_id'],
                            'message': msg,
                        }
                    }
                await ws.send(json.dumps(ret))
            elif raw_message == "魅魔":
                with open(base_path + "1.txt", encoding="utf8") as f:
                    msg = f.read()
                ret = {
                        'action': 'send_group_msg',
                        'params': {
                            'group_id': data['group_id'],
                            'message': msg,
                        }
                    }
                await ws.send(json.dumps(ret))
            elif raw_message == "都是魅魔的错":
                with open(base_path + "3.txt", encoding="utf8") as f:
                    msg = f.read()
                ret = {
                        'action': 'send_group_msg',
                        'params': {
                            'group_id': data['group_id'],
                            'message': msg,
                        }
                    }
                await ws.send(json.dumps(ret))
            elif raw_message == "是吧我也觉得":
                with open(base_path + "5.txt", encoding="utf8") as f:
                    msg = f.read()
                ret = {
                    'action': 'send_group_msg',
                    'params': {
                        'group_id': data['group_id'],
                        'message': msg,
                    }
                }
                await ws.send(json.dumps(ret))
            elif raw_message == "/2":
                with open(base_path + "4.txt", encoding="utf8") as f:
                    msg = f.read()
                ret = {
                    'action': 'send_group_msg',
                    'params': {
                        'group_id': data['group_id'],
                        'message': msg,
                    }
                }
                await ws.send(json.dumps(ret))
            elif raw_message == "/7":
                with open(base_path + "8.txt", encoding="utf8") as f:
                    msg = f.read()
                ret = {
                    'action': 'send_group_msg',
                    'params': {
                        'group_id': data['group_id'],
                        'message': msg,
                    }
                }
                await ws.send(json.dumps(ret))
            elif raw_message == "/6":
                with open(base_path + "7.txt", encoding="utf8") as f:
                    msg = f.read()
                ret = {
                    'action': 'send_group_msg',
                    'params': {
                        'group_id': data['group_id'],
                        'message': msg,
                    }
                }
                await ws.send(json.dumps(ret))
            elif raw_message == "/5":
                with open(base_path + "6.txt", encoding="utf8") as f:
                    msg = f.read()
                ret = {
                    'action': 'send_group_msg',
                    'params': {
                        'group_id': data['group_id'],
                        'message': msg,
                    }
                }
                await ws.send(json.dumps(ret))


if __name__ == '__main__':
    app.run(debug=True,port=8866,auto_reload=True)