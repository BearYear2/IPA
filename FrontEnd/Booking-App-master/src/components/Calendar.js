//Make February conditionally display 29 days if leap year.

import React, { useState } from 'react';
import range from '../helpers/range'
import monthLength from '../helpers/monthLength'
import BigInterval from './BigInterval';
import { useNavigate } from 'react-router-dom';

function Calendar(props) {
  
  const navigate = useNavigate();

  const [monthSelection, setMonthSelection] = useState('1');
  const [year, setYear] = useState(new Date().getFullYear());
  const [medic,setMedic] = useState('Rosa');

  function handleMonthChange(event) {
    setMonthSelection(event.target.value);
  }

  function handleYearChange(event) {
    setYear(event.target.value);
  }

  function handleMedicChange(event) {
    setMedic(event.target.value);
  }

  function clickDiv(event) {
    console.log(`Clicked on ${event.target}`);
  }

      const numbers = range(1, monthLength[monthSelection][1], 1);
      return (
        <div id='dateCalendarPicker'>

          <div id='intervalField'>
            <p>Please select a free interval for the date:</p>
            < BigInterval />
            <button onClick={() => navigate(-1)} className="MenuButtons">Back</button>
          </div>


          <div id='calendarContainer'>

            <div id="selectors">

              <select id='medicSelector' onChange={handleMedicChange}>
                <option value='John'>John</option>
                <option value='Rosa'>Rosa</option>
                <option value='Mary'>Mary</option>
              </select>

              <select id='yearSelector' onChange={handleYearChange}>
                <option value='2021'>2021</option>
                <option value='2022'>2022</option>
                <option value='2023'>2023</option>
              </select>

              <select id='monthSelector' onChange={handleMonthChange}>
                  {Object.entries(monthLength).map(([key, value]) =>
                  <option key={key} value={key}>{value[0]}</option>)}
              </select>
            </div>

            <div id="dayContainer" onClick={clickDiv}>
                {numbers.map((number) =>
                <div key={number.toString()} className="day">{`${number}`}</div>)}
            </div>

          </div>
        </div>
    );
  }

  export default Calendar;
