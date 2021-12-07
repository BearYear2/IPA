import React from 'react';

class SingleAppointmentReq extends React.Component {
    constructor(props) {
      super(props);
    }

  
    render() {
      return (   
        <div id='appointment-req-card'>
            <p>Client {this.name || "NO NAME"} requests an appointment at {this.hour || "NO HOUR"} </p>
            <div>
              <button className='yesNo'>Deny</button>
              <button className='yesNo'>Accept</button>
            </div>
        </div>
      );
    }
  }

  export default SingleAppointmentReq;