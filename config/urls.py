#coding: utf-8
from apis import *
from backend import *

urls = [
    ("/v1/simulation/love_experience", LoveController),
    ("/v1/simulation/dregs_experience", DregController),
    ("/v1/chapter/kira_campus", KiraCampusController),
    ("/v1/chapter/kamisama", KamisamaController),
    ("/v1/admin", AdminController),
    ("/v1/admin/add", AdminAddController),
]