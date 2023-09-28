import React from "react";
import "../style/styleAccueill.css";
function handleClick() {
  // Code à exécuter lorsque l'élément est cliqué
  console.log("L'élément a été cliqué !");
  // Vous pouvez ajouter ici la logique que vous souhaitez exécuter
}

const Accueil = () => {
  return (
    <div className="indexAccueil">
      <div className="div">

        <p className="art-chipel">
          <span className="span">Art</span>
          <span className="text-wrapper-2">Chipel</span>
        </p>
        <div className="overlap-group-2">
          <div className="waazup-cartoon-wrapper">
            <img
              className="waazup-cartoon"
              alt="Waazup cartoon"
              src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/6511c7272274091aaeadcb28/img/waazup-cartoon-wallpaper-website-with-louvre-nature-5dedf086-7c1.png"
            />
          </div>
          <div className="img-wrapper">
            <img
              className="waazup-cartoon-2"
              alt="Waazup cartoon"
              src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/6511c7272274091aaeadcb28/img/waazup-cartoon-wallpaper-website-with-french-monumentand-nature-.png"
            />
          </div>
          <div className="overlap-2">
            <img
              className="waazup-cartoon-3"
              alt="Waazup cartoon"
              src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/6511c7272274091aaeadcb28/img/waazup-cartoon-wallpaper-website-with-church-nature-4f9f88d9-7ce.png"
            />
          </div>
          <div className="overlap-3">
            <img
              className="waazup-cartoon-4"
              alt="Waazup cartoon"
              src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/6511c7272274091aaeadcb28/img/waazup-cartoon-wallpaper-website-with-chambord-castel-nature-0ad.png"
            />
          </div>
          <div className="overlap-4">
            <img
              className="waazup-cartoon-4"
              alt="Waazup cartoon"
              src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/6511c7272274091aaeadcb28/img/waazup-cartoon-wallpaper-website-with-french-monumentand-nature--1.png"
            />
          </div>
          <img
            className="chevron-droit"
            alt="Chevron droit"
            src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/6511c7272274091aaeadcb28/img/chevron-droit-1.png"
          />
          <img
            className="chevron-gauche"
            alt="Chevron gauche"
            src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/6511c7272274091aaeadcb28/img/chevron-gauche-1.png"
          />
        </div>
        <div className="france-wrapper">
          <img
            className="france"
            alt="France"
            src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/6511c7272274091aaeadcb28/img/france-2.png"
          />
        </div>
        <div className="text-wrapper-5" onClick={handleClick}>Carte</div>
        <div className="monument-removebg-wrapper" onClick={handleClick}>
          <img
            className="monument-removebg"
            alt="Monument removebg"
            src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/6511c7272274091aaeadcb28/img/monument-removebg-preview-1.png"
          />
        </div>
        <div className="text-wrapper-6" onClick={handleClick}>Monument</div>
        <div className="calendrier-wrapper" onClick={handleClick}>
          <img
            className="img-2"
            alt="Calendrier"
            src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/6511c7272274091aaeadcb28/img/calendrier-1.png"
          />
        </div>
        <div className="text-wrapper-7" onClick={handleClick}>Evenement</div>
        <div className="destination-wrapper" onClick={handleClick}>
          <img
            className="img-2"
            alt="Destination"
            src="https://cdn.animaapp.com/projects/6511c698c032644aea5b6c4d/releases/6511c7272274091aaeadcb28/img/destination-1.png"
          />
        </div>
        <div className="text-wrapper-8" onClick={handleClick}>Parcours</div>
        <div className="rectangle" />
        <div className="rectangle-2" />
      </div>
    </div>
  );
};
export default Accueil;
