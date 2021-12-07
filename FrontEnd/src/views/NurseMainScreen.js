import LogoutButton from '../components/LogoutButton'

function NurseMainScreen() {

    function fetchUsers() {
        //e.preventDefault();
        return("NURSE NAME HERE")
    }

    function choseApprove(e) {
        e.preventDefault();
        console.log("Clicked Approve");
    }

    function choseBookPhys(e) {
        e.preventDefault();
        console.log("Clicked BookPhys");
    }

    return (
        <div className="main-screen">
            <p>Nurse: {fetchUsers()}</p>
            <button className="MenuButtons mainButton" onClick={choseApprove}>Approve patient appointment</button>
            <button className="MenuButtons mainButton" onClick={choseBookPhys}>Book physician for patient</button>
            < LogoutButton />
        </div>
    );
}

export default NurseMainScreen;
