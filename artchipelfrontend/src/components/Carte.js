/* Le code importe les modules et styles nécessaires pour le composant `Carte`. */
import React, { useEffect, useState } from 'react';
import { loadModules, IdentityManager } from 'esri-loader';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';
import '../style/styleCarte.css';
import loupe from './images/loupeBlanc.png';
import axios from "axios";



/**
 * La fonction « Carte » est un composant React qui affiche une carte avec des marqueurs pour divers
 * lieux, permet aux utilisateurs de rechercher des lieux spécifiques et fournit une liste de
 * lieu avec pagination.
 * @returns Le composant `Carte` renvoie un élément JSX, qui représente la structure et le contenu de
 * la sortie rendue du composant.
 */
const Carte = () => {
  /* Ces lignes de code utilisent le hook `useState` pour créer et initialiser des variables d'état
  dans un composant fonctionnel. */
  const [selectedMonument, setSelectedMonument] = useState(null);
  const [parcoursList, setParcoursList] = useState([]); // Nouvelle variable d'état pour la liste des parcours
  const [monumentsList, setMonumentsList] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [selectedMap, viewMonumentOnMap] = useState(null);
  const [searchTerm, setSearchTerm] = useState('');
  const [showInfoPanel, setShowInfoPanel] = useState(false);
  const [showParcoursTab, setShowParcoursTab] = useState(false); // Nouvelle variable d'état pour basculer entre les onglets
  const itemsPerPage = 6;
  const [lieux, setLieux] = useState([]);
  const [parcours, setParcours] = useState([]);
  const [loadingLieux, setLoadingLieux] = useState(true);
  const [loadingParcours, setLoadingParcours] = useState(true);




  let view;
useEffect(() => {
  const fetchData = async () => {
    try {
      const [lieuxResponse, parcoursResponse] = await Promise.all([
        axios.get("http://localhost:8000/api/lieu/"),
        axios.get("http://localhost:8000/api/parcours/")
      ]);

      // Traitement des lieux
      const lieuxData = lieuxResponse.data;
      setLieux(lieuxData);
      setLoadingLieux(false);

      // Traitement des parcours
      const parcoursList = parcoursResponse.data;
      const parcoursDetailsList = await Promise.all(
        parcoursList.map(async (parcours) => {
          const detailsResponse = await axios.get(`http://localhost:8000/api/parcours/${parcours.idParcours}/`);
          const parcoursDetails = detailsResponse.data;
          parcoursDetails.parcours.etapes.forEach((lieu) => {
            lieu.location = [lieu.lieu.longitudeLieu, lieu.lieu.latitudeLieu];
          });
          return parcoursDetails.parcours;
        })
      );

      setParcours(parcoursDetailsList);
      setLoadingParcours(false);
    } catch (error) {
      console.error("Erreur lors de la récupération des données :", error);
    }
  };

  fetchData();
}, []);

  /* Le code ci-dessus est écrit en JavaScript et utilise le hook useEffect de React. Il charge
  plusieurs modules de l'API ArcGIS pour JavaScript, notamment Map, MapView, GraphicsLayer, Graphic,
  Directions, Search et Popup. */
  useEffect(() => {
  //   loadModules([
  //     'esri/Map',
  //     'esri/views/MapView',
  //     'esri/layers/GraphicsLayer',
  //     'esri/Graphic',
  //     'esri/widgets/Directions',
  //     'esri/widgets/Search',
  //     'esri/widgets/Popup',
  //   ], { css: true })
  //     .then(([Map, MapView, GraphicsLayer, Graphic, Directions, Search]) => {
  //       const map = new Map({
  //         basemap: 'streets-navigation-vector'
  //       });


  //       view = new MapView({
  //         container: 'map-view',
  //         map: map,
  //         center: [1.32, 47.75],
  //         zoom: 8,
  //       });
  //       const monumentsLayer = new GraphicsLayer();

  //       map.add(monumentsLayer);
      
  //       if (!loadingLieux && !loadingParcours) {
  //       /* Le bloc de code parcourt un ensemble de monuments et crée des graphiques pour chaque
  //       monument sur la carte. */
  //       lieux.forEach(monument => {
  //       if (monument.latitudeLieu !== null && monument.longitudeLieu !== null) {
  //         const point = {
  //           type: 'point',
  //           longitude: monument.longitudeLieu.toString(),
  //           latitude: monument.latitudeLieu.toString(),
  //         };

  //         const markerSymbol = {
  //           type: 'simple-marker',
  //           color: [18, 170, 54],
  //           outline: {
  //             color: [255, 255, 255],
  //             width: 2,
  //           },
  //         };

  //         const pointGraphic = new Graphic({
  //           geometry: point,
  //           symbol: markerSymbol,
  //           attributes: {
  //             name: monument.nomLieu,
  //             id: monument.idLieu,
  //           },
  //         });

  //         const popupTemplate = {
  //           title: '{name}',
  //           content: `<a href="/lieux/${monument.idLieu}">Voir le détail de '${monument.nomLieu}'</a>`,
  //         };

  //         pointGraphic.popupTemplate = popupTemplate;

  //         monumentsLayer.add(pointGraphic);
  //       }});


  //       /* Le code ci-dessous parcourt un tableau appelé "parcours" et crée un graphique polyligne pour
  //       chaque élément du tableau. Chaque polyligne représente un chemin avec plusieurs Lieu.
  //       Le code définit la couleur et la largeur de la polyligne, ainsi qu'un modèle contextuel qui
  //       sera affiché lorsque vous cliquerez sur la polyligne. Enfin, le graphique polyligne est
  //       ajouté à un calque appelé « monumentsLayer ». */
  //       parcours.forEach(parcour => {
  //         const validEtapes = parcour.etapes
  //           .filter(lieu => lieu.lieu.latitudeLieu !== null && lieu.lieu.longitudeLieu !== null);

  //         if (validEtapes.length > 1) {
  //           // Créez la polyligne uniquement s'il y a au moins deux étapes avec des coordonnées valides.
  //           const path = {
  //             type: 'polyline',
  //             paths: [validEtapes.map(waypoint => waypoint.location)],
  //           };
        
  //           const lineSymbol = {
  //             type: 'simple-line',
  //             color: [0, 159, 227],

  //             width: 2,
  //           };
        
  //           const pathGraphic = new Graphic({
  //             geometry: path,
  //             symbol: lineSymbol,
  //             attributes: {
  //               name: parcour.nomParcours,
  //               id: parcour.idParcours,
  //             },
  //           });
        
  //           const popupTemplate = {
  //             title: '{name}',
  //             content: `<p>Ce parcours inclut plusieurs lieux. <a href="/parcours/${parcour.idParcours}">Voir les détails du parcours</a></p>`,
  //           };
        
  //           pathGraphic.popupTemplate = popupTemplate;
        
  //           monumentsLayer.add(pathGraphic);
  //           console.log('Polyline added for parcours:', parcour);
  //         } else {
  //           console.log('Skipping parcours with insufficient valid etapes:', parcour);
  //         }
  //       });
        
  //     }




  //       /* Ce code ajoute un écouteur d'événement de clic à la couche graphique `monumentsLayer`.
  //       Lorsqu'un utilisateur clique sur un monument sur la carte, les attributs du monument
  //       sélectionné sont définis à l'aide de `setSelectedMonument(event.graphic.attributes)`. La vue
  //       se déplace ensuite vers l'emplacement du monument cliqué en utilisant `view.goTo()` avec une
  //       cible de la géométrie du monument cliqué et un niveau de zoom de 12. Enfin, le tableau
  //       `monuments` est défini comme variable d'état `monumentsList` en utilisant `
  //       setMonumentsList(monuments)`. */
  //       monumentsLayer.on('click', event => {
  //         setSelectedMonument(event.graphic.attributes);
  //         view.goTo({
  //           target: event.graphic.geometry,
  //           zoom: 12,
  //         });
  //       });

        setMonumentsList(lieux);
        setParcoursList(parcours);
      

  //       const viewMonumentOnMap = (location) => {
  //         if (view) {
  //           view.goTo({
  //             center: location,
  //             zoom: 12,
  //           });
  //         } else {
  //           console.error("View is undefined.");
  //         }
  //       };

  //       const directionsWidget = new Directions({
  //         view: view,
  //       });

  //       view.ui.add(directionsWidget, 'top-right');

  //       const searchWidget = new Search({
  //         view: view,
  //         resultGraphicEnabled: false,
  //         popupEnabled: false,
  //       });

  //       view.ui.add(searchWidget, 'top-left');

  //       return () => {
  //         if (view) {
  //           view.destroy();
  //         }
  //       };
  //     })
  //     .catch(err => console.error(err));
  }, [selectedMap,loadingLieux,loadingParcours]);

  const handleSearch = (term) => {
    setSearchTerm(term);
  };

  const handleMarkerClick = (monument) => {
    setSelectedMonument(monument);
    setShowInfoPanel(true);
  };

  const handleParcoursTabClick = () => {
    setShowParcoursTab(true);
  };

  const handleMonumentsTabClick = () => {
    setShowParcoursTab(false);
  };

  const changePage = (page) => {
    setCurrentPage(page);
  };

  const startIndex = (currentPage - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;
  const currentList = showParcoursTab ? parcoursList : monumentsList;

  const currentItems = currentList
  .filter((item) => {
    const itemName = item.nomLieu || item.nomParcours;
    return itemName.toLowerCase().includes(searchTerm.toLowerCase());
  })
  .slice(startIndex, endIndex);

  return (
    <div className='mainCarte'>
      <div className=' divContainerCarte d-flex justify-content-center align-items-center'>
        <div className='ContainerCarteVert d-flex justify-content-center align-items-center'>
          <h1 className='titreCartee2e d-flex titreCarte justify-content-center'>"Carte"</h1>
        </div>
      </div>
      <div className='d-flex justify-content-center fondVertLieux'>
      <iframe src="https://www.google.com/maps/d/embed?mid=19t-HwS5eC2JgzhoILFAM1B12Y8OY0xQ&ehbc=2E312F" width="1500" height="900"></iframe>
      </div>
      <section className=''>
        <div className='d-flex justify-content-center containerTitreLieu'>
          <h1 onClick={handleMonumentsTabClick} className='titreCarteListeLieux mt-5 d-flex justify-content-center align-items-center'>" Voir liste des lieux"</h1>
          <h1 onClick={handleParcoursTabClick} className='titreCarteListeParcours mt-5 d-flex justify-content-center align-items-center'>"Voir liste des parcours"</h1>
        </div>
        {/* Barre de Recherche */}
        <div className="d-flex searchBarDiv justify-content-center align-items-center">
          <div className={`${showParcoursTab ? 'divImageLoupeBleu' : 'divImageLoupeVert'}`}>
            <img className='ImageLoupe' src={loupe} alt="Loupe" />
          </div>
          <input
            className='searchBar'
            type="text"
            placeholder={showParcoursTab ? "Rechercher un parcours..." : "Rechercher un lieux..."}
            value={searchTerm}
            onChange={(e) => handleSearch(e.target.value)}
          />
        </div>
        {/* Liste des Monuments ou Parcours en fonction de l'onglet actif */}
        <div className='d-flex justify-content-center'>

        <div className="row containerListeLieuxParcours">
            {currentItems.map((item, index) => (
              <div key={index} className="col-md-6 mb-4 ">
                <div className={` ${showParcoursTab ? 'carteListeParcoursBleu' : 'carteListeLieuxVert'}`}>
                  <div className="card-body text-center">
                    <h5 className="card-title titleMonument">{showParcoursTab ? `${item.nomParcours}` : `${item.nomLieu}`}</h5>
                    <div>
                      <a href={showParcoursTab ? `/parcours/${item.idParcours}` : `/lieux/${item.idLieu}`}>
                        Détails
                      </a>
                      <a onClick={() => viewMonumentOnMap(item.location)}>Voir sur la carte</a>
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
        {/* Contrôles de Pagination */}
        <nav aria-label="Page navigation example">
          <ul className={`pagination justify-content-center`}>
            {Array.from({ length: Math.ceil(currentList.length / itemsPerPage) }, (_, index) => (
              <li key={index} className={`page-item ${currentPage === index + 1 ? 'active' : ''}`}>
                <a
                  className="page-link"
                  onClick={() => changePage(index + 1)}
                  style={{ cursor: 'pointer' }}
                >
                  {index + 1}
                </a>
              </li>
            ))}
          </ul>
        </nav>
      </section>
    </div>
  );
};

export default Carte;


