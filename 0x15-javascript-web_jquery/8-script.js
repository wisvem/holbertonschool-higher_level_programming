const $ = window.$;
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.getJSON(url, function (data, status) {
  data.results.forEach(element => {
    const node = document.createElement('LI');
    const txtNode = document.createTextNode(element.title);
    node.appendChild(txtNode);
    document.getElementById('list_movies').appendChild(node);
  });
});
