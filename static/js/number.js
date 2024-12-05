const selectNumber = document.getElementById('SelectedNumber')
const inputNumber = document.getElementById('phone_number')

selectNumber.addEventListener('change', function () {
  const selectedOption = JSON.parse(selectNumber.value)
  console.log(selectedOption) // Debugging line
  const contact = selectedOption.contact
  inputNumber.value = contact
})
