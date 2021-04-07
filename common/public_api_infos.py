from common.config_utils import config
import json,jsonpath
# print(config.Hosts)
def get_access_token_api(session,url_params):
    response =session.get(url='https://%s/cgi-bin/token'%config.Hosts, params=url_params)
    return response

def creat_user_tag_api(session,url_params,post_data):
    post_data_str1 = json.dumps(post_data, ensure_ascii=False)
    response = session.post(url='https://%s/cgi-bin/tags/create'%config.Hosts, params=url_params,
                             data=post_data_str1.encode('utf-8'))
    return response
def delete_user_tag_api(session,url_params,post_data):
    response = session.post(url='https://%s/cgi-bin/tags/delete'%config.Hosts, params=url_params,
                             data=post_data)
    return response

def get_token(session):
    url_params = {
        "grant_type": "client_credential",
        "appid": config.appid,
        "secret": config.secret
    }
    response = get_access_token_api(session,url_params)
    token_value = jsonpath.jsonpath(response.json(),'$.access_token')[0]
    return token_value
