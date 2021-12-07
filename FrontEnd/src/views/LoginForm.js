import React, { useState } from 'react';
import PropTypes from 'prop-types';

import { Routes, Route, useNavigate } from 'react-router-dom';

import TextForm from '../components/TextForm'
import PasswordForm from '../components/PasswordForm'
import { Lock, Person } from '@mui/icons-material';
import ClientRegisterForm from './ClientRegister';

function LoginForm({ setToken }) {

    const navigate = useNavigate();

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    function handleSubmit(e) {
        e.preventDefault();    
        setToken(username);
    }

    function clickRegister(e) {
        e.preventDefault();
        navigate('/register');
    }

    return (
        <div>
            <Routes>
                <Route path='/' element={
                            <form className="Form" onSubmit={handleSubmit}>
                            <div className="input-container">
                                <Person sx={{'fontSize':'2.5rem', 'flex':'10% 0.1'}}/>
                                <TextForm className="input-style" placeholder={"Name"} value={username} onChange={e => setUsername(e.target.value)}/>
                            </div>
                            <div className="input-container">
                                <Lock sx={{'fontSize':'2.5rem', 'flex':'10% 0.1'}}/>
                                <PasswordForm className="input-style" value={password} onChange={e => setPassword(e.target.value)}/>
                            </div>
                            <div className="button-container">
                                <button type='submit' className="MenuButtons">Login</button>
                                <button onClick={clickRegister} className="MenuButtons right">Register</button> 
                            </div>
                        </form>
                } />
                <Route path='/register' element={< ClientRegisterForm />} />
            </Routes>
        </div>
    );
}

export default LoginForm;

LoginForm.propTypes = {
    setToken: PropTypes.func.isRequired
  }
