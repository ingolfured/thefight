function clickmovie2 () {
$.ajax({
    type: 'POST',
    url: '/filesave/',
    data: {'path': dp, 'contents': contents},
    success: function (data, textStatus, jqXHR) {
      $("#status").html('');
      if (data.result == 'bad') {
        alert(data.error);
      }
    },
    error: 'No error', 
  });
}

function clickmovie1 () {
$.ajax({
    type: 'POST',
    url: '/filesave/',
    data: {'path': dp, 'contents': contents},
    success: function (data, textStatus, jqXHR) {
      $("#status").html('');
      if (data.result == 'bad') {
        alert(data.error);
      }
    },
    error: 'No error', 
  });
}
