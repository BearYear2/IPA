import React from 'react';
import MedicSelector from '../components/MedicSelector'
import SingleAppointmentReq from '../components/SingleAppointmentReq';

function AppointmentRequests() {

    function fetchClientRequests() {
        /* Fetch the client requests here. Name and hour. */
    }

    return (
        <div className='approvalAppointments'>
            <div id='medicSelection'>
                <p>Please choose your medic:</p>
                < MedicSelector />
            </div>
            <div className='appointment-card nonFixed'>
            { /* For each appointment request */ }
                < SingleAppointmentReq />
                < SingleAppointmentReq />
                < SingleAppointmentReq />
                < SingleAppointmentReq />
                < SingleAppointmentReq />
            </div>
        </div>
    );
}

export default AppointmentRequests;
