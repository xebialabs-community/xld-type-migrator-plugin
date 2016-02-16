#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from com.xebialabs.deployit.plugin.api.reflect import Type

def mapProperties(old, new):
  new.setType(Type.valueOf("was.JavaProcessDefinitionSpec"))
  if old.JavaVirtualMachine_classpath is not None:    	
    new.setProperty('JavaVirtualMachine_classpath', old.JavaVirtualMachine_classpath)
  if old.JavaVirtualMachine_bootClasspath is not None:
  	new.setProperty('JavaVirtualMachine_bootClasspath', old.JavaVirtualMachine_bootClasspath)
  if old.JavaVirtualMachine_verboseModeClass is not None:
  	new.setProperty('JavaVirtualMachine_verboseModeClass', old.JavaVirtualMachine_verboseModeClass)
  if old.JavaVirtualMachine_verboseModeGarbageCollection is not None:
  	new.setProperty('JavaVirtualMachine_verboseModeGarbageCollection', old.JavaVirtualMachine_verboseModeGarbageCollection)
  if old.JavaVirtualMachine_verboseModeJNI is not None:
  	new.setProperty('JavaVirtualMachine_verboseModeJNI', old.JavaVirtualMachine_verboseModeJNI)
  if old.JavaVirtualMachine_initialHeapSize is not None:
  	new.setProperty('JavaVirtualMachine_initialHeapSize', old.JavaVirtualMachine_initialHeapSize)
  if old.JavaVirtualMachine_maximumHeapSize is not None:
  	new.setProperty('JavaVirtualMachine_maximumHeapSize', old.JavaVirtualMachine_maximumHeapSize)
  if old.JavaVirtualMachine_genericJvmArguments is not None:
    new.setProperty('JavaVirtualMachine_genericJvmArguments', old.JavaVirtualMachine_genericJvmArguments)
  if old.JavaVirtualMachine_disableJIT is not None:
    new.setProperty('JavaVirtualMachine_disableJIT', old.JavaVirtualMachine_disableJIT)
# TODO: 
  if old.jvmCustomProperties is not None:
    map = {}
    map['newtestkey'] = 'newtestvalue'
#   parse the custom properties
    new.setProperty('JavaVirtualMachine_customProperties', map)

