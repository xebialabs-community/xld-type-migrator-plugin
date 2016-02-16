#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from java.util import TreeSet
from datetime import datetime as dt
from com.xebialabs.deployit.plugin.api.udm.base import BaseDeployable
from com.xebialabs.deployit.plugin.api.reflect import Type

import typeMigrator.wasServerConfigurationSpec.wasServerConfigurationSpec as wasServerConfigurationSpec

oldType = request.query['p1']
appId = request.query['p2']
oldVer = request.query['p3']
newVer = request.query['p4']

# Create a new deployment package
repositoryService.copy("%s/%s" % (appId, oldVer), "%s/%s" % (appId, newVer))

# Read the new deployment package
app = repositoryService.read("%s/%s" % (appId, newVer))

# Loop through the deployables
for item in app.getProperty('deployables'):
  deployable = repositoryService.read(item.id)
  if deployable.type == oldType:
    newDeployable = BaseDeployable()
#   newDeployable.setType(Type.valueOf("was.JavaProcessDefinitionSpec"))
    newDeployable.setId("%s/%s/%s" % (appId, newVer, "New" + deployable.name))
    newDeployable.setTags(TreeSet())
    wasServerConfigurationSpec.mapProperties(deployable, newDeployable)
    repositoryService.create("%s/%s/%s" % (appId, newVer, "New" + deployable.name), newDeployable)
    repositoryService.delete(deployable.id)
