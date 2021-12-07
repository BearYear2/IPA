import ClientRegisterCard from "../components/RegisterCard";

function ClientConfirmationForm() {

    function goBack(e) {
        e.preventDefault();    
        console.log('You clicked Back.');
    }

    function doConfirm(e) {
        e.preventDefault();    
        console.log('You clicked Confirm.');
    }

    return (
        <div id="registration">
            <div id="register-cards">
                <ClientRegisterCard />
                <ClientRegisterCard />
                <ClientRegisterCard />
            </div>
            <div className='button-container'>
                <button className='MenuButtons' onClick={goBack}>Back</button>
                <div id="PAGINATION HERE"></div>
                <button className='MenuButtons' onClick={doConfirm}>Confirm</button>
            </div>

        </div>
    );
}

export default ClientConfirmationForm;
