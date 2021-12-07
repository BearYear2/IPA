import React from 'react';
import Interval from '../components/Interval'
import Calendar from '../components/Calendar';
import MedicSelector from '../components/MedicSelector';

function CalendarView() {

    return (
        <div>
            <p>Please choose your medic:</p>
            < MedicSelector />
            
            <p>Please select an interval:</p>
            < Interval text="First interval" />
            < Interval text="Second interval" />

            <p>Please choose a month.</p>
            < Calendar />

        </div>
        
    );
}

export default CalendarView;
