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
        <div className="overlap-group">
          <div className="rectangle" />
          <img
            className="noah-buscher"
            alt="Noah buscher"
            src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/655633910d79d153e0ed390c/img/noah-buscher-x8zstuks2pm-unsplash-2.png"
          />
          <div className="rectangle-2" />
          <div className="text-wrapper">Parcours</div>
          <img
            className="image"
            alt="Image"
            src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/655633910d79d153e0ed390c/img/image-2.png"
          />
          <div className="rectangle-3" />
          <div className="rectangle-4" />
          <div className="rectangle-4" />
          <div className="text-wrapper-2">Lieux</div>
          <img
            className="tamas-tuzes-katai"
            alt="Tamas tuzes katai"
            src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/655633910d79d153e0ed390c/img/tamas-tuzes-katai-ren-adbr3ig-unsplash-2.png"
          />
          <div className="rectangle-5" />
          <div className="text-wrapper-3">Carte</div>
          <img
            className="jakob-dalbjorn"
            alt="Jakob dalbjorn"
            src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/655633910d79d153e0ed390c/img/jakob-dalbjorn-cukjre3nyyc-unsplash-2.png"
          />
          <div className="rectangle-6" />
          <div className="text-wrapper-4">Evenement</div>
          <img
            className="img"
            alt="Image"
            src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/655633910d79d153e0ed390c/img/image-4.png"
          />
          <p className="p">“Partez à la découverte du Centre Val de Loire”</p>
          <p className="bienvenue-dans-la">
            “ Bienvenue dans la magie du Centre-Val de Loire ! Explorez la vallée de la Loire avec ses châteaux
            emblématiques, plongez dans des vignobles d&#39;exception, et découvrez des paysages naturels à couper le
            souffle. Notre site vous ouvre les portes d&#39;une expérience unique, mêlant histoire, gastronomie, et
            charme à la française. Offrez-vous une escapade inoubliable au cœur de cette région captivante. Vivez la
            France authentique avec le Centre-Val de Loire ! “
          </p>
          <div className="text-wrapper-5">A PROPOS</div>
          <div className="text-wrapper-6">PLAN DU SITE</div>
          <div className="text-wrapper-7">ACCESSIBILITE</div>
          <div className="text-wrapper-8">MENTION LEGALES</div>
          <img
            className="line"
            alt="Line"
            src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/655633910d79d153e0ed390c/img/line-25.svg"
          />
          <img
            className="line-2"
            alt="Line"
            src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/655633910d79d153e0ed390c/img/line-6.svg"
          />
          <img
            className="line-3"
            alt="Line"
            src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/655633910d79d153e0ed390c/img/line-7.svg"
          />
          <img
            className="line-4"
            alt="Line"
            src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/655633910d79d153e0ed390c/img/line-8.svg"
          />
          <img
            className="image-2"
            alt="Image"
            src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/655633910d79d153e0ed390c/img/image-14.png"
          />
        </div>
      </div>
    </div>   
  );
};

export default Accueil;
