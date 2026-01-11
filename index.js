 
    const button = document.getElementById('button');
    button.addEventListener("click",() => {
      const message = document.querySelector('.input-box').value;
      document.querySelector('.progress-js').innerHTML = `mood sensor detecting your emotion in progress...`;
       setTimeout(() => {
        document.querySelector('.progress-js').innerHTML = '';
        moodDetector(message);
      },3000);
        
    });

    function moodDetector(message) {
      fetch("http://127.0.0.1:5000/analyze",{
      method: "POST", 
      headers: {
        "Content-Type": "application/json"
      },body: JSON.stringify({"message": message})
      })
      .then(response => response.json())
      .then(data=>{
        document.querySelector('.result-js').innerHTML = `you are now having a ${data.label} mood!!!`
        })
    };