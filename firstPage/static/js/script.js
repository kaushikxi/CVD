document.querySelector(".input-parameters-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const age = document.forms[0].elements[1].value
    const gender = document.forms[0].elements[2].value
    const cp = document.forms[0].elements[3].value
    const trestbps = document.forms[0].elements[4].value
    const chol = document.forms[0].elements[5].value
    const fbs = document.forms[0].elements[6].value
    const restecg = document.forms[0].elements[7].value
    const thalch = document.forms[0].elements[8].value
    const ca = document.forms[0].elements[9].value
    // const thal = document.forms[0].elements[10].value

    let gender0 = 0;
    let gender1 = 0;
    let cpArray = [0, 0, 0, 0];
    let fbs0 = 0;
    let fbs1 = 0;
    let restecgArray = [0, 0, 0];
    let caArray = [0, 0, 0, 0, 0];

    gender === "1" ? gender1 = 1 : gender0 = 1;
    cpArray[cp] = 1;
    fbs === "1" ? fbs1 = 1: fbs0 = 1;
    restecgArray[restecg] = 1;
    caArray[ca] = 1;

    let data = {
        age,
        trestbps,
        chol,
        thalch,
        gender0,
        gender1,
        cp0: cpArray[0],
        cp1: cpArray[1],
        cp2: cpArray[2],
        cp3: cpArray[3],
        fbs0,
        fbs1,
        restecg0: restecgArray[0],
        restecg1: restecgArray[1],
        restecg2: restecgArray[2],
        ca0: caArray[0],
        ca1: caArray[1],
        ca2: caArray[2],
        ca3: caArray[3],
        ca4: caArray[4]
    }

        fetch('http://127.0.0.1:8000/predictdisease', {
            method: 'POST',
            body: JSON.stringify(data)
        }).then(response => response.text())
        .then(data => {
            console.log(data.toString());
            if(data === "0"){
                document.querySelector(".result-box").innerHTML = "<p>You're not likely having any Cardio Vascular Disease.</p>"
            } else if(data === "1") {
                document.querySelector(".result-box").innerHTML = "<p>You're likely to have a Cardio Vascular Disease.</p>"
            }
        })
});
