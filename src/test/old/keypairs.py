from __future__ import print_function
import unittest
from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from twcc.twcc import TWCC

class ServiceTest(unittest.TestCase):
    def setUp(self):
        self.fn_twcc_yaml = '../yaml/NCHC_API-Test_env.yaml'
        self.twcc = TWCC(self.fn_twcc_yaml, debug = True)

        keyname = "twc1234"
        self.mydict = {"keypairs": keyname}
        self.mydata = {"name": keyname}

        self.yaml_keys = self.twcc.twcc_conf['stage']["keys"].keys()

    def test_connect(self):
        self.assertTrue(self.twcc.try_alive())
        
    def _test_key_create(self):
        for x in self.site_tags:
            for y in self.yaml_keys:
                self.keypair_create(x, y, 'txt')
                res = self.keypair_get(x, y, 'txt')
                self.assertEqual(res['name'], self.mydict['keypairs'])

    def _test_key_delete(self):
        for x in self.site_tags:
            for y in self.yaml_keys:
                self.keypair_delete(x, y, 'txt');
                res = self.keypair_get(x, y, 'json')
                self.assertIn('error', res)

    def keypair_delete(self,
            site_tag = 1,
            key_tag = 'sys',
            res_format = 'json'):

        return self.twcc.doAPI(
            site_sn = site_tag,
            key_tag = key_tag,
            func = "keypairs",
            url_dict = self.mydict,
            http = 'delete',
            res_type = 'txt')

    def keypair_get(self,
            site_tag = 1,
            key_tag = 'sys',
            res_format = 'json'):

        return self.twcc.doAPI(
            site_sn = site_tag,
            key_tag = key_tag,
            func = "keypairs",
            url_dict = self.mydict,
            http = 'get',
            res_type = 'json')

    def keypair_create(self,
            site_tag = 1,
            key_tag = 'sys',
            res_format = 'json'):

        return self.twcc.doAPI(
            site_sn = site_tag,
            key_tag = key_tag,
            func = "keypairs",
            data_dict = self.mydata,
            http = 'post',
            res_type = res_format)


if __name__  ==  '__main__':
    unittest.main()