function LogoutButton() {
    
    function logout() {
        window.location.href='/';
    };

    return (
        <button onClick={logout} className="MenuButtons">Logout</button>
    )
}

export default LogoutButton;