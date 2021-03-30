


class Basket():
    """
    A base Basket class, providing some default behaviors that
    can be inherited or overrided.
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {'number':1231231}
        self.basket = basket
