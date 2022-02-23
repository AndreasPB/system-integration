from bottle import run, get, response, post, request, error, hook, delete, put
import json
import uuid

items = [
    {
        "id": "c16d2802-c5a1-441c-b133-320ac74390cc",
        "name": "John",
        "last_name": "Smith",
        "age": 20,
    },
]


@hook("after_request")
def _():
    response.content_type = "application/json"


@get("/")
def _():
    return "Hello World!"


@get("/items")
def _():
    return json.dumps(items)


@get("/items/<id>")
def _(id):
    for item in items:
        if item["id"] == id:
            return json.dumps(item)
    response.status = 204
    return


@get("/items_comp/<id>")
def _(id):
    items = [x for x in items if x["id"] == id]
    if not items:
        response.status = 204
        return
    return items[0]


@post("/items")
def _():
    item_id = str(uuid.uuid4())
    item_name = request.json.get("name")
    item = {"id": item_id, "name": item_name}
    items.append(item)
    response.status = 201
    return {"id": item_id}


@put("/items/<id>")
def _(id):
    try:
        item = [item for item in items if item["id"] == id][0]
        # print(list(map(lambda key: item[key] = request.json[key], request.json.keys())))
        for key in request.json.keys():
            if key in item.keys():
                item[key] = request.json[key]
        return item
    except Exception as e:
        print(e)
        response.status = 204
        return


@delete("/items/<id>")
def _(id):
    for index, item in enumerate(items):
        if item["id"] == id:
            items.pop(index)
            response.status = 201
            return f"Item deleted: {id}"
    response.status = 204
    return


@error(404)
def _(error):
    response.content_type = "application/json"
    return json.dumps({"info": "Not found"})


run(host="127.0.0.1", port=42069, debug=True, reloader=True, server="paste")
