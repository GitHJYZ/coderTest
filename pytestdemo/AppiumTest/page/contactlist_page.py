from pytestdemo.AppiumTest.page.base_page import BPage

class ContactListPage(BPage):

    def goto_addmember(self):
        # click 添加成员
        self.swipe_find('添加成员').click()
        from pytestdemo.AppiumTest.page.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)