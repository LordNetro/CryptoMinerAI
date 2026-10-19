import React, { useState } from 'react';
import { Navbar, Container } from 'react-bootstrap';
import Login from './components/Login';
import Register from './components/Register';

function App() {
  const [isLoginView, setIsLoginView] = useState(true);

  const toggleView = () => {
    setIsLoginView(!isLoginView);
  };

  return (
    <>
      <Navbar bg="dark" variant="dark" expand="lg">
        <Container>
          <Navbar.Brand href="#home">CryptoMinerAI</Navbar.Brand>
        </Container>
      </Navbar>
      <main>
        {isLoginView ? <Login toggleView={toggleView} /> : <Register toggleView={toggleView} />}
      </main>
    </>
  );
}

export default App;
