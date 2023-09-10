import os

__path_dict__ = {}

__path_dict__['main'] = os.path.dirname(__file__)
__path_dict__['data'] = os.path.join(__path_dict__['main'], 'data')
__path_dict__['lib'] = os.path.join(__path_dict__['main'], 'lib')
__path_dict__['models'] = os.path.join(__path_dict__['main'], 'models')


__path_dict__['home'] = os.path.expanduser("~")
__path_dict__['dot-cerebrum-scanner'] = os.path.join(__path_dict__['home'],'.cerebrum-scanner')
__path_dict__['dot-cerebrum-scanner-jobs'] = os.path.join(__path_dict__['home'],'.cerebrum-scanner','jobs')
__path_dict__['dot-cerebrum-scanner-completed'] = os.path.join(__path_dict__['home'],'.cerebrum-scanner','completed')

__path_dict__['kvfiles'] = os.path.join(__path_dict__['main'], 'kvfiles')

for _,pth in __path_dict__.items():
    if os.path.exists(pth): pass
    else: os.mkdir(pth)
