const $ = window.$;
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$.getJSON(url, function (data, status) {
  const txtNode = document.createTextNode(data.hello);
  document.getElementById('hello').appendChild(txtNode);
});
