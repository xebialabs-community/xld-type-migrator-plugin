#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from com.xebialabs.deployit.plugin.api.udm.base import BaseDeployed
from com.xebialabs.deployit.plugin.api.udm import ConfigurationItem
from com.xebialabs.deployit.plugin.api.udm import Container
from com.xebialabs.deployit.plugin.api.validation import ValidationMessage

oldType = request.query['p1']
parent = request.query['p2']
ancestor = request.query['p3']

migratorModule = __import__('typeMigrator.' + oldType, fromlist=[''])

items = repositoryService.query(Type.valueOf(oldType),parent,ancestor,None,None,None,1,-1)

# Loop through the objects found
result = []
for item in items:
  oldItem = repositoryService.read(item.id)
  if oldItem.type == oldType:
    itemParent = '/'.join(oldItem.id.split('/')[0:-1])
    newItem = BaseDeployed()
    newItem.setId("%s/%s" % (itemParent, "New" + oldItem.name))  
    migratorModule.mapProperties(oldItem, newItem)
    result.append(newItem.getType().toString())
    repositoryService.create("%s/%s" % (itemParent, "New" + oldItem.name), newItem)

response.entity = result

