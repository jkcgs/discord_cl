$(document).ready(function() {
  var table = $('#commands').DataTable( {
      "ajax": {
        "url": "/api/commands",
        "dataSrc": ""
      },
      'columns': [
          {
              'data': null,
              "targets": -1,
              'defaultContent': '<a><i class="fas fa-plus-circle"></i></a>',
              'width': '10px'
          },
          {'data': 'name'},
          {'data': 'short_desc'}
      ]
  });

  $('#commands tbody').on( 'click', 'a', function () {
        var data = table.row( $(this).parents('tr') ).data();
        alert( data['description'] || '(sin descripción)' );
    });
});