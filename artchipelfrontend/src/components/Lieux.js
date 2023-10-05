import React from "react";
import '../style/styleLieux.css'

const Lieux = () => {
  return (
    <div className="index">
      <div className="div">
        <div className="overlap">
          <div className="text-wrapper">Monuments</div>
          <div className="rectangleLieux" />
          <div className="text-wrapper-2">Monuments</div>
          <img
            className="image-removebg"
            alt="Image removebg"
            src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/6512f433b8281b7f84dcefa8/img/image-removebg-preview-2--1.png"
          />
        </div>
        <div>Loir-et-Cher (41)</div>
        <div className="rectangle-mini" />
        <div>Loiret (45)</div>
        <div className="rectangle-mini" />
        <div>Cher (18)</div>
        <div className="rectangle-mini" />
        <div>Eure-et-Loir (28)</div>
        <div className="rectangle-mini" />
        <div>Indre (36)</div>
        <div className="rectangle-mini" />
        <div>Indre-et-Loire (37)</div>
        <div className="rectangle-mini" />

      </div>
    </div>
  );
};
export default Lieux;
