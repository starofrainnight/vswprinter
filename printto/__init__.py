import os.path

APP_NAME = os.path.basename(os.path.dirname(__file__))


def get_template_name(sub_name):
    """
    Get template name inside "<APP_NAME>/templates/<APP_NAME>/" .
    """
    return os.path.join(APP_NAME, sub_name)
