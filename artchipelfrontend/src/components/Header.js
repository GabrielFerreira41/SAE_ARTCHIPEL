import React from 'react';
import '../style/styleHeader.css';

import { Link } from 'react-router-dom';

const Header = () => {
  return (
    <header className='d-flex m-3'>
      <nav class="navbar navbar-expand-lg navbar-light navHeader">
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a href={`/`} class="nav-link fs-5">Accueil</a>
            </li>
            <li class="nav-item">
              <a href={`/Decouverte`} class="nav-link fs-5">Découverte</a>
            </li>
            <li class="nav-item">
              <a href={`/Parcours`} class="nav-link fs-5">Parcours</a>
            </li>
          </ul>
          <div className='Bleu'></div>
          <div className='Blanc'></div>
          <div className='Rouge'></div>
        </div>
        <form class="d-flex searchBar">
          <input class="form-control me-sm-2" type="search" placeholder="Lieux / Parcours / Oeuvres"></input>
            <button class="btn btn-secondary my-2 my-sm-0" type="submit">Search</button>
        </form>
      </nav>




    </header>
  );
};

export default Header;
