/* Le code importe divers modules et composants à partir de fichiers et de bibliothèques externes. */
import React, { useState, useEffect, useMemo } from "react";
import axios from "axios";
import "../style/styleAccueil.css";
import banniereFestival from "../components/images/banniéreFestival.jpg";
import parcours from "../components/images/parcours.jpg"
import carte from "../components/images/carte.jpg"
import evenements from "../components/images/evenement.jpg"
import lieuxImage from "../components/images/lieu.jpeg"

import { Link } from 'react-router-dom';
import ReactPlayer from 'react-player';
import { useNavigate } from "react-router-dom";


/**
 * La fonction Accueil renvoie un élément JSX qui représente la page d'accueil d'un site Web, affichant
 * une image de bannière, une vidéo et des liens vers différentes sections du site Web.
 * @returns Le composant Accueil renvoie un élément JSX, qui représente la structure et le contenu de
 * la sortie du composant.
 */
const Accueil = () => {
  const [lieux, setLieux] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    // Récupérer la liste complète des lieux
    axios.get("http://localhost:8000/api/lieu/")
      .then((response) => {
        const data = response.data;
        setLieux(data);
      })
      .catch((error) => {
        console.error("Erreur lors de la récupération des lieux :", error);
      });
  }, []);

  // Sélectionner 4 lieux aléatoires à afficher
  const randomLieux = useMemo(() => {
    if (lieux.length === 0) {
      return [];
    }

    const shuffledLieux = [...lieux].sort(() => 0.5 - Math.random());
    return shuffledLieux.slice(0, 3);
  }, [lieux]);
  return (
    <div className="mainAccueil">
      <div className="mt-5 container d-flex justify-content-center align-items-center">
        <img className="banniereFestival " src={banniereFestival}></img>
      </div>
      <div className="container text-center">
        <h2 className="Titre1 mt-5 d-flex justify-content-center align-items-center">“Découvrez le festival Ar(t]Chipel”</h2>
        <p className=" mt-2 presentationCVDL">Découvrez le Festival Artchipel, une célébration annuelle captivante de l'art et de la culture, mettant en vedette des expositions artistiques, des performances envoûtantes, des ateliers interactifs et des espaces immersifs. Rejoignez notre communauté créative lors de notre prochain événement pour explorer la diversité artistique, participer à des ateliers inspirants et créer des souvenirs uniques. Suivez-nous pour les dernières actualités et réservez vos billets pour cette expérience artistique inoubliable !</p>
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
            <Link to={`/Parcours/`} className="d-flex flex-column align-items-center">
              <img className="ImageParcours" src={parcours} alt="Parcours" />
              <div className="e2eTestParcours TitreLieux d-flex justify-content-center align-items-center">Parcours</div>
            </Link>
          </div>
          <div className="m-3">
            <Link to={`/lieux/`} className="d-flex flex-column align-items-center">
              <img className="ImageLieux" src={lieuxImage} alt="Lieux" />
              <div className="e2eTestLieux TitreLieux d-flex justify-content-center align-items-center">Lieux</div>
            </Link>
          </div>

        </div>
        <div className="d-flex flex-column align-items-center">
          <Link to={`/evenements/`} className="m-3 d-flex flex-column align-items-center">
            <img className="ImageEvenements" src={evenements} alt="Evenements" />
            <p className="TitreEvenements d-flex justify-content-center align-items-center">Evenements</p>
          </Link>

          <div className="m-3">
            <Link to={`/carte/`} className="d-flex flex-column align-items-center">
              <img className="ImageCarte" src={carte} alt="Carte" />
              <div className="e2eTestCarte TitreCarte d-flex justify-content-center align-items-center">Carte</div>
            </Link>
          </div>
        </div>
      </div>
      <div className="accueilSugestionLieuVert">
        <div className="d-flex justify-content-center">
          <h1 className="titreLilitaOneBlanc mt-5">Suggestion visite</h1>
        </div>
        <div className="d-flex justify-content-center">
          {randomLieux.map((lieu) => (
            <div className="m-3 p-2">
              <Link to={`/lieux/${lieu.idLieu}`} className="d-flex flex-column align-items-center">
                {lieu.imageLieu ? (
                  <img className="ImageLieuAleatoire justify-content-center" src={process.env.PUBLIC_URL + `/${lieu.imageLieu}`} alt="Image Lieu suggestion" />
                ) : (
                  <img className="ImageLieuAleatoire justify-content-center" src={process.env.PUBLIC_URL + `/images/artchipelDefault.png`} alt="Image Lieu sugestion" />
                )}
                <div className="row d-flex justify-content-center mt-3 titreLilitaOneBlancPetit text-white">{lieu.nomLieu}</div>
              </Link>
            </div>

          ))}
        </div>
      </div>
    </div>
  );
};

export default Accueil;
