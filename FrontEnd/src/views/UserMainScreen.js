import { useNavigate, Route, Routes } from 'react-router-dom';
import Calendar from '../components/Calendar';
import LogoutButton from '../components/LogoutButton'
import AppointmentList from '../components/AppointmentList'

function UserMainScreen() {

    const navigate = useNavigate();

    function fetchUsers() {
        //e.preventDefault();
        return("USERNAME HERE")
    }

    function choseBook(e) {
        e.preventDefault();
        navigate('/book');
    }

    function seeAppointments(e) {
        e.preventDefault();
        navigate('/appointments');
    }

    return (
        <div>
            <Routes>
                <Route path='/' element={ 
                <div className="main-screen">
                    <p>User: {fetchUsers()}</p>
                    <button className="MenuButtons mainButton" onClick={choseBook}>Book appointment</button>
                    <button className="MenuButtons mainButton" onClick={seeAppointments}>Your appointments</button>
                    < LogoutButton />
                </div>
                }
                />
                <Route path='/book' element={<Calendar/>} />
                <Route path='/appointments' element={<AppointmentList/>} />
            </Routes>
        </div>
    );
}

export default UserMainScreen;
