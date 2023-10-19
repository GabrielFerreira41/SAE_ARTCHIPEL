import React, { useState } from 'react';
import { Modal, Button, Form } from 'react-bootstrap';
import '../style/styleAccueill.css';

const Header = () => {
  const [showModal, setShowModal] = useState(false);

  const handleShowModal = () => {
    setShowModal(true);
  };

  const handleCloseModal = () => {
    setShowModal(false);
  };
  
  return (
    <header className="bg-white">
      <nav className="navbar navbar-expand-lg navbar-light">
        <div className="container">
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item">
                <a className="nav-link fs-5" href="/">
                  Accueil
                </a>
              </li>
              <li className="nav-item">
                <a className="nav-link fs-5" href="/Info">
                  Info
                </a>
              </li>
              <li className="nav-item">
                <a className="nav-link fs-5" href="/Decouverte">
                  Découvertes
                </a>
              </li>
            </ul>
            <img
              className="line"
              alt="Line"
              src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/6511c7272274091aaeadcb28/img/line-6.svg"
            />
            <img
              className="img"
              alt="Line"
              src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/6511c7272274091aaeadcb28/img/line-7.svg"
            />
            <img
              className="line-2"
              alt="Line"
              src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/6511c7272274091aaeadcb28/img/line-8.svg"
            />
            <form className="form-inline ml-auto">
              <input
                className="form-control"
                type="search"
                placeholder="Recherche"
                aria-label="Recherche"
              />
              <button className="btn btn-outline-primary" type="submit">
                <i className="fas fa-search"></i>
              </button>
              <Button variant="primary" className="ml-2" href="/Connexion">
                Connexion
              </Button>
            </form>
          </div>
        </div>
      </nav>
    </header>
  );
};

export default Header;
