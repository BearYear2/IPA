import React from 'react';

class Interval extends React.Component {
    constructor(props) {
      super(props);
      this.cnsl = this.cnsl.bind(this);
    }

    cnsl(e) {
      e.preventDefault();
      console.log("YOU DID IT")
    }
  
    render() {
      return (   
        <div className="interval">
            <p>{this.props.text || "Interval"}</p>
            <button onClick={this.cnsl} className='availabilityButton'>X</button>
        </div>
      );
    }
  }

  export default Interval;
