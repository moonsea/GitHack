#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import urllib2
import urllib
import json
import base64
from lib.data import conf

"""
 Request Github API
"""
class Repos(object):

    def __init__(self):
        super(Repos, self).__init__()
        self.base_url = 'https://api.github.com/repos'

    """
    API URL: https://api.github.com/repos/moonsea/ecshop
    """
    def base_info(self):
        super(Repos, self).__init__()
        base_url = '/'.join([self.base_url,conf.user,conf.repo])
        response = self.repo_request(base_url)
        return response

    """
    " Return repo content or content list
    """
    def repo_request(self,con_path):
        super(Repos, self).__init__()
        url = urllib2.Request(con_path)
        response = json.loads(urllib2.urlopen(url).read())

        return response

    def repo_con(self,con_path):

        response = self.repo_request(con_path)

        if(isinstance(response,dict)):
            file_con_en = response['content']
            self.detect_con(file_con_en) # Detect content
            return

        for item in response:
            print item['name'],'---',item['path']
            # if(item.has_key('content')):
            #     file_con_en = dic['content']
            #     self.detect_con(file_con_en) # Detect content
            #     return
            # else:
            self.repo_con(item['url'])

    """
    " Detect Content
    " Input: file encoded content
    """
    def detect_con(self,file_con_en):
        super(Repos, self).__init__()

    """
    " Return repo content with leaked information
    " root content api url: https://api.github.com/repos/moonsea/ecshop/contents
    " normal content api url: https://api.github.com/repos/moonsea/ecshop/contents/admin?ref=master"
    """
    def repo_leak_con(self):
        super(Repos, self).__init__()
        root_con_path = '/'.join([self.base_url,conf.user,conf.repo,'contents'])

        self.repo_con(root_con_path)

        " Root Content "
        root_con = self.repo_request(root_con_path)

        return root_con
