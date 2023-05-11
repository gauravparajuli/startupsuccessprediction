const loadLocations = () => {
    const url = 'http://localhost:5000/get_location_names'
    $.get(url, (data, status) => {
        if (data) {
            const locations = data.locations
            const uiLocation = document.getElementById('location')
            for (loc in locations) {
                const opt = new Option(locations[loc])
                uiLocation.append(opt)
            }
        }
    })
}

const getBhkValue = () => {
    var uiBhks = document.getElementsByName('bhk')
    for (i in uiBhks) {
        if (uiBhks[i].checked) {
            return parseInt(i) + 1
        }
    }
}

const getBathValue = () => {
    var uiBaths = document.getElementsByName('bath')
    for (i in uiBaths) {
        if (uiBaths[i].checked) {
            return parseInt(i) + 1
        }
    }
}

const onPredictSucccessClick = () => {
    const url = 'http://localhost:5000/estimate'
    const sqft = document.getElementById('area')
    const bhk = getBhkValue()
    const bath = getBathValue()
    const location = document.getElementById('location')
    $.post(
        url,
        {
            total_sqft: parseFloat(sqft.value),
            bhk,
            bath,
            location: location.value,
        },
        (data, status) => {
            // console.log(data)
            alert(`Estimated Price is: ${data.estimated_price} lakh(s)`)
        }
    )
}

window.onload = loadLocations()
