/* Le code importe divers modules et bibliothèques pour l'application React. */
import React, { useState } from 'react';
import { useModal } from 'react-hooks-use-modal';
import { motion } from 'framer-motion';
import "../style/styleParcours.css";


const parcoursList = [
  { id: 1, title: 'Parcours A', description: 'Description du parcours A', lieux: [{ id: 1, nom: 'Lieu 1A' }, { id: 2, nom: 'Lieu 2A' }, { id: 3, nom: 'Lieu 3A' }, { id: 4, nom: 'Lieu 4A' }, { id: 5, nom: 'Lieu 5A' }, { id: 6, nom: 'Lieu 6A' }, { id: 7, nom: 'Lieu 7A' }, { id: 8, nom: 'Lieu 8A' }, { id: 9, nom: 'Lieu 9A' }, { id: 10, nom: 'Lieu 10A' }] },
  { id: 2, title: 'Parcours B', description: 'Description du parcours B', lieux: [{ id: 4, nom: 'Lieu 4B' }, { id: 5, nom: 'Lieu 5B' }] },
  { id: 3, title: 'Parcours C', description: 'Description du parcours C', lieux: [{ id: 6, nom: 'Lieu 6C' }, { id: 7, nom: 'Lieu 7C' }, { id: 8, nom: 'Lieu 8C' }] },
  { id: 4, title: 'Parcours D', description: 'Description du parcours D', lieux: [{ id: 9, nom: 'Lieu 9D' }, { id: 10, nom: 'Lieu 10D' }] },
  { id: 5, title: 'Parcours E', description: 'Description du parcours E', lieux: [{ id: 11, nom: 'Lieu 11E' }, { id: 12, nom: 'Lieu 12E' }, { id: 13, nom: 'Lieu 13E' }] },
  { id: 6, title: 'Parcours F', description: 'Description du parcours F', lieux: [{ id: 14, nom: 'Lieu 14F' }, { id: 15, nom: 'Lieu 15F' }] },
  { id: 7, title: 'Parcours G', description: 'Description du parcours G', lieux: [{ id: 16, nom: 'Lieu 16G' }, { id: 17, nom: 'Lieu 17G' }, { id: 18, nom: 'Lieu 18G' }] },
  { id: 8, title: 'Parcours H', description: 'Description du parcours H', lieux: [{ id: 19, nom: 'Lieu 19H' }, { id: 20, nom: 'Lieu 20H' }] },
  { id: 9, title: 'Parcours I', description: 'Description du parcours I', lieux: [{ id: 21, nom: 'Lieu 21I' }, { id: 22, nom: 'Lieu 22I' }, { id: 23, nom: 'Lieu 23I' }] },
  { id: 10, title: 'Parcours J', description: 'Description du parcours J', lieux: [{ id: 24, nom: 'Lieu 24J' }, { id: 25, nom: 'Lieu 25J' }] },
  { id: 11, title: 'Parcours K', description: 'Description du parcours K', lieux: [{ id: 26, nom: 'Lieu 26K' }, { id: 27, nom: 'Lieu 27K' }, { id: 28, nom: 'Lieu 28K' }] },
  { id: 12, title: 'Parcours L', description: 'Description du parcours L', lieux: [{ id: 29, nom: 'Lieu 29L' }, { id: 30, nom: 'Lieu 30L' }] },
  { id: 13, title: 'Parcours M', description: 'Description du parcours M', lieux: [{ id: 31, nom: 'Lieu 31M' }, { id: 32, nom: 'Lieu 32M' }, { id: 33, nom: 'Lieu 33M' }] },
  { id: 14, title: 'Parcours N', description: 'Description du parcours N', lieux: [{ id: 34, nom: 'Lieu 34N' }, { id: 35, nom: 'Lieu 35N' }] },
  { id: 15, title: 'Parcours O', description: 'Description du parcours O', lieux: [{ id: 36, nom: 'Lieu 36O' }, { id: 37, nom: 'Lieu 37O' }, { id: 38, nom: 'Lieu 38O' }] },
  { id: 16, title: 'Parcours P', description: 'Description du parcours P', lieux: [{ id: 39, nom: 'Lieu 39P' }, { id: 40, nom: 'Lieu 40P' }] },
  { id: 17, title: 'Parcours Q', description: 'Description du parcours Q', lieux: [{ id: 41, nom: 'Lieu 41Q' }, { id: 42, nom: 'Lieu 42Q' }, { id: 43, nom: 'Lieu 43Q' }] },
  { id: 18, title: 'Parcours R', description: 'Description du parcours R', lieux: [{ id: 44, nom: 'Lieu 44R' }, { id: 45, nom: 'Lieu 45R' }] },
  { id: 19, title: 'Parcours S', description: 'Description du parcours S', lieux: [{ id: 46, nom: 'Lieu 46S' }, { id: 47, nom: 'Lieu 47S' }, { id: 48, nom: 'Lieu 48S' }] },
  { id: 20, title: 'Parcours T', description: 'Description du parcours T', lieux: [{ id: 49, nom: 'Lieu 49T' }, { id: 50, nom: 'Lieu 50T' }] },
  { id: 21, title: 'Parcours U', description: 'Description du parcours U', lieux: [{ id: 51, nom: 'Lieu 51U' }, { id: 52, nom: 'Lieu 52U' }, { id: 53, nom: 'Lieu 53U' }] },
  { id: 22, title: 'Parcours V', description: 'Description du parcours V', lieux: [{ id: 54, nom: 'Lieu 54V' }, { id: 55, nom: 'Lieu 55V' }] },
  { id: 23, title: 'Parcours W', description: 'Description du parcours W', lieux: [{ id: 56, nom: 'Lieu 56W' }, { id: 57, nom: 'Lieu 57W' }, { id: 58, nom: 'Lieu 58W' }] },
  { id: 24, title: 'Parcours X', description: 'Description du parcours X', lieux: [{ id: 59, nom: 'Lieu 59X' }, { id: 60, nom: 'Lieu 60X' }] },
  { id: 25, title: 'Parcours Y', description: 'Description du parcours Y', lieux: [{ id: 61, nom: 'Lieu 61Y' }, { id: 62, nom: 'Lieu 62Y' }, { id: 63, nom: 'Lieu 63Y' }] },
  { id: 26, title: 'Parcours Z', description: 'Description du parcours Z', lieux: [{ id: 64, nom: 'Lieu 64Z' }, { id: 65, nom: 'Lieu 65Z' }] },
  { id: 27, title: 'Parcours AA', description: 'Description du parcours AA', lieux: [{ id: 66, nom: 'Lieu 66AA' }, { id: 67, nom: 'Lieu 67AA' }, { id: 68, nom: 'Lieu 68AA' }] },
  { id: 28, title: 'Parcours BB', description: 'Description du parcours BB', lieux: [{ id: 69, nom: 'Lieu 69BB' }, { id: 70, nom: 'Lieu 70BB' }] },
  { id: 29, title: 'Parcours CC', description: 'Description du parcours CC', lieux: [{ id: 71, nom: 'Lieu 71CC' }, { id: 72, nom: 'Lieu 72CC' }, { id: 73, nom: 'Lieu 73CC' }] },
  { id: 30, title: 'Parcours DD', description: 'Description du parcours DD', lieux: [{ id: 74, nom: 'Lieu 74DD' }, { id: 75, nom: 'Lieu 75DD' }] },
];


