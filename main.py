from utils import debug, send, init

acct, user = init()

@send
def test():
    return user, "5P4M", "`2Pls` ignore this message!"
