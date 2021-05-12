const $ = window.$;
document.onreadystatechange = function () {
  if (document.readyState === 'complete') {
    $('#btn_translate').on('click', function () {
      const lc = $('#language_code').val();
      const url = 'https://fourtonfish.com/hellosalut/?lang=' + lc;
      $.getJSON(url, function (data, status) {
        $('#hello').text(data.hello);
      });
    });
  }
};
