const $ = window.$;
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$.getJSON(url, function (data, status) {
  const txtNode = document.createTextNode(data.name);
  document.getElementById('character').appendChild(txtNode);
});
