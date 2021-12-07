import React from 'react';

class PasswordForm extends React.Component {
    constructor(props) {
      super(props);
    }
  
    render() {
      return (   
        <input type="password" className={this.props.className || ""}  placeholder={"Password"} value={this.props.value} onChange={ this.props.onChange } />
      );
    }
  }

  export default PasswordForm;