async function loadCurrecies() {
    try {   
        const response = await axios.get('http://localhost:5500/api/currencies');
        const currencies = response.data; 

        currencies.forEach(([id, name, symbol]) => {
            //Extracting from Tuple used in Flask
            const option = `<option value="${id}">${name} (${id})${symbol ? ' ' + symbol : ''}</option>`;
            // May change Selcetion to & from currency based on api usecases w/in dropdown menu
            // baseCurrencySelect to fromSelect
            // quoteCurrencySelect to toSelect
            baseCurrencySelect.insertAdjacentHTML('beforeend', option); 
            quoteCurrencySelect.insertAdjacentHTML('beforeend', option);
        });

    } 
    
    catch (error) {
        console.error('Error loading currencies:', error);
    }
}

async function convertCurrencies(){

}