import React from 'react';

class NotificationPopup extends React.Component {
    constructor(props) {
      super(props);
    }
  
    handleChange(event) {    
        this.setState({value: event.target.value});  
    }
  
    render() {
      return (   
        <div id='popup'>
            <p> Call a function here to popup the message.</p>
            <p> The data has been processed.</p>
            <p> A notification has been sent to the doctor {/* state doctor */} </p>
            <button className='MenuButtons'>Continue</button>
        </div>
      );
    }
  }

  export default NotificationPopup;