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
        <InputField title='Bill' class='bill' />
        <SelectTip />
        <InputField title='Number of People' class='people' />
        <Calculations />
      </main>
    </div>
  );
}

export default App;
