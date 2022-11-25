import '../assets/styles/input-field.css'

const InputField = (props) => {
  return (
    <div className='input-field-container'>
      <p className='input-field__title'>{props.title}</p>
      <input className={props.class} type='text' placeholder='0' />
    </div>
  )
}

export default InputField