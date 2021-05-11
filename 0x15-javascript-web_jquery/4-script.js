document.getElementById('toggle_header').addEventListener('click', function () {
  // document.getElementsByTagName('header')[0].classList.add('red');
  if (document.getElementsByTagName('header')[0].className === 'green') {
    document.getElementsByTagName('header')[0].classList.add('red');
    document.getElementsByTagName('header')[0].classList.remove('green');
  } else if (document.getElementsByTagName('header')[0].className === 'red') {
    document.getElementsByTagName('header')[0].classList.add('green');
    document.getElementsByTagName('header')[0].classList.remove('red');
  }
});
