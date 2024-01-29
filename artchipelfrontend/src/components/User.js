import React from 'react';

var UserProfile = (function() {
    var isLoggedIn = false;
  
    var getIsLogged = function() {
      return isLoggedIn;
    };
  
    var setLogged = function(isLogged) {
        isLoggedIn = isLogged;     
    };
  
    return {
        getIsLogged: getIsLogged,
        setLogged: setLogged
    }
  
  })();

export default UserProfile