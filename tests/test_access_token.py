import unittest
import mock

from scripts.bitbucket import request_access_token, BitbucketException


class RequestAccessTokenTestCase(unittest.TestCase):

    def test_fails_ok(self):
        with mock.patch('scripts.bitbucket.requests') as requests:
            r = mock.MagicMock()
            r.status_code = 401
            r.json.return_value = {}

            requests.post.return_value = r

            with self.assertRaises(BitbucketException):
                request_access_token('client', 'secret', False)

    def test_works(self):
        with mock.patch('scripts.bitbucket.requests') as requests:
            r = mock.MagicMock()
            r.status_code = 200
            r.json.return_value = {"access_token": "token"}

            requests.post.return_value = r

            self.assertEqual(
                request_access_token('client', 'secret', False),
                "token"
            )