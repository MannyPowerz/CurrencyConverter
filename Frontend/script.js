async function loadCurrecies() 
{
    try 
    {   
        const response = await axios.get('http://localhost:5500/api/currencies');
        const currencies = response.data; 

        const baseCurrencySelect = document.getElementById('baseCurrencySelect');
        const quoteCurrencySelect = document.getElementById('quoteCurrencySelect');

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
    
    catch (error) 
    {
        console.error('Error loading currencies:', error);
    }
}

async function renderExchangeRate()
{

    const baseCurrencySelect = document.getElementById('baseCurrencySelect').value;
    const quoteCurrencySelect = document.getElementById('quoteCurrencySelect').value;
    const exchangeRateDiv = document.getElementById('exchangeRate') ;

    if (!baseCurrencySelect || !quoteCurrencySelect) 
    {
        exchangeRateDiv.innerHTML = '';
        return;
    }
    
    try
    {
        const response = await axois.get('http://localhost:5500/api/exchange-rate', 
        {
            params: 
            {   
                currency1: baseCurrencySelect,
                currency2: quoteCurrencySelect,
            }
        } );
        
        const rate = respoonse.data.rate;
        const formattedRate = rate.toFixed(4);

        exchangeRateDiv.innerHTML = '<div><strong>Exchange Rate:</strong> ${fromCurrency}/${toCurrency} = ${formattedRate}</div>';
    }



    catch (error)
    {
        console.error('Error generating exchange rate:', error);
        exchangeRateDiv.innerHTML = 'Unable to fetch exchange rate';
    }

}

async function convertCurrencies()
{
    const baseCurrencySelect = document.getElementById('baseCurrencySelect').value;
    const quoteCurrencySelect = document.getElementById('quoteCurrencySelect').value;
    const amount = document.getElementById('amount').value;
    const resultDiv = document.getElementById('result');


    if (!baseCurrencySelect || !quoteCurrencySelect || !amount) 
    {
        resultDiv.innerHTML = 'Please fill in all the following fields';
        return;
    }

    try 
    {
        const response = await axois.get('http://localhost:5500/api/convert', 
        {
            params: 
            {   
                currency1: baseCurrencySelect,
                currency2: quoteCurrencySelect,
                amount: amount
            }
        } );

        const result = response.data.converted_amount;
        resultDiv.innerHTML = '${amount} ${baseCurrencySelect} = ${result} ${quoteCurrencySelect}';
    }

    catch (error)
    {
        console.error('Conversion error: ', error);
        resultDiv.innerHTML = 'Failed Conversion, please try again.';
    }
}
// add converted converion rate for currency as a function in the website before currencies are converted in terms of amount 