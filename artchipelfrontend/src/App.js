// import React, { Component } from "react";
// import axios from "axios";

// class App extends Component {
//   constructor(props) {
//     super(props);
//     this.state = {
//       donneesApi: [], // Changer le nom de l'état à "donneesApi"
//     };
//   }

//   componentDidMount() {
//     this.fetchDataFromAPI();
//   }

//   fetchDataFromAPI = () => {
//     axios
//       .get("https://data.centrevaldeloire.fr/api/explore/v2.1/catalog/datasets/inventaire-du-patrimoine-en-region-centre-val-de-loire/records?limit=100")
//       .then((res) => this.setState({ donneesApi: res.data.results })) // Utilisez "donneesApi" au lieu de "todoList"
//       .catch((err) => console.log(err));
//   };

//   render() {
//     const { donneesApi } = this.state; // Utilisez "donneesApi" au lieu de "todoList"

//     return (
//       <div>
//         <h1>Données de l'API</h1>
//         <ul>
//           {donneesApi.map((item, index) => ( // Ajoutez un attribut "key" unique
//             <li key={index}>{item.etud}</li>
//           ))}
//         </ul>
//       </div>
//     );
//   }
// }

// export default App;
import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';

import Accueil from './components/Accueil';
import Lieux from './components/Lieux';
import Info from './components/Info';
import Decouverte from './components/Decouverte';
import Evenement from './components/Evenement';
import Parcours from './components/Parcours';
import Lieu from './components/Lieu';


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Accueil />} />
        <Route path="/Lieux" element={<Lieux />} />
        <Route path="/lieux/:id" component={Lieu} />
        <Route path="/Info" element={<Info />} />
        <Route path="/Decouverte" element={<Decouverte />} />
        <Route path="/Evenement" element={<Evenement/>}/>
        <Route path='/Parcours' element={<Parcours/>}/>
        </Routes>
    </Router>
  );
}

export default App;

