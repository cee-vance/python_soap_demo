#  Application is the glue between one or more service definitions, interface and protocol choices
from spyne.application import Application#webserver apacheIIS..WSGI asgi
# The @srpc decorator exposes methods as remote procedure calls and declares the data types it accepts and returns.
from spyne.decorator import srpc
# spyne.service.ServiceBase is the base class for all service definitions.
from spyne.service import ServiceBase

from spyne.model.complex import Iterable
from spyne.model.primitive import UnsignedInteger
from spyne.model.primitive import String


from spyne.server.wsgi import WsgiApplication

from wsgiref.simple_server import make_server
from spyne.protocol.soap import Soap11
from wsgiref.simple_server import make_server


class FibSoapService( ServiceBase):
    """
    Simple SOAP service with one method
    that takes one argument ,n an integer
    and returns an Iterable with n elements
    of the fibonnaci sequence
    """
    @srpc(UnsignedInteger, _returns=Iterable(String))
    def get_fib(n):
        n1,n2 = 0,1
        count = 0
        while count < n:
            n1,n2 = n2, n1+n2
            yield str(n2)
            count+=1



if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    app = Application([FibSoapService],
                      tns='spyne.examples.hello.http',
                      in_protocol=Soap11(),
                      out_protocol=Soap11())

    wsgi_app = WsgiApplication(app)

    server = make_server('127.0.0.1', 3333,wsgi_app)

    print('listening on http://127.0.0.1:3333')
    print("wsdl is at http://localhost:3333/?wsdl")

    server.serve_forever()