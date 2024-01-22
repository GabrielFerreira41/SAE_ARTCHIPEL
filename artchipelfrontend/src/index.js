/* Le code importe divers modules et feuilles de style nécessaires à l'application. */
import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.css';
import './index.css';
import App from './App';
import Header from './components/Header'
import Footer from './components/Footer'
import reportWebVitals from './reportWebVitals';
import './style/bootstrap.css'
import './style/bootstrap.min.css'
import './style/bootstrap.rtl.css'
import './style/bootstrap.rtl.min.css'
import "./style/styleHeader.css";
import './style/styleApp.css'




/* `ReactDOM.render()` est une méthode dans React qui est utilisée pour restituer les éléments React
dans le DOM (Document Object Model). */
ReactDOM.render(
  <React.StrictMode>
    <Header></Header>
    <App/>
    <Footer></Footer>

  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();