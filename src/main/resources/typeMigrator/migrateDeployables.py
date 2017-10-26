#
# Copyright 2017 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from java.util import TreeSet
from datetime import datetime as dt
from com.xebialabs.deployit.plugin.api.udm.base import BaseDeployable
from com.xebialabs.deployit.plugin.api.reflect import Type

oldType = request.query['p1']
appId = request.query['p2']
oldVer = request.query['p3']
newVer = request.query['p4']

migratorModule = __import__('typeMigrator.' + oldType, fromlist=[''])

# Create a new deployment package
repositoryService.copy("%s/%s" % (appId, oldVer), "%s/%s" % (appId, newVer))

# Read the new deployment package
app = repositoryService.read("%s/%s" % (appId, newVer))

# Loop through the deployables
result = []
for item in app.getProperty('deployables'):
  deployable = repositoryService.read(item.id)
  if deployable.type == oldType:
    newDeployable = BaseDeployable()
    newDeployable.setId("%s/%s/%s" % (appId, newVer, "New" + deployable.name))
    newDeployable.setTags(TreeSet())
    migratorModule.mapProperties(deployable, newDeployable)
    result.append(newDeployable.getType().toString())
    repositoryService.create("%s/%s/%s" % (appId, newVer, "New" + deployable.name), newDeployable)
    repositoryService.delete(deployable.id)

response.entity = result
