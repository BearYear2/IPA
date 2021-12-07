import LogoutButton from '../components/LogoutButton'

function AdminMainScreen() {

    function fetchUsers() {
        //e.preventDefault();
        return("ADMIN NAME HERE")
    }

    function choseConfirmReg(e) {
        e.preventDefault();
        console.log("Clicked ConfirmReg");
    }

    function choseCreateAcc(e) {
        e.preventDefault();
        console.log("Clicked CreateAcc");
    }

    function choseManageAcc(e) {
        e.preventDefault();
        console.log("Clicked ManageAcc");
    }

    return (
        <div className="main-screen">
            <p>Admin: {fetchUsers()}</p>
            <button className="MenuButtons mainButton" onClick={choseConfirmReg}>Confirm Registrations</button>
            <button className="MenuButtons mainButton" onClick={choseCreateAcc}>Create Accounts</button>
            <button className="MenuButtons mainButton" onClick={choseManageAcc}>Manage Accounts</button>
            < LogoutButton />
        </div>
    );
}

export default AdminMainScreen;
