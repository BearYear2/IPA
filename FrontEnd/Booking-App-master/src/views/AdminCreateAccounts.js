import TextForm from '../components/TextForm'
import { Person, AssignmentInd, AccountCircle, LocalPhone, Email } from '@mui/icons-material'; 

function AdminCreateAccounts() {

    function handleSubmit(e) {
        e.preventDefault();    
        console.log('You clicked submit.');
    }

    return (
        <div>
            <p className='prompt'>Create account:</p>
            <form className="Form" onSubmit={handleSubmit}>
                <div className="input-container">
                    <AccountCircle sx={{'fontSize':'2.5rem', 'flex':'10% 0.1'}}/>
                    <div id='radioContainer' className='input-style'>
                        <label className='radioChoice'><input type='radio' value='Medic' name='accountType' />Medic</label>
                        <label className='radioChoice'><input type='radio' value='Nurse' name='accountType' />Nurse</label>
                    </div>
                </div>
                <div className="input-container">
                    <Person sx={{'fontSize':'2.5rem', 'flex':'10% 0.1'}}/>
                    <TextForm className="input-style" placeholder={"Name and surname"}/>
                </div>
                <div className="input-container">
                    <AssignmentInd sx={{'fontSize':'2.5rem', 'flex':'10% 0.1'}}/>
                    <TextForm className="input-style" placeholder={"CNP"}/>
                </div>
                <div className="input-container">
                    <LocalPhone sx={{'fontSize':'2.5rem', 'flex':'10% 0.1'}}/>
                    <TextForm className="input-style" placeholder={"Phone number"} />
                </div>
                <div className="input-container">
                    <Email sx={{'fontSize':'2.5rem', 'flex':'10% 0.1'}}/>
                    <TextForm className="input-style" placeholder={"Email"} />
                </div>
                <div className="button-container">
                    <button className="MenuButtons">Go Back</button>
                    <button className="MenuButtons right">Confirm</button> 
                </div>
            </form>
        </div>

    );
}

export default AdminCreateAccounts;
