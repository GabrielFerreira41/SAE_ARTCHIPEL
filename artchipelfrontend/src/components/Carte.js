/* Le code importe les modules et styles nécessaires pour le composant `Carte`. */
import React, { useEffect, useState } from 'react';
import { loadModules, IdentityManager } from 'esri-loader';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';
import '../style/styleCarte.css';
import loupe from './images/loupeBlanc.png';


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

  let view;

  /* Le code ci-dessus est écrit en JavaScript et utilise le hook useEffect de React. Il charge
  plusieurs modules de l'API ArcGIS pour JavaScript, notamment Map, MapView, GraphicsLayer, Graphic,
  Directions, Search et Popup. */
  useEffect(() => {
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
          basemap: 'streets-navigation-vector',
          authentication: {
            username: 'Gabi41',
            password: '@Iut12345',
          },
        });


        view = new MapView({
          container: 'map-view',
          map: map,
          center: [1.32, 47.75],
          zoom: 8,
        });
        const monumentsLayer = new GraphicsLayer();

        map.add(monumentsLayer);

        const monuments = [
          { id: 1, name: 'Château de Chambord', location: [1.515, 47.616] },
          { id: 2, name: 'Cathédrale de Chartres', location: [1.485, 48.447] },
          { id: 3, name: 'Château de Chenonceau', location: [1.0707, 47.3244] },
          { id: 4, name: 'Château d\'Amboise', location: [0.9845, 47.4108] },
          { id: 5, name: 'Château de Villandry', location: [0.5110, 47.3423] },
          { id: 6, name: 'Château d\'Azay-le-Rideau', location: [0.4725, 47.2613] },
          { id: 7, name: 'Château de Blois', location: [1.3307, 47.5861] },
          { id: 8, name: 'Château de Cheverny', location: [1.4552, 47.5077] },
          { id: 9, name: 'Château de Loches', location: [1.0041, 47.1284] },
          { id: 10, name: 'Château de Chinon', location: [0.2454, 47.1676] },
          { id: 11, name: 'Château de Montpoupon', location: [0.9833, 47.2167] },
          { id: 12, name: 'Château de Chaumont-sur-Loire', location: [0.9760, 47.4826] },
          { id: 13, name: 'Château de Valençay', location: [1.5736, 47.1624] },
          { id: 14, name: 'Château de Langeais', location: [0.4045, 47.3307] },
          { id: 15, name: 'Château de Sully-sur-Loire', location: [2.3832, 47.7803] },
          { id: 16, name: 'Château de Gien', location: [2.6340, 47.6876] },
          { id: 17, name: 'Château de Meung-sur-Loire', location: [1.6947, 47.8202] },
          { id: 18, name: 'Château de La Ferté-Saint-Aubin', location: [1.9583, 47.8151] },
          { id: 19, name: 'Château de Saumur', location: [-0.2458, 47.2623] },
          { id: 20, name: 'Château de Brissac', location: [-0.5520, 47.3590] },
        ];

        const parcours = [
          {
            id: 21,
            name: 'Parcours des Châteaux Royaux',
            listeLieu: [
              { monumentId: 1, location: [1.515, 47.616] }, // Château de Chambord
              { monumentId: 2, location: [1.485, 48.447] }, // Cathédrale de Chartres
              { monumentId: 2, location: [1.0707, 47.3244] },
              { monumentId: 2, location: [0.9845, 47.4108] },
              { monumentId: 2, location: [0.5110, 47.3423] },
            ],
          },
          {
            id: 22,
            name: 'Parcours de la Vallée des Rois',
            listeLieu: [
              { monumentId: 3, location: [1.0707, 47.3244] }, // Château de Chenonceau
              { monumentId: 4, location: [0.9845, 47.4108] }, // Château d'Amboise
              { monumentId: 5, location: [0.5110, 47.3423] }, // Château de Villandry
              // ... (ajoutez d'autres lieux au besoin)
            ],
          },
          {
            id: 23,
            name: 'Parcours des Cités Médiévales',
            listeLieu: [
              { monumentId: 9, location: [1.0041, 47.1284] }, // Château de Loches
              { monumentId: 10, location: [0.2454, 47.1676] }, // Château de Chinon
              { monumentId: 11, location: [0.9833, 47.2167] }, // Château de Montpoupon
              // ... (ajoutez d'autres lieux au besoin)
            ],
          },
          {
            id: 24,
            name: 'Parcours des Abbayes Historiques',
            listeLieu: [
              { monumentId: 7, location: [1.3307, 47.5861] }, // Château de Blois
              { monumentId: 13, location: [1.5736, 47.1624] }, // Château de Valençay
              { monumentId: 14, location: [0.4045, 47.3307] }, // Château de Langeais
              // ... (ajoutez d'autres lieux au besoin)
            ],
          },
          {
            id: 25,
            name: 'Parcours des Jardins Élégants',
            listeLieu: [
              { monumentId: 5, location: [0.5110, 47.3423] }, // Château de Villandry
              { monumentId: 12, location: [0.9760, 47.4826] }, // Château de Chaumont-sur-Loire
              { monumentId: 18, location: [1.9583, 47.8151] }, // Château de La Ferté-Saint-Aubin
              // ... (ajoutez d'autres lieux au besoin)
            ],
          },
          // Ajoutez d'autres parcours au besoin...
        ];


        /* Le bloc de code parcourt un ensemble de monuments et crée des graphiques pour chaque
        monument sur la carte. */
        monuments.forEach(monument => {
          const point = {
            type: 'point',
            longitude: monument.location[0],
            latitude: monument.location[1],
          };

          const markerSymbol = {
            type: 'simple-marker',
            color: [18, 170, 54],
            outline: {
              color: [255, 255, 255],
              width: 2,
            },
          };

          const pointGraphic = new Graphic({
            geometry: point,
            symbol: markerSymbol,
            attributes: {
              name: monument.name,
              id: monument.id,
            },
          });

          const popupTemplate = {
            title: '{name}',
            content: `<a href="/lieux/${monument.id}">Voir le détail de '${monument.name}'</a>`,
          };

          pointGraphic.popupTemplate = popupTemplate;

          monumentsLayer.add(pointGraphic);
        });


        /* Le code ci-dessous parcourt un tableau appelé "parcours" et crée un graphique polyligne pour
        chaque élément du tableau. Chaque polyligne représente un chemin avec plusieurs Lieu.
        Le code définit la couleur et la largeur de la polyligne, ainsi qu'un modèle contextuel qui
        sera affiché lorsque vous cliquerez sur la polyligne. Enfin, le graphique polyligne est
        ajouté à un calque appelé « monumentsLayer ». */
        parcours.forEach(parcour => {
          const path = {
            type: 'polyline',
            paths: parcour.listeLieu.map(waypoint => waypoint.location),
          };

          const lineSymbol = {
            type: 'simple-line',
            color: [0, 159, 227],
            width: 2,
          };

          const pathGraphic = new Graphic({
            geometry: path,
            symbol: lineSymbol,
            attributes: {
              name: parcour.name,
              id: parcour.id,
            },
          });

          const popupTemplate = {
            title: '{name}',
            content: `<p>Ce parcours inclut plusieurs lieux. <a href="/parcours/${parcour.id}">Voir les détails du parcours</a></p>`,
          };

          pathGraphic.popupTemplate = popupTemplate;

          monumentsLayer.add(pathGraphic);
        });




        /* Ce code ajoute un écouteur d'événement de clic à la couche graphique `monumentsLayer`.
        Lorsqu'un utilisateur clique sur un monument sur la carte, les attributs du monument
        sélectionné sont définis à l'aide de `setSelectedMonument(event.graphic.attributes)`. La vue
        se déplace ensuite vers l'emplacement du monument cliqué en utilisant `view.goTo()` avec une
        cible de la géométrie du monument cliqué et un niveau de zoom de 12. Enfin, le tableau
        `monuments` est défini comme variable d'état `monumentsList` en utilisant `
        setMonumentsList(monuments)`. */
        monumentsLayer.on('click', event => {
          setSelectedMonument(event.graphic.attributes);
          view.goTo({
            target: event.graphic.geometry,
            zoom: 12,
          });
        });

        setMonumentsList(monuments);
        setParcoursList(parcours);

        const viewMonumentOnMap = (location) => {
          if (view) {
            view.goTo({
              center: location,
              zoom: 12,
            });
          } else {
            console.error("View is undefined.");
          }
        };

        const directionsWidget = new Directions({
          view: view,
        });

        view.ui.add(directionsWidget, 'top-right');

        const searchWidget = new Search({
          view: view,
          resultGraphicEnabled: false,
          popupEnabled: false,
        });

        view.ui.add(searchWidget, 'top-left');

        return () => {
          if (view) {
            view.destroy();
          }
        };
      })
      .catch(err => console.error(err));
  }, [selectedMap]);

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
    .filter(item => item.name.toLowerCase().includes(searchTerm.toLowerCase()))
    .slice(startIndex, endIndex);

  return (
    <div className='mainCarte'>
      <div className=' divContainerCarte d-flex justify-content-center align-items-center'>
        <div className='ContainerCarteVert d-flex justify-content-center align-items-center'>
          <h1 className='d-flex titreCarte justify-content-center'>"Carte"</h1>
        </div>
      </div>
      <div className='d-flex justify-content-center fondVertLieux'>
        <div id="map-view" style={{ height: '75vh', width: '75vw' }}></div>
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
                    <h5 className="card-title titleMonument">{item.name}</h5>
                    <div>
                      <a href={showParcoursTab ? `/parcours/${item.id}` : `/lieux/${item.id}`}>
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


