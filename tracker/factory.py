from importlib import import_module

def get_instance(module_name, class_name, base_class, *args, **kwargs):

  try:
    module = import_module(module_name)
    the_class = getattr(module, class_name)
    instance = the_class(*args, **kwargs)
  except (AttributeError, ModuleNotFoundError):
    raise ImportError('{} is not supported.'.format(module_name))
  else:
    if not issubclass(the_class, base_class):
      raise ImportError("{} is not a valid {}.".format(the_class, base_class))

  return instance
