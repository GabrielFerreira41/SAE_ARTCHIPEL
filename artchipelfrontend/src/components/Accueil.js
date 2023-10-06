import React from "react";
import "../style/styleAccueill.css";
import lieuImage from "../components/images/lieu.png";
import franceImage from "../components/images/france.png";
import calendrierImage from "../components/images/calendrier.png";
import destinationImage from "../components/images/destination.png";

const imageStyle = {
  width: "5vw", // ajustez la largeur comme vous le souhaitez
  height: "10vh", // ajustez la hauteur comme vous le souhaitez
};

const Accueil = () => {
  return (
    <div className="indexAccueil">
      <h1 className="titreNoir display-1 mt-5 mb-5 pt-5 pb-5">Art <span className="motVert">Chipel</span></h1>
      <div className="bandeauVert"></div>
      <div className="container mt-3 pt-3">
        <div className="row justify-content-center align-items-center">
          <div className="col-sm-2">
            <div className="d-flex flex-column align-items-center">
              <button className="btn btn-success btn-sm mx-2">
                <img src={lieuImage} alt="Lieu" style={imageStyle} />
              </button>
              <span>Lieu</span>
            </div>
          </div>

          <div className="col-sm-2">
            <div className="d-flex flex-column align-items-center">
              <button className="btn btn-danger btn-sm mx-2">
                <img src={franceImage} alt="France" style={imageStyle} />
              </button>
              <span>France</span>
            </div>
          </div>

          <div className="col-sm-2">
            <div className="d-flex flex-column align-items-center">
              <button className="btn btn-primary btn-sm mx-2">
                <img src={calendrierImage} alt="Calendrier" style={imageStyle} />
              </button>
              <span>Calendrier</span>
            </div>
          </div>

          <div className="col-sm-2">
            <div className="d-flex flex-column align-items-center">
              <button className="btn btn-warning btn-sm mx-2">
                <img src={destinationImage} alt="Destination" style={imageStyle} />
              </button>
              <span>Destination</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Accueil;
