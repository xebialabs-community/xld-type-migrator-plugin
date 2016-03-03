# xld-type-migrator-plugin v4.5.4

This plugin provides a UI screen that allows migration of an obsolete type to the new type that supersedes it.  

For deployables, the input is the obsolete type and deployment package info; the plugin will generate a new deployment package containing the new type in place of the old one.  A migration helper plugin containing a mapProperties.py method must be installed, for example, xld-type-migrator-was-plugin.

For deployeds, the input is an obsolote type and a parent or ancestor under the Infrastructure node.  A new type will be created in the same location as the obsolete type.
