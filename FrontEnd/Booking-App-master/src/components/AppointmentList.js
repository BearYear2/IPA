import React from 'react';
import { useNavigate } from 'react-router-dom';

//Use for medic and user.

function AppointmentList(props) {

  const navigate = useNavigate();

  function fetchAppointments(event) {    
      return("Tuesday, 12th of November, 8PM.");  
  }

    return (   
      <div id='intervalField'>
        <div className='appointment-card'>
            {/* For each appointment. */}
            {/* < Appointment ((with cancel appointment button.)) /> */}
            <p>Appointment A for hour X in date Z.</p>
            <p>Same stuff but different.</p>
            <p>Weird retrieval of data.</p>
            <p>Weird retrieval of data.</p>
            <p>Weird retrieval of data.</p>
            <p>Weird retrieval of data.</p>
            <p>Weird retrieval of data.</p>
            <p>Weird retrieval of data.</p>
            <p>Weird retrieval of data.</p>
            <p>Weird retrieval of data.</p>
            <p>Weird retrieval of data.</p>
            <p>Weird retrieval of data.</p>
        </div>
        <button onClick={() => navigate(-1)} className="MenuButtons">Back</button>
      </div>
    )
  }

  export default AppointmentList;