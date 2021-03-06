import locale
from stock_manager import db
from stock_manager.catalog.decorators import validate_post_args

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Float(asdecimal=True))

    @validate_post_args
    def __init__(self, name, price): 
        self.name = name
        self.price = price
    
    def __repr__(self):
        return '<Product %d>' % self.id
    
    def get_formatted_price(self, locale_code='pt_BR.UTF-8'):
        '''
        Get the product price formatted based on locale's currency.
        '''
        locale.setlocale(locale.LC_ALL, locale_code)
        return locale.currency(self.price, grouping=True, symbol=True)
    
    def is_product_already_exists(self, product_name):
        return self.query.filter_by(name=product_name).first()