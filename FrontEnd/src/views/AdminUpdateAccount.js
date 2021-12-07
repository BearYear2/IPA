import TextForm from '../components/TextForm'

function AdminUpdateAccount() {

    function handleDelete(e) {
        e.preventDefault();    
        console.log('You clicked Delete.');
    }

    function handleUpdate(e) {
        e.preventDefault();    
        console.log('You clicked Update.');
    }

    return (
        <div>
            <TextForm placeholder={"Name and surname"}/>
            <TextForm placeholder={"CNP"}/>
            <TextForm placeholder={"Phone number"}/>
            <TextForm placeholder={"Email"}/>
            <button onClick={handleDelete}>DELETE</button>
            <button onClick={handleUpdate}>UPDATE</button>
        </div>
    );
}

export default AdminUpdateAccount;
