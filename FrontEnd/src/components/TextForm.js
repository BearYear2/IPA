import React from 'react';

class TextForm extends React.Component {
    constructor(props) {
      super(props);
    }
  
    render() {
      return (   
        <input type="text" className={this.props.className || ""} placeholder={this.props.placeholder || "Text"} value={this.props.value} onChange={ this.props.onChange } />
      );
    }
  }

  export default TextForm;