# xlr-tfs2015-plugin v1.0.1

This plugin offers a rudimentary interface from XL Release to Team Foundation Server 2015.  It provides a configuration item for a TFS 2015 server and a createWorkItem.py script that creates a Work Item given Collection, Project, Type and Title parameters.

The functionality will be enriched with additional Work Item fields as specific needs materialize.

Note:  HttpRequest.py in XL Release must be enhanced to support the HTTP PATCH method.  See https://github.com/droberts2013/xl-release/server/src/main/resources/pythonutil/HttpRequest.py.  Place this custom file in <xl-release-server>/ext/pythonutil.
