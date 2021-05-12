
const $ = window.$;
document.onreadystatechange = function () {
  if (document.readyState === 'complete') {
    document.getElementById('add_item').addEventListener('click', function () {
      const node = document.createElement('LI');
      const txtNode = document.createTextNode('Item');
      node.appendChild(txtNode);
      $('.my_list')[0].appendChild(node);
    });
    document.getElementById('remove_item').addEventListener('click', function () {
      $('.my_list')[0].lastChild.remove();
    });
    document.getElementById('clear_list').addEventListener('click', function () {
      $('.my_list li').remove();
    });
  }
};
