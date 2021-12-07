import React from 'react';
import Interval from './Interval'

class BigInterval extends React.Component {
    constructor(props) {
        super(props);
      }

    render() {
    return ( 
        <div id='IntervalContainer'>  
            < Interval text='09:00 - 10:30' />
            < Interval text='10:30 - 12:00' />
            < Interval text='12:00 - 13:30' />
            < Interval text='13:30 - 15:00' />
            < Interval text='15:00 - 16:30' />
            < Interval text='16:30 - 18:00' />
            < Interval text='18:00 - 19:30' />
        </div>
        );
    }  
}

export default BigInterval;