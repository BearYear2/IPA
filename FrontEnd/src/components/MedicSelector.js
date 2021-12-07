import React from 'react';

class MedicSelector extends React.Component {
    constructor(props) {
      super(props);
      this.fetchMedics = this.fetchMedics.bind(this);
    }
  
    fetchMedics(event) {    
        return("Maria Renard");  
    }
  
    render() {
      return (   
        <select id='medic-selector'>
            {/* For each fetched medic. */}
            <option value='1'>{this.fetchMedics()}</option>
        </select>
      );
    }
  }

  export default MedicSelector;