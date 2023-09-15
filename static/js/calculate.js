const currencyFrom = document.querySelector('.converter__from');
const currencyTo = document.querySelector('.converter__to');
const amountField = document.querySelector('.amount');
const resultField = document.querySelector('.main__result');

const form = document.querySelector('form');
form.addEventListener('submit', getValue);

async function getValue(e) {
  e.preventDefault();
  try {
    let response = await fetch(`/api/rates?from=${currencyFrom.value}&to=${currencyTo.value}&value=${amountField.value}`);
    let result = await response.json();
    resultField.innerText = result['result'];
  } catch(err) {
    throw new Error(e.message);
  }
}