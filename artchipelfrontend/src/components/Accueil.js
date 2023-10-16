import React from "react";
import "../style/styleAccueill.css";
import lieuImage from "../components/images/lieu.png";
import franceImage from "../components/images/france.png";
import calendrierImage from "../components/images/calendrier.png";
import destinationImage from "../components/images/destination.png";
import { Link } from 'react-router-dom';



const Accueil = () => {
  return (
    <div className="index">
    <div className="div">
    <p className="art-chipel">
        <span className="span">Art</span>
        <span className="text-wrapper-16">Chipel</span>
      </p>
      <div className="overlap-group">
        <div className="overlap-2">
          <div className="rectangle" />
          <img
            className="noah-buscher"
            alt="Noah buscher"
            src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/652d46c6dd97f0a699044dd5/img/noah-buscher-x8zstuks2pm-unsplash-1@2x.png"
          />
          <div className="text-wrapper">Parcours</div>
          <div className="rectangle-2" />
          <div className="rectangle-3" />
          <div className="text-wrapper-2">Organiser</div>
          <div className="text-wrapper-3">Profiter</div>
        </div>
        <div className="overlap-3">
          <div className="mask-group">
            <div className="overlap-group-2">
              <div className="rectangle-4" />
              <div className="rectangle-5" />
              <div className="rectangle-6" />
              <img
                className="tamas-tuzes-katai"
                alt="Tamas tuzes katai"
                src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/652d46c6dd97f0a699044dd5/img/tamas-tuzes-katai-ren-adbr3ig-unsplash-1@2x.png"
              />
              <Link to="/Carte">
                <img src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/652d46c6dd97f0a699044dd5/img/jakob-dalbjorn-cukjre3nyyc-unsplash-1@2x.png" alt="Calendrier" className="jakob-dalbjorn" />
            </Link>
              <div className="text-wrapper-4">Carte</div>
            </div>
          </div>
          <div className="text-wrapper-5">Découvrer</div>
          <div className="text-wrapper-6">Parcourez la Région Centre</div>
        </div>
        <div className="overlap-4">
          <div className="rectangle-7" />
          <div className="rectangle-8" />
          <div className="rectangle-9" />
          <div className="rectangle-10" />
          <div className="phil-hearing" />
          <Link to="/Evenement">
                <img src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/652d46c6dd97f0a699044dd5/img/jakob-dalbjorn-cukjre3nyyc-unsplash-1@2x.png" alt="Calendrier" className="jakob-dalbjorn" />
          </Link>
          <div className="text-wrapper-7">Evenements</div>
          <div className="text-wrapper-8">Participer</div>
          <div className="text-wrapper-9">Rencontrer</div>
          <div className="text-wrapper-10">Apprendre</div>
        </div>
        <div className="overlap-5">
          <div className="rectangle-11" />
          <div className="rectangle-12" />
          <div className="rectangle-13" />
          <div className="rectangle-14" />
          <Link to="/Lieux">
                <img src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/652d46c6dd97f0a699044dd5/img/image-1@2x.png" alt="France" className="image" />
          </Link>
          <div className="text-wrapper-11">Lieux</div>
          <div className="text-wrapper-12">Explorer</div>
          <div className="text-wrapper-13">Admirer</div>
          <div className="text-wrapper-14">Découvrir</div>
        </div>
        <p className="p">“Partez à la découverte des merveilleuses régions françaises !”</p>
      </div>      
    </div>
  </div>       
  );
};

export default Accueil;
