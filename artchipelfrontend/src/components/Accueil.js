import React from "react";
import "../style/styleAccueill.css";
import lieuImage from "../components/images/lieu.png";
import franceImage from "../components/images/france.png";
import calendrierImage from "../components/images/calendrier.png";
import destinationImage from "../components/images/destination.png";

const Accueil = () => {
  return (
    <div className="indexAccueil">
      <h1 className="titreNoir">Art <span className="motVert">Chipel</span></h1>
      <div className="bandeauVert"></div>
      <div className="boutons">
        <div className="carréVert"></div>
        <button className="boutonRond vert">
          <img src={lieuImage} alt="Lieu" />
        </button>
        <span>Lieu</span>

        <button className="boutonRond rose">
          <img src={franceImage} alt="France" />
        </button>
        <span>France</span>
        <button className="boutonRond bleu">
          <img src={calendrierImage} alt="Calendrier" />
        </button>
        <span>Calendrier</span>
        <button className="boutonRond rouge">
          <img src={destinationImage} alt="Destination" />
        </button>
        <span>Destination</span>
        <div className="carréVert"></div>
      </div>
    </div>
  );
};

export default Accueil;
