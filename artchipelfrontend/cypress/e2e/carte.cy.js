// carte_spec.js
describe('Page Carte', () => {
    beforeEach(() => {
      cy.visit('http://localhost:3000/carte'); 
    });
  
    it('devrait afficher la carte', () => {
      cy.get('#map-view').should('be.visible');
    });
  
    it('devrait afficher la liste des lieux par défaut', () => {
      cy.get('.titreCarteListeLieux').should('have.class', 'mt-5');
    });
  
    it('devrait permettre de rechercher des lieux', () => {
      const searchTerm = 'Château de Chambord';
      cy.get('.searchBar').type(searchTerm);
      cy.get('.carteListeLieuxVert').should('have.length', 1);
      cy.contains('.titleMonument', searchTerm);
    });
  
    it('devrait permettre de basculer entre la liste des lieux et la liste des parcours', () => {
      cy.get('.titreCarteListeParcours').click();
      //continuer test un fois BD OK
    });
  
    it('devrait afficher les détails d\'un lieu', () => {
      cy.get('.carteListeLieuxVert').first().contains('Détails').click();
      cy.url().should('include', '/lieux/');
      // Ajoutez des assertions spécifiques à la page des détails des lieux si nécessaire
    });
  
    it('devrait afficher les détails d\'un parcours', () => {
      cy.get('.titreCarteListeParcours').click();
      cy.get('.carteListeParcoursBleu').first().contains('Détails').click();
      cy.url().should('include', '/parcours/');
    });
  
    it('devrait afficher un monument sur la carte après avoir cliqué sur "Voir sur la carte"', () => {
      cy.get('.carteListeLieuxVert').first().contains('Voir sur la carte').click();
      cy.get('.esri-view').should('be.visible'); 
    });
  
    it('devrait permettre de naviguer entre les pages de la liste des lieux', () => {
      cy.get('.pagination').should('be.visible');
      cy.get('.pagination').contains('2').click();
      cy.get('.page-item.active').should('contain', '2');
    });
  });
  