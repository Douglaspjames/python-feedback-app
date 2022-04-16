import unittest
import app

import webtest

class TestApp(unittest.TestCase):

    def test_index(self):
        test_app = webtest.TestApp(app.app)
        resp = test_app.get('/')
        self.assertEqual(resp.status, '200 OK')
        self.assertEqual(resp.content_type, 'text/html')

    def test_submit(self):
        test_app = webtest.TestApp(app.app)
        resp = test_app.post('/submit', dict(customer='Fred Derfler', dealer='Tom Smith', rating=10, comments='nice job') )
        self.assertEqual(resp.status, '200 OK')
        self.assertEqual(resp.content_type, 'text/html')

if __name__ == '__main__':
    unittest.main()
