from zeep import Client

"""
Client makes a request to a SOAP Web Service
running locally.  The Web Service 
returns the number of fibonacci numbers
requested by get_fib() , 
and prints to console
"""
# start a client with the info
client  = Client('http://127.0.0.1:3333/?wsdl')

int_fibs = None

while True:
    n_fibs = input("Input the number of fibonacci numbers:")
    if n_fibs.isdigit():
        int_fibs = int(n_fibs)
        break

# call to SOAP Web Service
result = client.service.get_fib(int_fibs)

print(result)

