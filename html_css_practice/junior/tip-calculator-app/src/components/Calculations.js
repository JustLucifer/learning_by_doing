import '../assets/styles/calculations.css'
import { ResetButtonColor } from './SelectTip'

const Calculations = () => {
  return (
    <div className='calculations'>
      <div className='calculations__show-result-container'>
        <ShowResult title='Tip Amount' id='tip' />
        <ShowResult title='Total' id='total' />
      </div>
      <button className='calculations__reset-button' id='reset-button' onClick={resetAll}>
        RESET
      </button>
    </div>
  )
}

export default Calculations

export const ShowResult = (props) => {
  return (
    <div className='calculations__result-container'>
      <p className='calculations__title'>
        {props.title}<br/>
        <span className='calculations__title--gray-lower'>
          / person
        </span>
      </p>

      <p className='calculations__result' id={props.id}>
        $0.00
      </p>
    </div>
  )
}

const resetAll = () => {
  document.getElementById('bill').value = ''
  document.getElementById('people').value = ''
  const results = document.querySelectorAll('.calculations__result')
  for (let i = 0; i < results.length; i++) {
    results[i].innerText = '0.00'
  }

  ResetButtonColor()
}