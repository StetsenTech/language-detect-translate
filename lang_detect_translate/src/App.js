import React, { Component } from 'react';
import './App.css';
import {FormComponent} from './components/formComponent.jsx'

class App extends Component {
  render() {
    return (
      <div className="App">
        <FormComponent/>
      </div>
    );
  }
}

export default App;
