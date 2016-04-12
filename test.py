import main
import unittest


class UserSignupTestCase(unittest.TestCase):
    def setUp(self):
        main.app.config['TESTING'] = True
        self.app = main.app.test_client()

    def signUp(self, inputName, inputEmail, inputPassword):
        return self.app.post('/signUp', data=dict(
            inputName = inputName,
            inputEmail = inputEmail, inputPassword = inputPassword
        ),follow_redirects=True)

    def test_signUp_ok(self):
        rv = self.signUp("ray", "ray@gmail.com", "123456")
        assert b'success'

    def test_signUp_not_ok(self):
        rv = self.signUp("admin", "admin@admin.com", "123456")
        assert b'fail'
	
    def test_signUp_not_ok1(self):
        rv = self.signUp("ray", "admin@admin.com", "123456")
        assert b'fail'

    def validateLogin(self, InputUsername, inputPassword):
        return self.app.post('/validateLogin', data=dict(
            InputUsername = InputUsername,
            inputPassword=inputPassword
        ),follow_redirects=True)

    def test_validateLogin_ok(self):
        rv = self.validateLogin("mohamed", "123456")
        assert b'Success' 

    def test_validateLogin_not_ok(self):
        rv = self.validateLogin("mohamed", "test")
        assert b'Fail'

    def test_validateLogin_unknown_user(self):
        rv = self.validateLogin("batman", "test123")
        assert b'Fail'

if __name__ == '__main__':
    unittest.main()