/* Le code importe divers modules et composants à partir de fichiers et de bibliothèques externes. */
import React from "react";
import "../style/styleAccueil.css";
import banniereFestival from "../components/images/banniéreFestival.jpg";
import parcours from "../components/images/parcours.jpg"
import carte from "../components/images/carte.jpg"
import evenements from "../components/images/evenement.jpg"
import lieux from "../components/images/lieu.jpeg"

import { Link } from 'react-router-dom';
import ReactPlayer from 'react-player'


/**
 * La fonction Accueil renvoie un élément JSX qui représente la page d'accueil d'un site Web, affichant
 * une image de bannière, une vidéo et des liens vers différentes sections du site Web.
 * @returns Le composant Accueil renvoie un élément JSX, qui représente la structure et le contenu de
 * la sortie du composant.
 */
const Accueil = () => {
  return (
    <main>
      <div className="mt-5 container d-flex justify-content-center align-items-center">
        <img className="banniereFestival" src={banniereFestival}></img>
      </div>
      <div className="container text-center">
        <h2 className="Titre1 mt-5 d-flex justify-content-center align-items-center">“Découvrez le festival Ar(t]Chipel”</h2>
        <p className=" mt-2 presentationCVDL">“ Texte présentation Festival“</p>
        <div className="d-flex justify-content-center m-5">
          <ReactPlayer className='Youtube' url='https://youtu.be/7-rKv1aZk8s?si=fiLJ2M3T6yknLVLW' width='45vw'
            height='51.4vh' />
        </div>

      </div>
      <div className="container text-center">

        <h2 className="Titre1 mt-5 d-flex justify-content-center align-items-center">“Partez à la découverte du Centre Val de Loire”</h2>
        <p className=" mt-2 presentationCVDL">“ Bienvenue dans la magie du Centre-Val de Loire ! Explorez la vallée de la Loire avec ses châteaux emblématiques, plongez dans des vignobles d'exception, et découvrez des paysages naturels à couper le souffle. Notre site vous ouvre les portes d'une expérience unique, mêlant histoire, gastronomie, et charme à la française. Offrez-vous une escapade inoubliable au cœur de cette région captivante. Vivez la France authentique avec le Centre-Val de Loire ! “</p>
      </div>
      <div className="d-flex justify-content-center">
        <div className="d-flex flex-column align-items-center">
          <div className="m-3">
            <img className="ImageParcours" src={parcours} alt="Parcours" />
            <Link to={`/Parcours/`} className="TitreLieux d-flex justify-content-center align-items-center">Parcours</Link>
          </div>
          <div className="m-3">
            <img className="ImageLieux" src={lieux} alt="Lieux" />
            <Link to={`/lieux/`} className="TitreLieux d-flex justify-content-center align-items-center">Lieux</Link>
          </div>
        </div>
        <div className="d-flex flex-column align-items-center">
          <div className="m-3">
            <img className="ImageEvenements" src={evenements} alt="Evenements" />
            <p className="TitreEvenements d-flex justify-content-center align-items-center">Evenements</p>
          </div>
          <div className="m-3">
            <img className="ImageCarte" src={carte} alt="Carte" />
            <Link to={`/carte/`} className="TitreCarte d-flex justify-content-center align-items-center">Carte</Link>
          </div>



        </div>
      </div>

    </main>
  );
};

export default Accueil;
