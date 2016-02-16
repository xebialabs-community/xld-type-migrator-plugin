/*
 * THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
 * FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
 */

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
      alert("Successfully migrated");
    },
    error: function(xhr, status, error) {
      alert(xhr.responseText);
    }
  });
}

