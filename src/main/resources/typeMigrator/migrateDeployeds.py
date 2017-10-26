#
# Copyright 2017 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from com.xebialabs.deployit.plugin.api.udm.base import BaseDeployed
from com.xebialabs.deployit.plugin.api.udm import ConfigurationItem
from com.xebialabs.deployit.plugin.api.udm import Container
from com.xebialabs.deployit.plugin.api.validation import ValidationMessage

oldType = request.query['p1']
parent = request.query['p2']
ancestor = request.query['p3']

migratorModule = __import__('typeMigrator.' + oldType, fromlist=[''])

if parent is not None and parent.split('/')[0] != "Infrastructure":
  raise Exception("Invalid parent path: The path must be under Infrastructure.")

if ancestor is not None and ancestor.split('/')[0] != "Infrastructure":
  raise Exception("Invalid ancestor path: The path must be under Infrastructure.")

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

