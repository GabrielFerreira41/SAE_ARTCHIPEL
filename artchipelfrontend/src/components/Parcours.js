/* Le code importe divers modules et bibliothèques pour l'application React. */
import React, { useEffect, useState } from 'react';
import { useModal } from 'react-hooks-use-modal';
import { motion } from 'framer-motion';
import "../style/styleParcours.css";
import axios from "axios";
import { Link } from 'react-router-dom'; // Assurez-vous d'avoir React Router installé dans votre projet
import { loadModules } from 'esri-loader';






/**
 * La fonction `Parcours` est un composant React qui restitue une mosaïque d'éléments de parcours,
 * chacun avec un titre et une description, et permet à l'utilisateur de cliquer sur un élément pour
 * afficher plus de détails dans un modal.
 * @returns Le composant Parcours renvoie une structure JSX qui comprend un titre, un conteneur pour
 * une liste d'éléments de parcours et un composant modal qui affiche des informations supplémentaires
 * lorsqu'un utilisateur clique sur un élément de parcours.
 */
const Parcours = () => {
  const [parcours, setParcours] = useState([]);
  const [loadingParcours, setLoadingParcours] = useState(true);
  let view;


  useEffect(() => {

    const fetchData = async () => {
      try {
        const response = await axios.get("http://localhost:8000/api/parcours/");
        const parcoursList = response.data;

        const parcoursDetailsList = [];

        // Utilisation de Promise.all pour attendre que toutes les requêtes soient terminées
        await Promise.all(
          parcoursList.map(async (parcours) => {
            const detailsResponse = await axios.get(`http://localhost:8000/api/parcours/${parcours.idParcours}/`);
            const parcoursDetails = detailsResponse.data;
            parcoursDetails.parcours.etapes.forEach((lieu) => {
              lieu.location = [lieu.lieu.longitudeLieu, lieu.lieu.latitudeLieu];
            });
            parcoursDetailsList.push(parcoursDetails.parcours);
          })
        );

        setParcours(parcoursDetailsList);
        setLoadingParcours(false);
      } catch (error) {
        console.error("Erreur lors de la récupération des parcours :", error);
      }
    };

    fetchData();
  }, []);


  console.log(parcours)
  const fadeInUp = {
    initial: { opacity: 0, y: 20 },
    animate: { opacity: 1, y: 0 },
  };

  const maxSize = 30;
  const itemsPerRow = 4;

  const getRandomColor = () => {
    const startColor = [0, 159, 227];
    const endColor = [18, 170, 54];
    const randomColor = startColor.map((start, index) => {
      const end = endColor[index];
      return Math.floor(Math.random() * (end - start + 1)) + start;
    });
    return `rgb(${randomColor.join(', ')})`;
  };

  const calculateSize = () => {
    const totalItems = parcours.length;
    const rows = Math.ceil(totalItems / itemsPerRow);
    const width = Math.floor(window.innerWidth / itemsPerRow);
    const height = Math.floor(window.innerHeight / rows);

    return {
      width: Math.min(width, maxSize),
      height: Math.min(height, maxSize),
    };
  };

  const [selectedParcours, setSelectedParcours] = useState(null);

  const [Modal, open, close] = useModal('root', {
    preventScroll: true,
    closeOnOverlayClick: false
  });

  const handleParcoursClick = (parcours) => {

    loadModules([
      'esri/Map',
      'esri/views/MapView',
      'esri/layers/GraphicsLayer',
      'esri/Graphic',
      'esri/widgets/Directions',
      'esri/widgets/Search',
      'esri/widgets/Popup',
    ], { css: true })
      .then(([Map, MapView, GraphicsLayer, Graphic, Directions, Search]) => {
        const map = new Map({
          basemap: 'streets-navigation-vector'
        });


        view = new MapView({
          container: 'map-view',
          map: map,
          center: [1.32, 47.75],
          zoom: 8,
        });
        const monumentsLayer = new GraphicsLayer();

        map.add(monumentsLayer);
      });
  setSelectedParcours(parcours);
  open();
};



return (
  <div>
    <div className=' divContainer d-flex justify-content-center align-items-center'>
      <div className='ContainerTitreParcoursVert d-flex justify-content-center align-items-center'>
        <h1 className='titreMosaiquee2e d-flex titreParcours justify-content-center'>"Parcours Mosaïque"</h1>
      </div>
    </div>
    <motion.ul
      className="parcours-list list-unstyled"
      style={{
        display: 'grid',
        gridTemplateColumns: `repeat(${itemsPerRow}, 1fr)`,
        gap: '0',
        margin: '0',
        padding: '0',
      }}
    >
      {parcours.map((parcour) => (
        <motion.li
          key={parcour.idParcours}
          className="parcours-item d-flex justify-content-center align-items-center"
          variants={fadeInUp}
          onClick={() => handleParcoursClick(parcour)}
          whileHover={{ scale: 1.1 }}
          style={{
            width: `${calculateSize().width}rem`,
            height: `${calculateSize().height}rem`,
            backgroundColor: getRandomColor(),
            margin: '0',
          }}
        >
          <div className='text-center'>
            <h3 style={{ fontSize: '90%', margin: '0' }}>{parcour.nomParcours}</h3>
            <p style={{ fontSize: '80%', margin: '0' }}>description à faire </p>
          </div>
        </motion.li>
      ))}
    </motion.ul>
    {/* /* Le composant `<Modal>` est un composant personnalisé utilisé pour afficher une fenêtre modale
      ou contextuelle dans l'application. Il enveloppe le contenu qui doit être affiché dans le
      modal et fournit des fonctionnalités pour ouvrir et fermer le modal. */}
    <Modal>
      <div className='popUp d-flex'>
        <div className='titrePopUpParcours d-flex justify-content-center' >
          <div className='titleDiv'>
            <h1 className='d-flex justify-content-center LilitaOneGreen mb-5'>{selectedParcours?.nomParcours}</h1>
            <div>
            <div className='ListeLieuxPopUpParcours d-flex justify-content-center align-items-center'>
            {selectedParcours && (
              <ul className="lieux-list list-unstyled lieuContainerCheminParcours">
                {selectedParcours.etapes.map((lieu, index) => (
                  /* Le code `<React.Fragment>` est utilisé comme wrapper pour regrouper plusieurs
                  éléments sans ajouter d'élément DOM supplémentaire. Il vous permet de renvoyer
                  plusieurs éléments de la méthode de rendu d'un composant sans avoir à les
                  envelopper dans un seul élément parent. */
                  <React.Fragment key={lieu.lieu.idLieu}>
                    <div className='d-flex justify-content-center'>
                      <div>
                        {index > 0 && <p className='cheminParcours'> • </p>}
                        {index > 0 && <p className='cheminParcours'> • </p>}
                        {index > 0 && <p className='cheminParcours mb-3'> • </p>}
                      </div>
                    </div>
                    <div className='d-flex justify-content-center'>

                      <li className='listeLieuxParcours d-flex justify-content-center'>
                        <Link className='LilitaOneWhite p-2' to={`/lieux/${lieu.lieu.idLieu}`}>{lieu.lieu.nomLieu}</Link>
                      </li>

                    </div>

                  </React.Fragment>
                ))}
              </ul>
            )}
          </div>
            </div>
          </div>

        </div>
        <div className='ContainerListeLieuxPopUpParcours'>
          <div className='d-flex justify-content-end'>
            <button className='buttonClosePopUp' onClick={close}>X</button>
          </div>
          <div className='d-flex justify-content-center align-items-center containerCarteParcours'>
          <div id="map-view" style={{ height: '40vh', width: '38vw' }}></div>

          </div>
        </div>

      </div>
    </Modal>
  </div>
);
};

export default Parcours;

