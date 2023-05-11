const load = () => {
    const marketUrl = 'http://localhost:8000/get_markets'
    const countryUrl = 'http://localhost:8000/get_countries'
    $.get(marketUrl, (data, status) => {
        if (data) {
            const markets = data.markets
            const uiMarket = document.getElementById('market')
            for (m in markets) {
                const opt = new Option((text = m), (value = markets[m]))
                uiMarket.append(opt)
            }
        }
    })
    $.get(countryUrl, (data, status) => {
        if (data) {
            const countries = data.countries
            const uiCountry = document.getElementById('country')
            for (c in countries) {
                const opt = new Option((text = c), (value = countries[c]))
                uiCountry.append(opt)
            }
        }
    })
}

const estimate = () => {
    const url = 'http://localhost:8000/estimate'
    const nRounds = document.getElementById('nRounds').value
    const founded = document.getElementById('founded').value
    const first = document.getElementById('first').value
    const last = document.getElementById('last').value
    const market = document.getElementById('market').value
    const country = document.getElementById('country').value
    const investment = document.getElementById('investment').value

    $.post(
        url,
        {
            nRounds: parseFloat(nRounds),
            founded,
            first,
            last,
            market,
            country,
            investment,
        },
        (data, status) => {
            // console.log(data)
            alert(`Given startup will be ${data.status}!`)
        }
    )
}

window.onload = load()
