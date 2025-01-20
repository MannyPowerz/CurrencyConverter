// async function loadCurrencies() 
// {
//     try 
//     {   
//         const response = await axios.get('http://localhost:5000/api/currencies');
//         const currencies = response.data; 

//         const baseCurrencySelect = document.getElementById('baseCurrencySelect');
//         const quoteCurrencySelect = document.getElementById('quoteCurrencySelect');

//         currencies.forEach(([id, name, symbol]) => {
//             //Extracting from Tuple used in Flask
//             const option = `<option value="${id}">${name} (${id})${symbol ? ' ' + symbol : ''}</option>`;
//             // May change Selcetion to & from currency based on api usecases w/in dropdown menu
//             // baseCurrencySelect to fromSelect
//             // quoteCurrencySelect to toSelect
//             baseCurrencySelect.insertAdjacentHTML('beforeend', option); 
//             quoteCurrencySelect.insertAdjacentHTML('beforeend', option);
//         });

//         await renderExchangeRate();

//     } 
    
//     catch (error) 
//     {
//         console.error('Error loading currencies:', error);
//     }
// }

async function loadCurrencies() {
    try {
        const response = await axios.get('http://localhost:5000/api/currencies');
        if (response.data && Array.isArray(response.data)) {
            const currencies = response.data;

            const baseCurrencySelect = document.getElementById('baseCurrencySelect');
            const quoteCurrencySelect = document.getElementById('quoteCurrencySelect');

            // Clear any existing options in case of re-render
            baseCurrencySelect.innerHTML = '';
            quoteCurrencySelect.innerHTML = '';

            currencies.forEach(([id, name, symbol]) => {
                const option = `<option value="${id}">${name} (${id})${symbol ? ' ' + symbol : ''}</option>`;
                baseCurrencySelect.insertAdjacentHTML('beforeend', option);
                quoteCurrencySelect.insertAdjacentHTML('beforeend', option);
            });

            // Render exchange rate for the default selection
            await renderExchangeRate();
        } else {
            console.error('Invalid or empty currency list received.');
        }
    } catch (error) {
        console.error('Error loading currencies:', error);
    }
}


async function renderExchangeRate()
{

    const baseCurrency = document.getElementById('baseCurrencySelect').value;
    const quoteCurrency = document.getElementById('quoteCurrencySelect').value;
    const exchangeRateDiv = document.getElementById('exchangeRate') ;

    if (!baseCurrency || !quoteCurrency) 
    {
        exchangeRateDiv.innerHTML = '';
        return;
    }
    
    try
    {
        const response = await axios.get('http://localhost:5000/api/exchange-rate', 
        {
            params: 
            {   
                currency1: baseCurrency,
                currency2: quoteCurrency,
            }
        } );
        
        const rate = response.data.rate;
        const formattedRate = rate.toFixed(4);

        exchangeRateDiv.innerHTML = `<div><strong>Exchange Rate:</strong> ${baseCurrency}/${quoteCurrency} = ${formattedRate}</div>`;
    }



    catch (error)
    {
        console.error('Error generating exchange rate:', error);
        exchangeRateDiv.innerHTML = 'Unable to fetch exchange rate';
    }

}

async function convertCurrencies()
{
    const baseCurrency = document.getElementById('baseCurrencySelect').value;
    const quoteCurrency = document.getElementById('quoteCurrencySelect').value;
    const amount = document.getElementById('amount').value;
    const resultDiv = document.getElementById('result');


    if (!baseCurrency || !quoteCurrency || !amount) 
    {
        resultDiv.innerHTML = 'Please fill in all the following fields';
        return;
    }

    try 
    {
        const response = await axios.get('http://localhost:5000/api/convert', 
        {
            params: 
            {   
                currency1: baseCurrency,
                currency2: quoteCurrency,
                amount: amount
            }
        } );

        const result = response.data.converted_amount;
        resultDiv.innerHTML = `${amount} ${baseCurrency} = ${result} ${quoteCurrency}`;
    }

    catch (error)
    {
        console.error('Conversion error: ', error);
        resultDiv.innerHTML = 'Failed Conversion, please try again.';
    }
}

document.getElementById('baseCurrencySelect').addEventListener('change',renderExchangeRate);
document.getElementById('quoteCurrencySelect').addEventListener('change',renderExchangeRate);

document.addEventListener('DOMContentLoaded', loadCurrencies);

// add converted converion rate for currency as a function in the website before currencies are converted in terms of amount 