const node = document.createElement('LI');
const txtNode = document.createTextNode('Item');
node.appendChild(txtNode);
document.getElementsByClassName('my_list')[0].appendChild(node);
