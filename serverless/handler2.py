

from random import randint


def hello(event, context):

    return {"message": "hello world!"}


def hello_check(event, context):

    response = randint(0, 2)
    return {"value": response}


def hello_receiver(event, context):
    if event["body"] == 2:
        return True
    elif event["body"] == 1:
        return False
    else:
        raise (Exception("No valid option try again"))


def hello_0(event, context):
    raise (Exception("No valid option try again"))


def hello_1(event, context):
    resp = {"value": True}
    print(resp)
    return resp


def hello_2(event, context):
    resp = {"value": False}
    print(resp)
    return resp


# sls invoke stepf --name hellostepfunc --stage dev