/**
 * La fonction `Parcours` est un composant React qui restitue une mosaïque d'éléments de parcours,
 * chacun avec un titre et une description, et permet à l'utilisateur de cliquer sur un élément pour
 * afficher plus de détails dans un modal.
 * @returns Le composant Parcours renvoie une structure JSX qui comprend un titre, un conteneur pour
 * une liste d'éléments de parcours et un composant modal qui affiche des informations supplémentaires
 * lorsqu'un utilisateur clique sur un élément de parcours.
 */
const Parcours = () => {
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
    const totalItems = parcoursList.length;
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
        {parcoursList.map((parcours) => (
          <motion.li
            key={parcours.id}
            className="parcours-item d-flex justify-content-center align-items-center"
            variants={fadeInUp}
            onClick={() => handleParcoursClick(parcours)}
            whileHover={{ scale: 1.1 }}
            style={{
              width: `${calculateSize().width}rem`,
              height: `${calculateSize().height}rem`,
              backgroundColor: getRandomColor(),
              margin: '0',
            }}
          >
            <div className='text-center'>
              <h3 style={{ fontSize: '90%', margin: '0' }}>{parcours.title}</h3>
              <p style={{ fontSize: '80%', margin: '0' }}>{parcours.description}</p>
            </div>
          </motion.li>
        ))}
      </motion.ul>
      {/* /* Le composant `<Modal>` est un composant personnalisé utilisé pour afficher une fenêtre modale
      ou contextuelle dans l'application. Il enveloppe le contenu qui doit être affiché dans le
      modal et fournit des fonctionnalités pour ouvrir et fermer le modal. */}
      <Modal>
        <div className='popUp d-flex'>
          <div className='titrePopUpParcours d-flex justify-content-center align-items-center' >
            <div className='titleDiv'>
              <h1 className='d-flex justify-content-center LilitaOneGreen'>{selectedParcours?.title}</h1>
              <div className='d-flex justify-content-center'>
                <button className=''>Voir sur la Carte</button>
              </div>
            </div>

          </div>
          <div className='ContainerListeLieuxPopUpParcours'>
            <div className='d-flex justify-content-end'>
              <button className='buttonClosePopUp' onClick={close}>X</button>
            </div>
            <div className='ListeLieuxPopUpParcours d-flex justify-content-center align-items-center'>
              {selectedParcours && (
                <ul className="lieux-list list-unstyled lieuContainerCheminParcours">
                  {selectedParcours.lieux.map((lieu, index) => (
                    /* Le code `<React.Fragment>` est utilisé comme wrapper pour regrouper plusieurs
                    éléments sans ajouter d'élément DOM supplémentaire. Il vous permet de renvoyer
                    plusieurs éléments de la méthode de rendu d'un composant sans avoir à les
                    envelopper dans un seul élément parent. */
                    <React.Fragment key={lieu.id}>
                      <div className='d-flex justify-content-center'>
                        <div>
                          {index > 0 && <p className='cheminParcours'> • </p>}
                          {index > 0 && <p className='cheminParcours'> • </p>}
                          {index > 0 && <p className='cheminParcours mb-3'> • </p>}
                        </div>
                      </div>
                      <div className='d-flex justify-content-center'>

                        <li className='LilitaOneWhite listeLieuxParcours d-flex justify-content-center'>
                          {lieu.nom}
                        </li>
                      </div>

                    </React.Fragment>
                  ))}
                </ul>
              )}
            </div>
          </div>

        </div>
      </Modal>
    </div>
  );
};

export default Parcours;

