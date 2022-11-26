import './App.css';
import Header from './components/Header';
import InputField from './components/InputField'
import SelectTip from './components/SelectTip'
import Calculations from './components/Calculations'

function App() {
  return (
    <div className="App">
      <Header />
      <main className='main-content'>
        <div className="fill-data-container">
          <InputField title='Bill' class='bill' id='bill' />
          <SelectTip />
          <InputField title='Number of People' class='people' id='people'/>
        </div>
        <Calculations />
      </main>
    </div>
  );
}

export default App;
