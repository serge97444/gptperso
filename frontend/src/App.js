import logo from './logo.svg';
import './App.css';
import Input_User from './Input_User'
import React, { Component }  from 'react';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <div>
         <Input_User/>
         </div>
      </header>
    </div>
  );
}

export default App;
