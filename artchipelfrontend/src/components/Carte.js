import React from "react";
import "../style/styleCarte.css";

const Carte = () => {
  return (
    <div>
        <div className="bandeauJaune"><h1 className="titreBlanc p-5">Carte</h1></div>
        <iframe frameborder="0" width="1920" height="750" src="https://data.centrevaldeloire.fr/map/embed/artchipel/?&static=false&scrollWheelZoom=true"></iframe>
    </div>

  );
};
export default Carte;
