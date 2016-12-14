# Copyright 2016: Venidera Research & Development.
# All Rights Reserved.
#
# Licensed under the GNU General Public License, Version 3.0 (the "License")
# you may not use this file except in compliance with the License. You may
# obtain a copy of the License at
#
#      https://www.gnu.org/licenses/gpl-3.0.en.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
import requests
import socket
from json import dumps,loads
from logging import debug

def ping(host, port):
    try:
        socket.socket().connect((host, port))
        debug('Ping in %s: %d - LINC API Server: Ok\n' % (host, port))
        return True
    except socket.error as err:
        if err.errno == socket.errno.ECONNREFUSED:
            debug('Can\'t connect to LINC API Server')
            return False
        raise Exception('Fail to test LINC API Server connection status')

class Connection(object):
    def __init__(self, server='localhost', port=80):
        self.server = server
        self.port = port
        ping(server, port)
        self.headers = {'content-type': "application/json",'Linc-API-AuthToken':None}

    def get_endpoint(self, key):
        return {
            'login': '/auth/login',
            'lions': '/lions/!',
            'version': '/version/',
            'listlions': '/lions/list'
            # 'entsearch': '/entities/search/',
            # 'entbatch': '/entities/batch/',
            # 'enttypes': '/entities/types/',
            # 'entupdate': '/entities/!',
            # 'reltypes': '/relationships/types/',
            # 'relsearch': '/relationships/search/',
            # 'relupdate': '/relationships/!',
            # 'rel': '/relationships/',
            # 'relbatch': '/relationships/batch/',
            # 'tsr': '/timeseries/',
            # 'tsrupdate': '/timeseries/!',
            #
            # 'types': '/types/',
        }.get(key)

    def get_url(self):
        if self.port == 80:
            return self.server
        else:
            return self.server + ':' + str(self.port)

    def _post(self, endpoint=None, data=None, objid=''):
        if not endpoint or not data:
            return
        resource = self.get_endpoint(endpoint).replace('!', objid)
        url = str(self.get_url() + resource)
        response = requests.post(url, data=dumps(data),headers=self.headers,verify=True)
        return response

    def _get(self, endpoint=None, objid='', params={}):
        if not endpoint:
            return
        resource = self.get_endpoint(endpoint).replace('!', objid)
        url = str(self.get_url() + resource)
        response = requests.get(url,params=params)
        return response

    def login(self, username, password):
        assert isinstance(username, str) and isinstance(password, str), \
            'username and password must be str.'
        response = self._post(endpoint='login',data={'username':username,'password':password},headers=self.heheaders)
        if response.ok:
            if 200 <= response.status_code < 300:
                body = loads(response.text)
                self.headers['Linc-API-AuthToken'] = body['data']['token']
                self.info = body['data']
                return True
            else:
                debug('Login failed: '+resp.reason)
        return False

    def get_lions(self,objid=''):
        response = self._get(endpoint='lions')
        if response.ok:
            if 200 <= response.status_code < 300:
                body = loads(response.text)
                return body
            else:
                debug('Login failed: '+resp.reason)
        return False

    def get_lions_list(self):
        response = self._get(endpoint='listlions')
        if response.ok:
            if 200 <= response.status_code < 300:
                body = loads(response.text)
                return body['data']
            else:
                debug('Login failed: '+resp.reason)
        return False

    def get_version(self):
        response = self._get(endpoint="version")
        return loads(response.text)['message']
