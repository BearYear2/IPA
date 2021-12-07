import TextForm from '../components/TextForm'
import PasswordForm from '../components/PasswordForm'
import { Person, Lock, AssignmentInd } from '@mui/icons-material';

import { useNavigate } from 'react-router-dom';

function ClientRegisterForm() {

    const navigate = useNavigate();

    function handleSubmit(e) {
        e.preventDefault();    
        console.log('You clicked submit.');
    }

    return (
        <form className="Form" onSubmit={handleSubmit}>
            <div className="input-container">
                <Person sx={{'fontSize':'2.5rem', 'flex':'10% 0.1'}}/>
                <TextForm className="input-style" placeholder={"Name"}/>
            </div>
            <div className="input-container">
                <Lock sx={{'fontSize':'2.5rem', 'flex':'10% 0.1'}}/>
                <PasswordForm className="input-style" />
            </div>
            <div className="input-container">
                <AssignmentInd sx={{'fontSize':'2.5rem', 'flex':'10% 0.1'}}/>
                <TextForm className="input-style" placeholder={"CNP"}/>
            </div>
            <div className="button-container">
                <button onClick={() => navigate(-1)} className="MenuButtons">Go Back</button>
                <button type='submit' className="MenuButtons right">Confirm</button> 
            </div>
        </form>
    );
}

export default ClientRegisterForm;
