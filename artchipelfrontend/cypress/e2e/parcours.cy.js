
context('Parcours', () => {
    beforeEach(() => {
      cy.visit('http://localhost:3000/parcours'); // Replace with your actual development server URL
    });
  
    it('should open a modal when clicking on a parcours item', () => {
      cy.get('.parcours-item').first().click();
      cy.get('.popUp').should('be.visible');
    });
  
    it('should close the modal when clicking the close button', () => {
      cy.get('.parcours-item').first().click();
      cy.get('.buttonClosePopUp').click();
      cy.get('.parcours-item').should('be.visible');
    });
  
    it('should display the selected parcours title in the modal', () => {
      cy.get('.parcours-item').first().click();
      cy.get('.popUp h1').should('have.text', 'Parcours A'); // Adjust based on your test data
    });
  
    it('should navigate to the map when clicking "Voir sur la Carte"', () => {
      cy.get('.parcours-item').first().click();
      cy.get('.popUp button').click();
      // Add assertions or interactions for the map view
    });
  
    it('should display the list of lieux in the modal', () => {
      cy.get('.parcours-item').first().click();
      cy.get('.lieux-list li').should('have.length', 10); // Adjust based on your test data
    });
  
    it('should close the modal when clicking outside the modal content', () => {
      cy.get('.parcours-item').first().click();
      cy.get('.popUp').click('topLeft'); // Click outside the modal content
      cy.get('.parcours-item').should('be.visible');
    });
  });
  