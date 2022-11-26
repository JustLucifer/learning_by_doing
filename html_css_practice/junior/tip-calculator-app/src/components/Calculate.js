import { tipPercent } from './SelectTip'
import { customTipValue } from './InputField'

const calcResult = () => {
  const bill = +document.getElementById('bill').value.trim()
  const people = +document.getElementById('people').value.trim()
  let tip = 0

  if (people == '' || people == 0 || bill == '' || bill == 0) {
    updateResult('0.00', '0.00')
    DimResetButton()
    return
  }

  if (tipPercent) {
    tip = bill * (+tipPercent / 100)
  } else if (customTipValue) {
    tip = bill * (+customTipValue / 100)
  }

  const tipAmount = String(Math.ceil((tip / people) * 100) / 100)
  const total = String(Math.ceil((bill + tip) / people * 100) / 100)

  updateResult(tipAmount, total)
  LightResetButton()
}

export default calcResult

const updateResult = (tipAmount, total) => {
  const tip = document.getElementById('tip')
  const sum = document.getElementById('total')
  tip.innerText = `$${tipAmount}`
  sum.innerText = `$${total}`
}

const LightResetButton = () => {
  const resetButton = document.getElementById('reset-button')
  resetButton.style.opacity = '1'
}

export const DimResetButton = () => {
  const resetButton = document.getElementById('reset-button')
  resetButton.style.opacity = '.5'
}
