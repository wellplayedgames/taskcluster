# coding=utf-8
#####################################################
# THIS FILE IS AUTOMATICALLY GENERATED. DO NOT EDIT #
#####################################################
# noqa: E128,E201
from ...aio.asyncclient import AsyncBaseClient
from ...aio.asyncclient import createApiClient
from ...aio.asyncclient import config
from ...aio.asyncclient import createTemporaryCredentials
from ...aio.asyncclient import createSession
_defaultConfig = config


class Object(AsyncBaseClient):
    """
    The object service provides HTTP-accessible storage for large blobs of data.
    """

    classOptions = {
    }
    serviceName = 'object'
    apiVersion = 'v1'

    async def ping(self, *args, **kwargs):
        """
        Ping Server

        Respond without doing anything.
        This endpoint is used to check that the service is up.

        This method is ``stable``
        """

        return await self._makeApiCall(self.funcinfo["ping"], *args, **kwargs)

    async def uploadObject(self, *args, **kwargs):
        """
        Upload backend data

        Upload backend data.

        This method is ``experimental``
        """

        return await self._makeApiCall(self.funcinfo["uploadObject"], *args, **kwargs)

    async def downloadObject(self, *args, **kwargs):
        """
        Download object data

        Download object data.
        See [Download Methods](https://docs.taskcluster.net/docs/reference/platform/object/upload-download-methods#download-methods) for more detail.

        This method is ``experimental``
        """

        return await self._makeApiCall(self.funcinfo["downloadObject"], *args, **kwargs)

    funcinfo = {
        "downloadObject": {
            'args': ['name'],
            'input': 'v1/download-object-request.json#',
            'method': 'put',
            'name': 'downloadObject',
            'output': 'v1/download-object-response.json#',
            'route': '/download/<name>',
            'stability': 'experimental',
        },
        "ping": {
            'args': [],
            'method': 'get',
            'name': 'ping',
            'route': '/ping',
            'stability': 'stable',
        },
        "uploadObject": {
            'args': ['name'],
            'input': 'v1/upload-object-request.json#',
            'method': 'post',
            'name': 'uploadObject',
            'route': '/upload/<name>',
            'stability': 'experimental',
        },
    }


__all__ = ['createTemporaryCredentials', 'config', '_defaultConfig', 'createApiClient', 'createSession', 'Object']
