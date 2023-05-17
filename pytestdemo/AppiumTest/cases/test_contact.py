from faker import Faker
from pytestdemo.AppiumTest.page.app import App
from pytestdemo.AppiumTest.utils.contact_info import ContactInfo


class TestContact():
    def setup_class(self):
        self.contactinfo = ContactInfo()
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.restart()

    def teardown_class(self):
        self.app.stop()

    def test_addcontact(self):
        name = self.contactinfo.get_name()
        phonenum = self.contactinfo.get_phonenum()

        self.main.goto_contactlist().\
            goto_addmember().\
            addmember_bymenual().\
            edit_member(name,phonenum).\
            find_toast()