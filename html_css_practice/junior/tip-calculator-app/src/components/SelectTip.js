import '../assets/styles/select-tip.css'
import { CheckData } from '../components/InputField'
import calcResult from './Calculate'

export let tipPercent

const SelectTip = () => {
  const percentsList = [5, 10, 15, 25, 50]
  
  return (
    <div className='select-tip'>
      <p className='select-tip__title'>
        Select Tip %
      </p>
      <div className='select-tip__buttons-container'>
        {percentsList.map((percent) => (
          <TipButton key={percent} percent={percent} />
        ))}
        <CustomField />
      </div>
    </div>
  )
}

export default SelectTip

const TipButton = (props) => {
  return (
    <button onClick={ButtonClicked}
     className='select-tip__button'>
      {props.percent}%
    </button>
  )
}

const CustomField = () => {
  return (
    <input type='text' 
    className='select-tip__custom'
    placeholder='Custom'
    id='custom-tip'
    onChange={CheckData}
    onFocus={ResetButtonColor} />
  )
}

const ButtonClicked = event => {
  ResetButtonColor()
  document.getElementById('custom-tip').value = ''
  
  event.target.style.backgroundColor = 'hsl(172, 67%, 45%)'
  event.target.style.color = 'hsl(183, 100%, 15%)'
  tipPercent = event.target.innerText.replace('%', '')
  calcResult()
}

export const ResetButtonColor = () => {
  const buttons = document.querySelectorAll('.select-tip__button')
  tipPercent = ''

  for (let i = 0; i < buttons.length; i++) {
    buttons[i].style.backgroundColor = 'hsl(183, 100%, 15%)';
    buttons[i].style.color = 'hsl(189, 41%, 97%)';
  }
}
