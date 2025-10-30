from flask import Flask
from flask_cors import CORS
from config import Config

from .routes.user_bp import user_bp
from .routes.product_bp import product_bp
from .routes.domi_bp import domi_bp
from .routes.cart_bp import cart_bp
from .routes.pedido_bp import pedido_bp
from .routes.pago_bp import pago_bp
from .routes.valo_bp import valo_bp
from .database import DatabaseConnection

def init_app():
    """Crea y configura la aplicación Flask"""
    
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    
    CORS(app, supports_credentials=True, resources={               
                                                    r"*": {"origins": "*"},
                                                    # r"/profile/*": {"origins": "*"},
                                                    # r"/products/*": {"origins": "*"},
                                                    # r"/'pedidos'/*": {"origins": "*"}
                                                    # r"/error/*": {"origins": "*"},
                                                    # r"/pedido/*": {"origins": "*"},
                                                    # r"/carrito/*": {"origins": "*"}
                                                    })

    app.config.from_object(
        Config
    )

    DatabaseConnection.set_config(app.config)

    # app.register_blueprint(errors, url_prefix = '/errors')
    app.register_blueprint(user_bp, url_prefix = '')
    app.register_blueprint(product_bp, url_prefix = '/products')
    app.register_blueprint(domi_bp, url_prefix = '/addresses')
    app.register_blueprint(cart_bp, url_prefix = '/carts')
    app.register_blueprint(pedido_bp, url_prefix = '/pedidos')
    app.register_blueprint(pago_bp, url_prefix = '/pagos')
    app.register_blueprint(valo_bp, url_prefix = '/valoracion')
    return app