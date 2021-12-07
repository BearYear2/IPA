import { Person, AssignmentInd, Close, Check } from '@mui/icons-material';

function ClientRegisterCard() {

    function acceptRegister(e) {
        e.preventDefault();    
        console.log('You clicked accept.');
    }

    function declineRegister(e) {
        e.preventDefault();    
        console.log('You clicked decline.');
    }
    return (
        <div class="card">
            <div className="input-card">
                <Person sx={{'fontSize':'45px'}}/>
                <input className="fetched-inputs" type="text" value={"Fetch Name"} disabled={true}/>
            </div>

            <div className="input-card">
                <AssignmentInd sx={{'fontSize':'45px'}}/>
                <input className="fetched-inputs" type="text" value={"Fetch Name"} disabled={true}/>
            </div>

            <div className='accept-deny-buttons'>
                <Close sx={{'marginRight': '30%', 'fontSize':'45px'}} />
                <Check sx={{'marginLeft': '30%', 'fontSize':'45px'}} />
            </div>

        </div>
    );
}

export default ClientRegisterCard;
