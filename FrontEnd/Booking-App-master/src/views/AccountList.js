import React from 'react';
import AccountCard from '../components/AccountCard';

class AccountList extends React.Component {
    constructor(props) {
      super(props);
      this.fetchAccounts = this.fetchAccounts.bind(this);
    }
  
    fetchAccounts(event) {    
        return("Doctor, 011X1");  
    }
  
    render() {
      return (   
        <div className='approvalAppointments'>
            <p className='prompt'>Accounts:</p>
            <div className='appointment-card nonFixed'>
              {/* For each account. */}
              < AccountCard />
              < AccountCard />
              < AccountCard />
              < AccountCard />
              < AccountCard />
          </div>
        </div>
      );
    }
  }

  export default AccountList;