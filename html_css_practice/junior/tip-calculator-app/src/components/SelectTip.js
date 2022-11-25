import '../assets/styles/select-tip.css'

const SelectTip = () => {
  const percentsList = [5, 10, 15, 25, 50]
  
  return (
    <div className='select-tip'>
      <p className='select-tip__title'>
        Select Tip %
      </p>
      <div className='select-tip__buttons-container'>
        {percentsList.map((percent) => (
          <TipButton key={percent} percent={percent}/>
        ))}
        <CustomField />
      </div>
    </div>
  )
}

export default SelectTip

const TipButton = (props) => {
  return (
    <button className='select-tip__button'>{props.percent}%</button>
  )
}

const CustomField = () => {
  return (
    <input type='text' 
    className='select-tip__custom'
    placeholder='Custom' />
  )
}
