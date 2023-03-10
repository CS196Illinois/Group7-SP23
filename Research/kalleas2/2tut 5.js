const Home = () => {

    const handleClick = (e) => {
        console.log('Hello, ninjas', e);
    }

    const handleCkickAgain = (name, e) => {
        console.log('hello ' + name, e.target);
    }

    return ( 
        <div className="home">
            <h2></h2>
            <button onClick={handleClick}>Click me</button>
            <button onClick={(e) => handleClickAgain('mario')}>Click me again</button>
        </div>
     );
}
 
export default Home;