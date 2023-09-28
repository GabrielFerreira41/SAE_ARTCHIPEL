import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.css';
import './index.css';
import App from './App';
import Header from './components/Header'
import Accueil from './components/Accueil'
import Lieux from './components/Lieux'
import reportWebVitals from './reportWebVitals';
import { BrowserRouter as Router, Route, Switch, Redirect } from 'react-router-dom';
import './style/bootstrap.css'
import './style/bootstrap.min.css'
import './style/bootstrap.rtl.css'
import './style/bootstrap.rtl.min.css'



ReactDOM.render(
  <React.StrictMode>
    <Header></Header>
    <App/>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();