from importlib import import_module

from .base import BaseStrategy

def factory(exchange_name, *args, **kwargs):

  try:
    module_name = exchange_name
    class_name = exchange_name.capitaliza() + 'Strategy'
    strategy_module = import_module('.' + module_name, package='strategy')
    strategy_class = getattr(strategy_module, class_name)
    instance = strategy_class(*args, **kwargs)
  except (AttributeError, ModuleNotFoundError):
    raise ImportError('{} is not a supported exchange.'.format(exchange_name))
  else:
    if not issubclass(strategy_class, BaseStrategy):
      raise ImportError("We currently don't have {}, but you are welcome to send in the request for it.".format(strategy_class))

  return instance
