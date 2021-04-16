# CRLF Injection

* curl -v https://www.example.com -H 'x-request-id: 450%0d%0a%0d%0aTest=test' | grep 'x-request-id'
