// menutoggle
const toggle = document.querySelector('.toggle')
const navigation = document.querySelector('.navigation')
const main = document.querySelector('.main')
const contact = document.querySelector('.contact')

toggle.onclick = function () {
  navigation.classList.toggle('active')
  main.classList.toggle('active')
  contact.classList.toggle('active')
}
// add the hovered class in selected list//
const list = document.querySelectorAll('.navigation li')
function activeLink () {
  list.forEach((item) =>
    item.classList.remove('hovered'))
  this.classList.add('hovered')
}
list.forEach((item) =>
  item.addEventListener('mouseover', activeLink))
