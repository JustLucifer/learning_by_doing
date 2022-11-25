import '../assets/styles/calculations.css'

const Calculations = () => {
  return (
    <div className='calculations'>
      <div className='calculations__show-result-container'>
        <ShowResult title='Tip Amount' />
        <ShowResult title='Total' />
      </div>
      <button className='calculations__reset-button'>
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

      <p className='calculations__result'>
        $0.00
      </p>
    </div>
  )
}
