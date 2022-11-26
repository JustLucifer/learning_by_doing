import '../assets/styles/input-field.css'
import calcResult from './Calculate'

export let customTipValue

const InputField = (props) => {
  return (
    <div className='input-field-container'>
      <p className='input-field__title'>{props.title}</p>
      <input className={props.class}
       type='text'
       placeholder='0'
       id={props.id}
      onChange={CheckData} />
    </div>
  )
}

export default InputField

export const CheckData = event => {
  let value = event.target.value

  if (!Number.isFinite(+value)) {
    value = value.slice(0, -1)
    event.target.value = value
  } else {
    if (event.target.id === 'custom-tip') {
      customTipValue = event.target.value
    }
    calcResult(value)
  }
}
