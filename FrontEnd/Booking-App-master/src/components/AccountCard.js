import React from 'react';

class AccountCard extends React.Component {
    constructor(props) {
      super(props);
    }
  
    fetchMedics(event) {    
        return("Maria Renard");  
    }
  
    render() {
      return (   
        <div id='account-card'>
            <p>Account status: {/*status*/}</p>
            <p>Account ID: {/*ID*/}</p>
            <button className="MenuButtons">Select this account</button>
        </div>
      );
    }
  }

  export default AccountCard;