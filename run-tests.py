#!/usr/bin/python
"""
Runs unittests for app.

Based vaguely on https://github.com/kamalgill/flask-appengine-template/blob/master/src/apptest.py
"""

import os
import sys
import unittest
import warnings
#import nose

# silences Python's complaints about imports
warnings.filterwarnings('ignore', category=UserWarning)


def main(sdk_path, test_path):
    sys.path.insert(0, sdk_path)
    import dev_appserver
    dev_appserver.fix_sys_path()
    sys.path.insert(1, os.path.join(os.path.abspath('.'), 'lib'))
    sys.path.insert(1, os.path.join(os.path.abspath('.')))

    try:
        import config
    except ImportError:
        raise Exception('Unable to load config module. Paths are most likely screwed up. Current path is: %r and has %r' % (
            os.path.abspath('.'), os.listdir(os.path.abspath('.'))
        ))
    config.enable_debug_panel = False

    #
    # This must always be imported first.
    from flask import logging

    from main import app

    logger = logging.create_logger(app)

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    logger.addHandler(console)

    suite = unittest.loader.TestLoader().discover(test_path)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    for path_to_try in ['/usr/local/google_appengine', './google_appengine', 'C:\Program Files (x86)\Google\google_appengine', 'C:\Program Files\Google\google_appengine']:
        if os.path.exists(path_to_try):
            SDK_PATH = path_to_try

    TEST_PATH = os.path.join(os.path.dirname(os.path.abspath(__name__)))
    main(SDK_PATH, TEST_PATH)
