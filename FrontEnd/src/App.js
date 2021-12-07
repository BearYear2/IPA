import React, { useState } from 'react';

import { BrowserRouter, Route, Switch } from 'react-router-dom';

import './App.css';
import RegisterCard from './components/RegisterCard'
import ClientConfirmationForm from './views/ClientConfirmation';
import ClientRegisterForm from './views/ClientRegister';
import LoginForm from './views/LoginForm';
import ConfirmationPopup from './components/ConfirmationPopup'
import UserMainScreen from './views/UserMainScreen'
import Calendar from './components/Calendar';
import Interval from './components/Interval';
import BigInterval from './components/BigInterval'
import AppointmentList from './components/AppointmentList';
import NurseMainScreen from './views/NurseMainScreen'
import SingleAppointmentReq from './components/SingleAppointmentReq';
import AppointmentRequests from './views/AppointmentRequests';
import AdminMainScreen from './views/AdminMainScreen'
import AdminCreateAccounts from './views/AdminCreateAccounts'
import AccountList from './views/AccountList'

function App() {
  
  const [token, setToken] = useState();

  function decideView(tk) {
    switch (tk) {
      case 'user':
        return (<UserMainScreen />);
      
      case 'nurse':
        return (<NurseMainScreen />);
      
      case 'admin':
        return (<AdminMainScreen />);

      default:
        return (
          <div>
            <p>No valid info</p>
            <LoginForm setToken={setToken}/>
          </div>
        )
    }
  }

  if(!token) {
    return (
      <body className="App">
        <div className="App-body">
          < LoginForm setToken={setToken}/>
        </div>
      </body>
      );
    }

  return (
    <body className="App">
      <div className="App-body">
        {decideView(token)}
      </div>
    </body>
    )
  }

export default App;
