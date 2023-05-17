import json
import pytest
import yaml
import logging
from jsonpath import jsonpath
from pytestdemo.service.api.tag.tag_api import Tag

class TestWeWork:
    def setup_class(self):
        self.tag = Tag('ww9a7c9f39d084b5a1','XH_5yu4cp94O_NuSC_iQA7sbHwtHTBMxi-6A6tWBAZs')
        self.tag.clear_whole_tag()

    def test_get_whole_tag(self):
        r = self.tag.get_tag_list()
        logging.info(json.dumps(r.json(), indent=2, ensure_ascii=False))

    def test_add_tag(self):
        self.tag.clear_whole_tag()
        r = self.tag.add_tag_name("2022/5/8")
        assert r.json()['errcode'] == 0
        r = self.tag.get_tag_list()
        assert '2022/5/8' in [i['group_name'] for i in r.json()['tag_group']]

        r = self.tag.add_tag_name("2022/5/9", [{"name": "021"}, {"name": "022"}])
        assert r.json()['errcode'] == 0
        r = self.tag.get_tag_list()
        assert r.json()["tag_group"][1]["tag"][0]["name"] == "021"
        l = jsonpath(r.json(), '$..tag[*].name')
        assert '021' in l and '022' in l

    def test_delete_tag(self):
        self.tag.clear_whole_tag()
        r = self.tag.add_tag_name("2022/5/8")
        assert r.json()['errcode'] == 0
        r = self.tag.get_tag_list()
        logging.info(json.dumps(r.json(), indent=2, ensure_ascii=False))
        r = self.tag.del_tag_by_name(groupName="2022/5/8")
        assert r['errcode'] == 0
        r = self.tag.get_tag_list()
        assert '2022/5/8' not in [i['group_name'] for i in r.json()['tag_group']]

    @pytest.mark.parametrize("tagNameOld, groupNameOld, newName, newOrder",
                             yaml.safe_load(open('yaml/edit_tag_success.yaml', encoding='utf - 8')))
    def test_edit_tag(self, tagNameOld, groupNameOld, newName, newOrder):
        self.tag.clear_whole_tag()
        r = self.tag.add_tag_name("group", [{"name": "label1"}])
        assert r.json()['errcode'] == 0
        r = self.tag.get_tag_list()
        assert r.json()["tag_group"][0]["tag"][0]["name"] == "label1"
        r = self.tag.edit_tag_name(tagNameOld=tagNameOld, groupNameOld=groupNameOld, newName=newName, newOrder=newOrder)
        assert r.json()['errcode'] == 0
        r = self.tag.get_tag_list()
        if tagNameOld is not None:
            assert r.json()["tag_group"][0]["tag"][0]["name"] == newName
            if newOrder is not None:
                assert r.json()["tag_group"][0]["tag"][0]["order"] == newOrder
        elif groupNameOld is not None:
            assert r.json()["tag_group"][0]["group_name"] == newName
            if newOrder is not None:
                assert r.json()["tag_group"][0]["order"] == newOrder

    def test_smoke_flow(self):
        self.tag.clear_whole_tag()
        r = self.tag.add_tag_name("2022/5/8", [{"name": "021"}])
        assert r.json()['errcode'] == 0
        r = self.tag.edit_tag_name(tagNameOld='021', newName='label1_bak')
        assert r.json()['errcode'] == 0

        r = self.tag.del_tag_by_name(tagName="label1_bak")
        assert r['errcode'] == 0
        r = self.tag.get_tag_list()
        assert r.json()["tag_group"] == []