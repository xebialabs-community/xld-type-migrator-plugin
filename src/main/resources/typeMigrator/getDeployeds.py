#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from com.xebialabs.deployit.plugin.api.reflect import Type

result = []
objs = repositoryService.query(Type.valueOf(request.query['type'],request.query['parent'],request.query['ancestor'],request.query['namePattern'],None,None,1,-1)
for obj in objs:
	result.append(obj)

response.entity = result
