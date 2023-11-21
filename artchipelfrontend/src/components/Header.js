import React from 'react';
import "../style/styleHeader.css";

const Header = () => {
  return (
    <header class='index'>
      <div className="overlap">
        <img
        className="vector"
        alt="Vector"
        src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/655633910d79d153e0ed390c/img/vector.svg"/>
      </div>
      <div className="text-wrapper-9">Découvertes</div>
      <div className="text-wrapper-10">Recherche</div>
      <div className="vector-wrapper">
        <img
        className="vector-2"
        alt="Vector"
        src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/655633910d79d153e0ed390c/img/vector-1.svg"/>
      </div>
      <img
      className="vector-3"
      alt="Vector"
      src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/655633910d79d153e0ed390c/img/vector-2.svg"/>
      <img
      className="image-3"
      alt="Image"
      src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/655633910d79d153e0ed390c/img/image-12.png"/>
  </header>
  );
};

export default Header;
