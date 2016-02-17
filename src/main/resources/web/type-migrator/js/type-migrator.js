/*
 * THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
 * FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
 */

String.prototype.format = function () {
  var args = arguments;
  return this.replace(/\{\{|\}\}|\{(\d+)\}/g, function (m, n) {
    if (m == "{{") { return "{"; }
    if (m == "}}") { return "}"; }
    return args[n];
  });
};

function migrate() {
  p1 = $('#obsoleteType').val();
  p2 = $('#applicationPath').val();
  p3 = $('#oldVerNum').val();
  p4 = $('#newVerNum').val();
  $.ajax({
    datatype: "json",
    url: "/api/extension/type-migrator/migrate?p1=" + p1 + "&p2=" + p2 + "&p3=" + p3 + "&p4=" + p4,
    crossDomain: true,
    beforeSend: function(xhr) {
      var base64 = parent.getAuthToken();
      xhr.setRequestHeader("Authorization", base64);
    },
    success: function(data) {
      message = "{0} {2}/{3}/{1} to {2}/{4}/{5}".format("Successfully migrated", p1, p2, p3, p4, data.entity);
      alert(message);
    },
    error: function(xhr, status, error) {
      alert(xhr.responseText);
    }
  });
}
