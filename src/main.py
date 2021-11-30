# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List

from alibabacloud_cdn20180510.client import Client as Cdn20180510Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_cdn20180510 import models as cdn_20180510_models 
import os

# 获取环境变量
def getEnvPara(parameterName, default=None, 
    raiseExceptionIfNone=True):
    parameterValue = os.environ.get(parameterName, default)
    if parameterValue is None and raiseExceptionIfNone:
        raise Exception(parameterName + " not defined")
    return parameterValue

ACCESS_KEY_ID = getEnvPara(parameterName="ACCESS_KEY_ID")
ACCESS_KEY_SECRET = getEnvPara(parameterName="ACCESS_KEY_SECRET")
OBJECT_TYPE = getEnvPara(parameterName="OBJECT_TYPE")
OBJECT_PATH = getEnvPara(parameterName="OBJECT_PATH")

class Cdn:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Cdn20180510Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 您的AccessKey ID,
            access_key_id=access_key_id,
            # 您的AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # 访问的域名
        config.endpoint = 'cdn.aliyuncs.com'
        return Cdn20180510Client(config)

    @staticmethod
    def refresh() -> None:
        client = Cdn.create_client(ACCESS_KEY_ID, ACCESS_KEY_SECRET)
        refresh_object_caches_request = cdn_20180510_models.RefreshObjectCachesRequest(
            object_type=OBJECT_TYPE,
            object_path=OBJECT_PATH
        )
        # 复制代码运行请自行打印 API 的返回值
        res = client.refresh_object_caches(refresh_object_caches_request)
        print(res)

    @staticmethod
    async def refresh_async() -> None:
        client = Cdn.create_client(ACCESS_KEY_ID, ACCESS_KEY_SECRET)
        refresh_object_caches_request = cdn_20180510_models.RefreshObjectCachesRequest(
            object_type=OBJECT_TYPE,
            object_path=OBJECT_PATH
        )
        # 复制代码运行请自行打印 API 的返回值
        res = await client.refresh_object_caches_async(refresh_object_caches_request)
        print(res)
    
    @staticmethod
    def describeRefreshQuota() -> None:
        client = Cdn.create_client(ACCESS_KEY_ID, ACCESS_KEY_SECRET)
        describe_refresh_quota_request = cdn_20180510_models.DescribeRefreshQuotaRequest()
        # 复制代码运行请自行打印 API 的返回值
        res = client.describe_refresh_quota(describe_refresh_quota_request)
        print(res)


if __name__ == '__main__':
    Cdn.describeRefreshQuota()
    Cdn.refresh()
    Cdn.describeRefreshQuota()